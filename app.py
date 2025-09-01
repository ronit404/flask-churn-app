import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import pandas as pd
import numpy as np
from werkzeug.security import generate_password_hash, check_password_hash
import shap

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# --- LOAD THE ML MODELS AND EXPLAINER ---
model = pickle.load(open('churn_model.pkl', 'rb'))
model_columns = pickle.load(open('model_columns.pkl', 'rb'))
explainer = pickle.load(open('shap_explainer.pkl', 'rb'))

# --- DATABASE HELPER FUNCTION ---
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- RECOMMENDATION ENGINE ---
def generate_recommendations(factors):
    recommendations = []
    if not factors: return recommendations
    if any("Contract_Month-to-month" in f for f in factors): recommendations.append("Offer an upgrade to a 1-year contract with a discount.")
    if any("tenure" in f for f in factors): recommendations.append("Engage with a welcome call or tutorial for new customers.")
    if any("MonthlyCharges" in f for f in factors): recommendations.append("Review their plan for cost-saving opportunities.")
    if not recommendations: recommendations.append("Proactively contact the customer to address potential dissatisfaction.")
    return recommendations[:2]

# --- APP ROUTES ---
@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        # Check the session for results from a previous prediction, then clear them.
        # .pop() gets the value and removes it, so it's only shown once.
        prediction_text = session.pop('prediction_text', None)
        confidence_score = session.pop('confidence_score', None)
        top_factors = session.pop('top_factors', None)
        recommendations = session.pop('recommendations', None)
        
        return render_template('index.html', 
                               prediction_text=prediction_text,
                               confidence_score=confidence_score,
                               top_factors=top_factors,
                               recommendations=recommendations)

# ... (login, signup, logout routes are unchanged) ...
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not username or not password:
            error = 'Please enter both username and password.'
        else:
            conn = get_db_connection()
            user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
            conn.close()
            
            if user and check_password_hash(user['password'], password):
                session['logged_in'] = True
                session['username'] = user['username']
                return redirect(url_for('home'))
            else:
                error = 'Invalid username or password. Please try again.'
    
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    success = None
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not username or not password:
            error = 'Please enter both username and password.'
        elif len(password) < 6:
            error = 'Password must be at least 6 characters long.'
        else:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            try:
                conn = get_db_connection()
                conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
                conn.commit()
                conn.close()
                success = 'Account created successfully! Please log in.'
            except sqlite3.IntegrityError:
                error = 'Username already exists. Please choose a different username.'
    
    return render_template('signup.html', error=error, success=success)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/predict', methods=['POST'])
def predict():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    # ... (form data gathering and processing is the same) ...
    form_data = {'tenure': float(request.form.get('tenure')), 'MonthlyCharges': float(request.form.get('monthly_charges')), 'Contract': request.form.get('contract'), 'Partner': request.form.get('partner'), 'Dependents': request.form.get('dependents'), 'gender': request.form.get('gender'), 'PaymentMethod': request.form.get('payment_method'), 'InternetService': request.form.get('internet_service'), 'OnlineSecurity': request.form.get('online_security'),}
    input_data = {**form_data, 'PhoneService': ['Yes'], 'MultipleLines': ['No'], 'OnlineBackup': ['No'], 'PaperlessBilling': ['Yes'], 'DeviceProtection': ['No'], 'TechSupport': ['No'], 'StreamingTV': ['No'], 'StreamingMovies': ['No'], 'TotalCharges': [form_data['MonthlyCharges'] * form_data['tenure']]}
    input_df = pd.DataFrame(input_data)
    input_df_encoded = pd.get_dummies(input_df)
    input_df_aligned = input_df_encoded.reindex(columns=model_columns, fill_value=0)
    
    prediction = model.predict(input_df_aligned)
    prediction_proba = model.predict_proba(input_df_aligned)
    
    if prediction[0] == 1:
        session['prediction_text'] = "This customer is LIKELY to churn."
        session['confidence_score'] = f"{prediction_proba[0][1]*100:.2f}%"
        
        shap_values_obj = explainer(input_df_aligned)
        shap_values = shap_values_obj.values[:, :, 1]
        feature_names = input_df_aligned.columns
        feature_impacts = pd.DataFrame(list(zip(feature_names, shap_values[0])), columns=['feature', 'impact']).sort_values(by='impact', ascending=False)
        top_factors = feature_impacts.head(3)['feature'].tolist()

        session['top_factors'] = top_factors
        session['recommendations'] = generate_recommendations(top_factors)
    else:
        session['prediction_text'] = "This customer is UNLIKELY to churn."
        session['confidence_score'] = f"{prediction_proba[0][0]*100:.2f}%"
        session['top_factors'] = []
        session['recommendations'] = []

    # Redirect back to the homepage to display the results
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


# Churn Predictor Pro 🚀

A modern, AI-powered customer churn prediction application built with Flask and machine learning. This professional tool helps businesses identify customers at risk of churning and provides actionable recommendations to improve customer retention.

![Churn Predictor Pro](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-orange)

## ✨ Features

### 🎯 Core Functionality
- **AI-Powered Predictions**: Advanced machine learning algorithms for accurate churn prediction
- **Real-time Analysis**: Instant predictions with detailed risk factor analysis
- **Actionable Insights**: Specific recommendations to prevent customer churn
- **SHAP Explanations**: Transparent AI with feature importance explanations

### 🎨 Modern UI/UX
- **Professional Design**: Clean, modern interface with gradient themes
- **Responsive Layout**: Works seamlessly on desktop and mobile devices
- **Interactive Elements**: Smooth animations and hover effects
- **User Authentication**: Secure login/signup system

### 📊 Analytics & Insights
- **Risk Assessment**: High/Low risk indicators with confidence scores
- **Factor Analysis**: Top contributing factors to churn risk
- **Recommendation Engine**: AI-generated actionable recommendations
- **Visual Feedback**: Color-coded status indicators and progress bars

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Machine Learning**: Scikit-learn, SHAP (SHapley Additive exPlanations)
- **Database**: SQLite with SQLAlchemy
- **Authentication**: Werkzeug password hashing
- **Styling**: Custom CSS with modern gradients and animations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd flask-churn-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database**
   ```bash
   python init_db.py
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Create an account or log in
   - Start predicting customer churn!

## 📋 Usage Guide

### 1. User Registration/Login
- Create a new account with username and password
- Secure authentication with password hashing
- Session management for logged-in users

### 2. Customer Data Input
The application collects the following customer information:

#### **Customer Profile**
- **Tenure**: How long the customer has been with the company (months)
- **Monthly Charges**: Current monthly billing amount ($)
- **Contract Type**: Month-to-month, One year, or Two year

#### **Demographics**
- **Partner**: Whether the customer has a partner
- **Dependents**: Whether the customer has dependents
- **Gender**: Customer's gender
- **Payment Method**: Electronic check, Mailed check, Bank transfer, or Credit card

#### **Services**
- **Internet Service**: DSL, Fiber optic, or No internet
- **Online Security**: Yes, No, or N/A

### 3. Prediction Results
After submitting customer data, you'll receive:

- **Churn Risk Assessment**: High/Low risk with confidence percentage
- **Top Risk Factors**: Key factors contributing to churn risk
- **Actionable Recommendations**: Specific steps to retain the customer
- **Quick Actions**: Suggested next steps (Call Customer, Send Offer, View History)

## 🏗️ Project Structure

```
flask-churn-app/
├── app.py                 # Main Flask application
├── init_db.py            # Database initialization
├── generate_explainer.py # SHAP explainer generation
├── churn_model.pkl       # Trained machine learning model
├── model_columns.pkl     # Model feature columns
├── shap_explainer.pkl    # SHAP explainer for model interpretation
├── database.db           # SQLite database
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── static/
│   └── style.css        # Custom CSS styles
└── templates/
    ├── base.html        # Base template
    ├── index.html       # Main dashboard
    ├── login.html       # Login page
    └── signup.html      # Signup page
```

## 🔧 Configuration

### Environment Variables
The application uses the following configuration:

- `SECRET_KEY`: Flask secret key for session management
- `DEBUG`: Enable/disable debug mode

### Model Configuration
- The machine learning model is pre-trained and saved as `churn_model.pkl`
- SHAP explainer is generated and saved as `shap_explainer.pkl`
- Feature columns are saved as `model_columns.pkl`

## 🎯 Machine Learning Model

### Model Details
- **Algorithm**: Random Forest Classifier
- **Features**: 20+ customer attributes
- **Performance**: High accuracy with SHAP explanations
- **Interpretability**: Transparent AI with feature importance

### SHAP Explanations
The application uses SHAP (SHapley Additive exPlanations) to provide:
- Feature importance rankings
- Individual prediction explanations
- Transparent AI decision-making

## 🔒 Security Features

- **Password Hashing**: Secure password storage using Werkzeug
- **Session Management**: Secure user sessions
- **Input Validation**: Form validation and sanitization
- **SQL Injection Protection**: Parameterized queries

## 📱 Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production deployment, consider:
- Using a production WSGI server (Gunicorn, uWSGI)
- Setting up a reverse proxy (Nginx)
- Using a production database (PostgreSQL, MySQL)
- Implementing HTTPS
- Setting up monitoring and logging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Flask community for the excellent web framework
- Scikit-learn team for machine learning tools
- SHAP developers for model interpretability
- Bootstrap team for the responsive CSS framework

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

---

**Made with ❤️ for better customer retention**


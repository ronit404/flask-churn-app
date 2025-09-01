import pickle
import shap
import pandas as pd # Add pandas import just in case for compatibility

# Load the trained RandomForest model
print("Loading the trained model...")
model = pickle.load(open('churn_model.pkl', 'rb'))
print("Model loaded successfully.")

# Create a SHAP TreeExplainer object. This object is specifically designed for tree-based models like RandomForest.
# The explainer learns how the model makes decisions.
print("Creating SHAP explainer...")
explainer = shap.TreeExplainer(model)
print("Explainer created successfully.")

# Save the explainer object to a file for use in our Flask app#  
print("Saving the explainer to 'shap_explainer.pkl'...")
with open('shap_explainer.pkl', 'wb') as file: 
    pickle.dump(explainer, file)

print("Explainer saved successfully. You can now use it in your app.")
    


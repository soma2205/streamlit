# import necessary libraries
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor  # You can replace this with your preferred ML model

# Create a simple RandomForestRegressor model (you can replace it with your own model)
model = RandomForestRegressor()

# Function to predict runs based on input features
def predict_runs(features):
    # You should replace this with your model prediction logic
    # For now, we'll just return a random number
    return int(features['wickets']) * 10

# Streamlit app
def main():
    st.title("Cricket Run Predictor")

    # Collect user input
    st.sidebar.header("Input Features")
    overs = st.sidebar.slider("Overs", 0.0, 50.0, 10.0)
    wickets = st.sidebar.slider("Wickets", 0, 10, 2)
    runs = st.sidebar.slider("Runs", 0, 300, 150)
    # You can add more input features as needed

    features = {
        'overs': overs,
        'wickets': wickets,
        'runs': runs,
        # Add more features as needed
    }

    # Predict runs
    predicted_runs = predict_runs(features)

    # Display the prediction
    st.write(f"Predicted Runs: {predicted_runs}")

# Run the app
if __name__ == "__main__":
    main()

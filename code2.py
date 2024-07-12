# Version 2 of deployment code 

import streamlit as st
import numpy as np
import joblib

# Load the serialized model
try:
    loaded_model = joblib.load("D:\\PYTHON PROJECTS\\Machine learning\\Portfolio\\CAR_PRICE Pj\\Car.joblib1")
    st.write("Model loaded successfully.")
except Exception as e:
    st.error(f"Error loading model: {e}")

# Creating a function for prediction
def Price_prediction(features):
    try:
        # Convert data to numeric values
        data_array = np.asarray(features, dtype=np.float64)
        # Reshape the array as we are predicting for one instance
        data_reshaped = data_array.reshape(1, -1)

        prediction = loaded_model.predict(data_reshaped)
        return prediction[0]
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None

def main():
    # Giving title
    st.title("Car Price Prediction")

    # Getting data from the user
    Car_Name = st.selectbox("Car_Name", ["fortuner", "corolla altis", "city"])  # Categorical field
    Year = st.text_input("Year")
    Present_Price = st.text_input("Present_Price")
    Kms_Driven = st.text_input("Kms_Driven")
    Fuel_Type = st.selectbox("Fuel_Type", ["Petrol", "Diesel", "CNG"])  # Categorical field
    Seller_Type = st.selectbox("Seller_Type", ["Dealer", "Individual"])  # Categorical field
    Transmission = st.selectbox("Transmission", ["Manual", "Automatic"])  # Categorical field

    # Code for prediction
    prediction = ''
    
    # Creating a button for prediction
    if st.button('Car price result'):

        # Check if any input field is empty
        if not Year or not Present_Price or not Kms_Driven:
            st.error("Please enter valid numeric values for Year, Present Price, and Kms Driven.")
            return

        try:
            # Convert input values to float for numeric fields
            Year = float(Year)
            Present_Price = float(Present_Price)
            Kms_Driven = float(Kms_Driven)

            # Convert categorical fields to numeric codes
            Car_Name_dict = {"fortuner": 3, "corolla altis": 2, "city": 1}
            Fuel_Type_dict = {"Petrol": 0, "Diesel": 1, "CNG": 2}
            Seller_Type_dict = {"Dealer": 0, "Individual": 1}
            Transmission_dict = {"Manual": 0, "Automatic": 1}

            Car_Name = Car_Name_dict[Car_Name]
            Fuel_Type = Fuel_Type_dict[Fuel_Type]
            Seller_Type = Seller_Type_dict[Seller_Type]
            Transmission = Transmission_dict[Transmission]

            # Features for prediction
            features = [Car_Name,Year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission]

            # Make prediction
            prediction = Price_prediction(features)
            prediction = prediction*100
            if prediction is not None:
                st.success(f"Predicted Car Price: {prediction:.2f} USD")
            else:
                st.error("Prediction failed.")

        except ValueError as e:
            st.error(f"Error in input values: {e}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()

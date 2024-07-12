import streamlit as st
import pandas as pd
import numpy as np
import joblib


# Load the serialized model
loaded_model = joblib.load("D:\PYTHON PROJECTS\Machine learning\Portfolio\CAR_PRICE Pj\Car.joblib1")
# Creating a function for prediction
def Price_prediction(filtered_df):
    # Convert data to numeric values
    data_array = np.asarray(filtered_df, dtype=np.float64)
    # Reshape the array as we are predicting for one instance
    data_reshaped = data_array.reshape(1, -1)

    prediction = loaded_model.predict(data_reshaped)
    print(prediction)

    return prediction[0]
        

def main():
    # Giving title
    st.title("Car Price Prediction")
    # Getting data from the user

    Car_Name = st.text_input("Car_Name")
    Year = st.text_input("Year")
    Present_Price = st.text_input("Present_Price")
    Kms_Driven = st.text_input("Kms_Driven")
    Fuel_Type = st.text_input("Fuel_Type")
    Seller_Type = st.text_input("Seller_Type")
    Transmission = st.text_input("Transmission")

    # Code for prediction
    diagnosis = ''
    
    # Creating a button for prediction
    if st.button('Car price result'):
    
        # Convert input values to float
        Car_Name = int(Car_Name)
        Year = float(Year)
        Present_Price = float(Present_Price)
        Kms_Driven = float(Kms_Driven)
        Fuel_Type = int(Fuel_Type)
        Seller_Type = int(Seller_Type)
        Transmission = int(Transmission)

        diagnosis = Price_prediction([Car_Name, Year, Present_Price, Kms_Driven, Fuel_Type,Seller_Type,Transmission])
        

    st.success(diagnosis)

if __name__ == '__main__':
    main()

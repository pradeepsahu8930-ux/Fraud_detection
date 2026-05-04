import streamlit as st
import pandas as pd
import joblib

model=joblib.load("fraud_detection_pipeline.pkl")       #Loads: 
                                                        # preprocessing
                                                        # trained model
st.title("Fraud Detection Prediction App")

st.markdown("Please enter the transaction detailes and use the predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT"])

amount = st.number_input("Amount", min_value = 0.0, value=1000.0)   #min_value=0.0 → no negative amount     value=1000.0 → default
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value = 0.0, value=10000.0) #Balance before transaction
newbalanceOrig = st.number_input("New Balance (Sender)", min_value= 0.0, value=9000.0) #Balance after transaction
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value= 0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{        #type      amount   oldbalanceOrg ...
                                        #TRANSFER  1000     10000
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
        }])
    prediction = model.predict(input_data)[0]
    
    st.subheader(f"Prediction:'{int(prediction)}'")   #Show prediction value
    if prediction == 1:
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction looks like it is not a fraud")
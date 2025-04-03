import streamlit as st
import sklearn
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Bike sharing")
st.markdown(
    "The dataset contains modifications with regards to the original for illustrative & learning purposes"
)
num_input_previous = st.number_input("Insert the registered bikes", min_value=654, max_value=5000, value=bikes_registered)
user_input = [[bikes_registered]]

if st.button('Predict?'):
    st.write("The model predicts the bikes registered:", model.predict(user_input).round(2))

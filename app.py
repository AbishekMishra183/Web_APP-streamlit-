import streamlit as st 
from predict import predict_diabetes  # ✅ Corrected import

st.set_page_config(page_title='Diabetes Prediction App')

st.title('Diabetes Prediction')
st.header('Input your Data:')

glucose = st.number_input('Glucose', min_value=0, max_value=400, value=20)
blood_pressure = st.number_input('Blood Pressure', 0, 200, 0)
dfp = st.number_input('DFP', 0, 20, 0)
age = st.number_input('Age', 20, 80, 40)

st.sidebar.header("hihiihihihihihihihihihiiih")

if st.button('Test Diabetes'):
    input_data = [glucose, blood_pressure, dfp, age]
    result = predict_diabetes(input_data)

    if result[0] == 1:
        st.error('High probability of Diabetes')
    else:
        st.success("Congratulations, you have no diabetes.")

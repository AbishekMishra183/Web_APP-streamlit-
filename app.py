import streamlit as st
from predict import predict #file ko name predict_diabets fumction lai cl gareko
#if we import filename only then we call by using filename.function_name
st.set_page_config(page_title='Diabetes Preidicition App')

st.title('Diabetes Predicition')
st.header('Input your Data:')



glucose=st.number_input('Glucose', min_value=0 , max_value=400,value=20)
blood_pressure=st.number_input('Blood_Pressure' , 0, 200, 0)
dfp=st.number_input('DFP' , 0, 20, 0)
age=st.number_input('Age',20,80,40)
st.sidebar.header("hihiihihihihihihihihihiiih")
if st.button('Test Diabetes'): # button le k k kaam garney yah mention huna parcha
  input_data=[glucose, blood_pressure,dfp,age]
  result=predict_diabetes(input_data)
  print(result)

  if result[0]==1 :
    st.error('High probability of Diabetes')

  else :
    st.error("Congratulation you have no diabetes")

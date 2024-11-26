import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pickle 

#load model
model = tf.keras.models.load_model('model.h5')

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('label_encoder_gender.pkl', 'rb') as f:
    encoder_gender = pickle.load(f)    

with open('onehot_encoder_geo.pkl', 'rb') as f:
    onehotencoder_geo = pickle.load(f)

st.title('Customer Churn Prediction')

#input
gender = st.selectbox('Gender', encoder_gender.classes_)
geography = st.selectbox('Geography', onehotencoder_geo.categories_[0])
age = st.slider('Age', min_value=0, max_value=100)
tenure = st.slider('Tenure', min_value=0, max_value=10)
balance = st.number_input('Balance', min_value=0.0)
num_of_products = st.slider('Number of Products', min_value=1, max_value=4)
has_credit_card = st.selectbox('Has Credit Card', [1, 0])
is_active_member = st.selectbox('Is Active Member', [1, 0])
estimated_salary = st.number_input('Estimated Salary', min_value=0.0)   
credit_score = st.number_input('Credit Score', min_value=0, max_value=1000) 

input_data = pd.DataFrame({
        'CreditScore': [credit_score],
        'Gender': [encoder_gender.transform([[gender]])[0]],
        'Age': [age],    
        'Tenure': [tenure],
        'Balance': [balance],    
        'NumOfProducts': [num_of_products],
        'HasCrCard': [has_credit_card],
        'IsActiveMember': [is_active_member],
        'EstimatedSalary': [estimated_salary]
})

# 
geo_encoded = onehotencoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehotencoder_geo.get_feature_names_out(["Geography"]))

input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)
input_df_scaler = scaler.transform(input_data)

prediction = model.predict(input_df_scaler)
predic_prob = prediction[0][0]

if predic_prob > 0.5:
    st.write('The customer will leave the bank')
else:    
    st.write('The customer will not leave the bank')
import pyrebase
import streamlit as st
from datetime import datetime
firebaseConfig = {
  'apiKey': "AIzaSyAbKQaFB3dFYAN0j8lULRl-GmQj4njPewU",
  'authDomain': "whatsapp-chat-analyzer-92e0e.firebaseapp.com",
  'projectId': "whatsapp-chat-analyzer-92e0e",
  'databaseURL':"https://whatsapp-chat-analyzer-92e0e-default-rtdb.europe-west1.firebasedatabase.app/" ,
  'storageBucket':"whatsapp-chat-analyzer-92e0e.appspot.com",
  'messagingSenderId':"1079404908115",
  'appId': "1:1079404908115:web:65c34f924644767c4e40a6",
  'measurementId': "G-G 4EFBCLV9L"
};

firebase = pyrebase.intialize_app(firebaseConfig)
auth = firebase.auth()

db= firebase.database()
storage = firebase.storage()
    
st.title("Our Community")

choice= st.selectbox('Login/Signup' , ['login' , 'Sign up'])

email =st.text_input('Email Address')
password = st.text_input('Password' , type='password')


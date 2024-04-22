import streamlit as st
import helper
import pickle
from tensorflow import keras
from keras.models import load_model
from keras.layers import Embedding
from keras import Sequential
from keras.layers import Dense,Embedding,LSTM,Bidirectional, BatchNormalization,Dropout


model = load_model('modelsq1q2.h5')

st.header('DUPLICATE QUESTION CHECKER DL')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')


find_button = st.button('Find')

if find_button:
      
   if  (len(q1) ==0) and (len(q2) ==0):
      st.header('Plese Enter both question')
   elif not q1:
      st.header('Plese Enter question 1')
   elif not q2:
      st.header('Plese Enter question 2')

   else:
      query = helper.making_query(q1,q2)
      result = model.predict(query)[0]
      
      st.header("duplicacy percentage :" + result)
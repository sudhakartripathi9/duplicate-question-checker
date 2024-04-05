import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl','rb'))

st.header('DUPLICATE QUESTION CHECKER')

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
      
      if result:
         st.header('Duplicate')
      else:
         st.header('Not Duplicate')
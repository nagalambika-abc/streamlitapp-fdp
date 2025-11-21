import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('subject wise student marks')
st.write('This is a simple barchart to display student marks in different subjects.')

data={
    'Subjects':['Data structure', 'Python', 'English', 'History', 'Geography'],
    'marks':    [85, 90, 78, 88, 92]}

df=pd.DataFrame(data)
st.subheader('student marks ')

df.set_index('Subjects', inplace=True)                 
st.bar_chart(df)

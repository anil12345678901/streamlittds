import streamlit as st
st.title("TDS Graded Assignment 8")
a = st.number_input('Insert first number:')
b = st.number_input('Insert second number:')
c = st.number_input('Insert third number:')
largest=st.maxValue(a,b,c)
st.write(largest)

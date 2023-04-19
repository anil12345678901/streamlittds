import streamlit as st
st.title("TDS Graded Assignment 8")
a = st.number_input('Insert first number:')
b = st.number_input('Insert second number:')
c = st.number_input('Insert third number:')
largest=0
if a>=b and a>=c:
  largest=a
if b>=c and b>=a:
  largest=b
if c>=a and c>=b:
  largest=c
st.write("The largest number is:" largest)

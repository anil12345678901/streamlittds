$pip install streamlit
$streamlit --version

import streamlit as st

a = int(input()) 
b = int(input()) 
c = int(input()) 
largest = 0 
if a > b and a > c:
  largest = a 
if b > a and b > c:
  largest = b 
if c > a and c > b: 
  largest = c 
st.write(largest)

$streamlit run main.py

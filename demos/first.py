import streamlit as st
import pandas as pd
data = [1,2,3,4]

data2 = {
    "India": "Rupee",
    "USA": "Dollar"
}



st.title('My first app')
st.text("This is my first app.")
# st.write(data2)

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


import streamlit as st

if st.button('Hit me'):
    st.write('clicked')
chk = st.checkbox('Check me out')
st.write(chk)
rad = st.radio('Radio', [1,2,3])
st.write(rad)
select1 = st.selectbox('Select', [1,2,3])
st.write(select1)
select2 = st.multiselect('Multiselect', [1,2,3])
st.write(select2)
slide1 = st.slider('Slide me', min_value=0, max_value=10)
st.write(slide1)
slide2 = st.select_slider('Slide to select', options=[1,'2'])
st.write(slide2)
inp = st.text_input('Enter some text')
st.write(inp)
num = st.number_input('Enter a number')
st.write(num)
text = st.text_area('Area for textual entry')
st.write(text)
dt = st.date_input('Date input')
st.write(dt)
t = st.time_input('Time entry')
st.write(t)
f = st.file_uploader('File uploader')
st.write(f)
c = st.color_picker('Pick a color')
st.write(c)
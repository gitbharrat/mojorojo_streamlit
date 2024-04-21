import streamlit as st

st.header("This is a my first web app")
st.header('_Streamlit_ is :blue[cool] :sunglasses:')


code = '''def hello():
    print("Hello, MojoRojo!")'''
st.code(code, language='python')

 
if st.button('Say hello'):
    st.write('Hello there')
else:
    st.write('Goodbye')
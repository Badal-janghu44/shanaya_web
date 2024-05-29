import streamlit as st
name=st.text_input("Enter your name")
fname=st.text_input("Enter your father name")
adr=st.text_area("Enter your text :")
classdata=st.selectbox("Enter your class",(1,2,4,5,6))
button=st.button("submit")
if button :
    st.markdown(f"""
    Name : {name}
    Fname : {fname}
    Adress : {adr}
    Class : {classdata}
""")
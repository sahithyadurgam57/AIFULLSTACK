import streamlit as st
st.set_page_config(page_title="Text Input Demo")
st.title("Text Input Demo")
name=st.text_input("Enter your name:", placeholder="e.g.minnu")
st.write(f"Hello, {name}!😁")

password=st.text_input("Enter your password:", type="password")
st.write(f"Your password has {len(password)} characters.")

comments=st.text_area("Any additional comments?", height=150)
st.write(f"Your wrote {(comments)} characters.")

if st.button("submit"):
    st.write("You clicked on submit button!")

show_message=st.checkbox("Do you want an extra message?")
if show_message:
    st.write("This is the message. Have a good day!")

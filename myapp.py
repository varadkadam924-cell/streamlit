import streamlit as st
import numpy as np
import pandas as pd

# st.title("Hello, Streamlit!")
# st.write("Streamlit : This is your first streamlit app")
# st.text("Lets go Started")

# name = st.text_input("Enter your name")
# if st.button("Submit"):
#     st.success(f"Hello {name}")

# df = pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
# st.line_chart(df)
# st.bar_chart(df)

# st.sidebar.title("Navigation")
# st.image("https://www.dataops.live/hubfs/streamlitlogo.png",caption="Sample Image")
# st.video("https://www.youtube.com/watch?v=IbSSGOFoXxg")

# upload_file = st.file_uploader("Upload a csv", type="csv")
# if upload_file:
#     df = pd.read_csv(upload_file)
#     st.dataframe(df)

st.title("Text and Markdown Demo")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**, *Italic*, Code, [Link](https://streamlit.io)")
st.code("for i in range(5): print(i)",language="python")
st.text_input("What'syour Name")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range",0, 100)
st.selectbox("Select a fruit",["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings",["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

with st.form("Login Form"):
    username = st.text_input("Username")
    password = st.text_input("Password",type="password")
    submitted = st.form_submit_button("Login")

    if submitted :
        st.success(f"Welcome, {username}")
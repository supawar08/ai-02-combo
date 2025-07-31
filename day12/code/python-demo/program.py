import streamlit as st
import pickle

# load the model
with open("hearing_test_model.pkl", "rb") as file:
    model = pickle.load(file)

# set the title
# st.title("Hearing Test Classification")

# set the header
st.header("Hearing Test Classification")

# set the subheader
# st.subheader("Predict if a patient will suffer with hearing disability by using age and physical score")

st.text("Predict if a patient will suffer with hearing disability by using age and physical score")

# get the input from user
age = st.text_input("Age")
physical_score = st.text_input("Physical Score")

# add a button to predict the result
button = st.button("Predict")

# check if the button is pressed
if button:
    print(f"age: {age}, type = {type(age)}")
    print(f"physical score: {physical_score}, type = {type(physical_score)}")

    # predict the result using model
    result = model.predict([[int(age), int(physical_score)]])
    
    # print success or error
    if result[0] == 1:
        st.success("The result is positive")
    elif result[0] == 0:
        st.error("The result is negative")



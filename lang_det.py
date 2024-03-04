import pickle
import streamlit as st

pickle_file_path = "svc98.pkl"

with open(pickle_file_path, "rb") as pickle_file:
        Lrdetect_Model = pickle.load(pickle_file)


st.title("Language Detection Tool")
input_test = st.text_input("Enter Your Text Here")

button_clicked = st.button("Get Language Name")
res = ''
if button_clicked:
	res = Lrdetect_Model.predict([input_test])[0]
st.write("# ", res)

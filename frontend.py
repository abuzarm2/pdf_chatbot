import streamlit as st
import requests

st.title("QnA on PDF Document📝")
uploaded_file = st.file_uploader("Upload a PDF file", type=("pdf"))

if uploaded_file:
    # Send the uploaded file to the backend
    # files = {'file': uploaded_file.getvalue()}
    # response = requests.post("http://localhost:5001/docprocess", files=files)
    files = {'file': (uploaded_file.name,
                      uploaded_file.getvalue(), uploaded_file.type)}
    response = requests.post("http://localhost:5001/docprocess", files=files)

    if response.status_code == 200:
        st.write(response.json().get("message"))
    else:
        st.write(f"Failed to process document: {response.status_code}")

question = st.text_input(
    "Ask something about the document",
    placeholder="Can you give me a insurance plan?",
)

if question:
    # TODO: Call the QnA API to get the answer
    res = requests.post("http://localhost:5000/qna",
                        json={"question": question})
    st.write("### Question:")
    st.write(question)

    st.write("### Answer:")
    st.write(res.json().get("Answer"))

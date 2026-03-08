import streamlit as st
from agent import run_file_organizer_agent

st.title("📂 AI File Organizer Agent")
st.write("Automatically organize files in your folder")

folder_path = st.text_input("Enter Folder Path")

if st.button("Run Agent"):
    if folder_path:
        result = run_file_organizer_agent(folder_path)
        st.write(result)
    else:
        st.warning("Please enter a folder path")
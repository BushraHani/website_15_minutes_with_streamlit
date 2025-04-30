import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Students Data Generator", layout="wide")
st.title("Student CVS File Generator")

name = ["Ali", "Aisha", "Ahmed", "Fatima", "Osman", "Zainab","Bilal", "Hina","Sami","Nadia",]

students = []

for i in range (1,16):
    student = {
        "ID": i,
        "Name": random.choice(name),
        "Age": random.randint(18,25),
        "Grade": random.choice(["A","B","C","D","E","F",])
    }   
    students.append(student)
    
df = pd.DataFrame(students)
st.subheader("Generated Students Data")
st.dataframe(df) 

csv_file = df.to_csv(index=False).encode('utf-8')  
st.download_button("Download CSV File",csv_file,"students.csv", "text/csv")
st.success("Students Record Generated Sucessfully!")

# app.py
import streamlit as st
import pandas as pd

def load_data():
    # Load data from Excel file
    excel_path = "datasets/driver_world_standings.xlsx"  
    df = pd.read_excel(excel_path)
    return df

def main():
    # Title
    st.title("Driver Standings")

    # Load data from Excel
    df = load_data()

    for index, row in df.iterrows():


        col1, col2 = st.columns([4,1])

        # Display text and images for the first row
        col1.header(f"{row['Championship Standing']}. {row['Driver']}")
        col1.markdown(" ")
        col1.markdown(f"<p style='font-size: 22px;'>{row['Points']} PTS</p>", unsafe_allow_html=True)
        col1.markdown(" ")
        col1.markdown(" ")
        col1.markdown(f"<p style='font-size: 22px;'>{row['Car']}</p>", unsafe_allow_html=True)

        col2.markdown(" ")
        col2.markdown(" ")
        col2.markdown(" ")
        col2.image(row['Image Filename'], width=130)
        col2.image(row['Number Filename'], width=70)
        col2.markdown(" ")
        col2.markdown(" ")




        


if __name__ == "__main__":
    main()

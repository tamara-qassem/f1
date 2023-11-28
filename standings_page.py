# app.py
import streamlit as st
import pandas as pd
import os

def load_data():
    # Load data from Excel file
    excel_path = "datasets/driver_world_standings.xlsx"  
    df = pd.read_excel(excel_path)
    return df

def main():
    # Title
    st.title("Driver Standings and Images")

    # Load data from Excel
    df = load_data()

    # Iterate through rows, displaying two items per row
    for index, row in df.iterrows():
        # Create a container with a light blue background using st.markdown
        st.markdown(
            f"""
            <div style="background-color: #e6f7ff; padding: 15px; border-radius: 10px; margin-bottom: 15px;">
                <h2>{row['Championship Standing']}. {row['Driver']}</h2>
                <div style="display: flex; justify-content: space-between; margin-top: 10px;">
                    <div style="flex: 1;">
                        <p>{row['Points']} PTS</p>
                        <p>{row['Car']}</p>
                    </div>
                    <div style="flex: 1;">
                        <img src="data:image/png;base64,{row['Image Filename']}"  width="150">
                        <img src="data:image/png;base64,{row['Number Filename']}" width="70">
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()

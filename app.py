import streamlit as st
import pandas as pd
from datetime import date
st.set_page_config(page_title="RWC Generator", layout="wide")
st.title("Re-Warehousing Certificate Generator")
upload=st.file_uploader("Upload Excel", type=["xlsx"])
if upload:
    df=pd.read_excel(upload)
    st.dataframe(df)
    fno=st.text_input("File No","S25/19/2013 PT VII-ACC.Cus")
    letter_date=st.date_input("Letter Date", date.today())
    if st.button("Generate Report"):
        html=(f"<h2>OFFICE OF THE DEPUTY COMMISSIONER OF CUSTOMS</h2><p><b>F.No.</b> {fno} Date: {letter_date}</p><p>Sub: Re-Warehousing Certificate</p>")
        html+=df.to_html(index=False)
        st.components.v1.html(html,height=600,scrolling=True)
        st.download_button("Download HTML",html,"report.html")

import streamlit as st
import pandas as pd

from modules.database import load_assessments

st.set_page_config(
    page_title="Assessment History",
    layout="wide"
)

st.title("Assessment History")

rows = load_assessments()

if len(rows) == 0:

    st.info("No assessments available.")

else:

    df = pd.DataFrame(

        rows,

        columns=[
            "ID",
            "Organization",
            "Department",
            "AI System",
            "Owner",
            "Industry",
            "AI Type",
            "Deployment",
            "Criticality",
            "Governance Score",
            "Risk",
            "Assessment Date"
        ]

    )

    st.dataframe(df, use_container_width=True)
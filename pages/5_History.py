import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Assessment History",
    page_icon="📁",
    layout="wide"
)

st.title("Assessment History")

# --------------------------------------------------------
# CONNECT TO DATABASE
# --------------------------------------------------------

conn = sqlite3.connect("raigap.db")
cursor = conn.cursor()

# --------------------------------------------------------
# LOAD DATA
# --------------------------------------------------------

try:
    query = """
    SELECT
        id,
        organization,
        department,
        ai_system,
        owner,
        industry,
        overall_score,
        risk,
        assessment_date
    FROM assessments
    ORDER BY assessment_date DESC
    """

    df = pd.read_sql_query(query, conn)

except Exception:

    df = pd.DataFrame()

# --------------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------------

if df.empty:

    st.info("No assessments have been saved yet.")

else:

    st.subheader("Saved Assessments")

    search = st.text_input("Search by Organization")

    if search:

        df = df[
            df["organization"]
            .str.contains(search, case=False, na=False)
        ]

    risk_filter = st.selectbox(
        "Filter by Risk",
        ["All", "Low Risk", "Medium Risk", "High Risk"]
    )

    if risk_filter != "All":

        df = df[df["risk"] == risk_filter]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download CSV",
        csv,
        "Assessment_History.csv",
        "text/csv"
    )

conn.close()
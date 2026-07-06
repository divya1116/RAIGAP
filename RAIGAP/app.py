import streamlit as st
from modules.database import create_tables
def load_css():

    with open("assets/style.css") as f:

        st.markdown(

            f"<style>{f.read()}</style>",

            unsafe_allow_html=True

        )

load_css()
create_tables()

st.set_page_config(
    page_title="RAIGAP",
    page_icon="🛡️",
    layout="wide"
)

# ---------- Sidebar ----------
st.sidebar.title("🛡️ RAIGAP")
st.sidebar.markdown("### Responsible AI Governance")
st.sidebar.info(
    "Evaluate AI systems against Responsible AI principles and governance requirements."
)

st.sidebar.markdown("---")
st.sidebar.success("Version 1.0")
st.sidebar.caption("Developed as an AI Governance Decision Support System")

# ---------- Header ----------
st.title("Responsible AI Governance & Regulatory Impact Assessment Platform")

st.markdown("""
This platform helps organizations evaluate AI systems using
globally accepted Responsible AI and AI Governance principles.

The system supports governance assessment, compliance readiness,
risk analysis, automated reporting, and decision support.
""")

st.divider()

# ---------- KPI Cards ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Governance Dimensions", "8")

with col2:
    st.metric("Assessment Questions", "40")

with col3:
    st.metric("Risk Levels", "3")

with col4:
    st.metric("Frameworks", "6")

st.divider()

# ---------- Features ----------
st.subheader("Core Features")

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
### Governance Assessment

- AI Governance Evaluation
- Responsible AI Assessment
- Governance Scoring
- Compliance Readiness
""")

with c2:
    st.markdown("""
### Analytics & Reporting

- Governance Dashboard
- Risk Classification
- PDF Reports
- Historical Assessments
""")

st.divider()

st.success("Database initialized successfully.")

st.info(
    "Select **New Assessment** from the left sidebar to begin evaluating an AI system."
)

st.markdown("---")

st.caption(
    "RAIGAP | Responsible AI Governance & Regulatory Impact Assessment Platform | Version 1.0"
)
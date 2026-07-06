import streamlit as st

from modules.scoring import (
    calculate_overall_score,
    classify_risk,
)

from modules.database import save_assessment
from modules.report_generator import generate_report


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Final Assessment",
    page_icon="📄",
    layout="wide"
)

st.title("AI Governance Final Assessment")


# --------------------------------------------------
# CHECK ASSESSMENT DATA
# --------------------------------------------------

if "dimension_scores" not in st.session_state:
    st.warning("No assessment found. Please complete a governance assessment first.")
    st.stop()

scores = st.session_state.dimension_scores

if not scores:
    st.warning("Please complete at least one governance dimension.")
    st.stop()


# --------------------------------------------------
# CALCULATE SCORE
# --------------------------------------------------

overall = calculate_overall_score(scores)
risk = classify_risk(overall)


# --------------------------------------------------
# DISPLAY METRICS
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.metric("Overall AI Governance Index", f"{overall}%")

with col2:
    st.metric("Overall Risk Classification", risk)


# --------------------------------------------------
# GET BASIC INFORMATION
# --------------------------------------------------

organization = st.session_state.get("organization", "")
department = st.session_state.get("department", "")
ai_system = st.session_state.get("ai_system", "")
owner = st.session_state.get("owner", "")
industry = st.session_state.get("industry", "")
ai_type = st.session_state.get("ai_type", "")
deployment = st.session_state.get("deployment", "")
criticality = st.session_state.get("criticality", "")


# --------------------------------------------------
# ORGANIZATION DETAILS
# --------------------------------------------------

st.divider()

st.subheader("Assessment Information")

st.write(f"**Organization:** {organization}")
st.write(f"**Department:** {department}")
st.write(f"**AI System:** {ai_system}")
st.write(f"**Project Owner:** {owner}")
st.write(f"**Industry:** {industry}")
st.write(f"**AI Type:** {ai_type}")
st.write(f"**Deployment:** {deployment}")
st.write(f"**Business Criticality:** {criticality}")


# --------------------------------------------------
# ACTION BUTTONS
# --------------------------------------------------

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button("Save Assessment", use_container_width=True):

        save_assessment(
            organization,
            department,
            ai_system,
            owner,
            industry,
            ai_type,
            deployment,
            criticality,
            overall,
            risk
        )

        st.success("Assessment saved successfully.")


with col2:

    if st.button("Generate PDF Report", use_container_width=True):

        filename = "reports/RAIGAP_Report.pdf"

        generate_report(
            filename,
            organization,
            ai_system,
            overall,
            risk,
            scores
        )

        st.success("PDF report generated successfully.")

        with open(filename, "rb") as pdf_file:

            st.download_button(
                "Download PDF Report",
                pdf_file,
                file_name="RAIGAP_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )


# --------------------------------------------------
# DIMENSION SCORES
# --------------------------------------------------

st.divider()

st.subheader("Dimension-wise Governance Scores")

for dimension, score in scores.items():

    st.write(f"### {dimension}")

    st.progress(score / 100)

    st.write(f"Score: **{score}%**")


# --------------------------------------------------
# EXECUTIVE SUMMARY
# --------------------------------------------------

st.divider()

st.subheader("Executive Summary")

if overall >= 85:

    st.success(
        "The AI system demonstrates a high level of governance maturity with strong governance controls."
    )

elif overall >= 60:

    st.warning(
        "The AI system demonstrates moderate governance maturity. Some governance controls should be strengthened."
    )

else:

    st.error(
        "The AI system demonstrates low governance maturity. Significant improvements are recommended before production deployment."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "RAIGAP | Responsible AI Governance & Regulatory Impact Assessment Platform | Version 1.0"
)
from modules.action_plan import generate_action_plan

st.divider()

st.subheader("Governance Action Plan")

plan = generate_action_plan(scores)

if len(plan)==0:

    st.success("No corrective actions required.")

else:

    st.table(plan)
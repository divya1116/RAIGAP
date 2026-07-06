import streamlit as st

st.set_page_config(
    page_title="New Assessment",
    page_icon="📋",
    layout="wide"
)

st.title("New AI Governance Assessment")

st.write(
    "Provide the details of the AI system before starting the governance assessment."
)

st.markdown("---")

with st.form("assessment_form"):

    col1, col2 = st.columns(2)

    with col1:
        organization = st.text_input("Organization Name")
        department = st.text_input("Department")
        ai_system = st.text_input("AI System Name")
        owner = st.text_input("Project Owner")

    with col2:
        industry = st.selectbox(
            "Industry",
            [
                "Banking",
                "Financial Services",
                "Insurance",
                "Healthcare",
                "Government",
                "Retail",
                "Manufacturing",
                "Other",
            ],
        )

        ai_type = st.selectbox(
            "AI System Type",
            [
                "Machine Learning",
                "Generative AI",
                "NLP",
                "Computer Vision",
                "Decision Support",
                "Recommendation System",
            ],
        )

        deployment = st.selectbox(
            "Deployment Environment",
            [
                "Cloud",
                "On-Premise",
                "Hybrid",
            ],
        )

        criticality = st.selectbox(
            "Business Criticality",
            [
                "Low",
                "Medium",
                "High",
            ],
        )

    description = st.text_area(
        "Brief Description of the AI System",
        height=120,
    )

    submitted = st.form_submit_button("Proceed to Governance Assessment")

if submitted:
    st.session_state.organization = organization
    st.session_state.department = department
    st.session_state.ai_system = ai_system
    st.session_state.owner = owner
    st.session_state.industry = industry
    st.session_state.ai_type = ai_type
    st.session_state.deployment = deployment
    st.session_state.criticality = criticality
    st.success("Basic information captured successfully.")

    st.write("### Assessment Summary")

    st.write(f"**Organization:** {organization}")
    st.write(f"**Department:** {department}")
    st.write(f"**AI System:** {ai_system}")
    st.write(f"**Project Owner:** {owner}")
    st.write(f"**Industry:** {industry}")
    st.write(f"**AI Type:** {ai_type}")
    st.write(f"**Deployment:** {deployment}")
    st.write(f"**Business Criticality:** {criticality}")
    st.write(f"**Description:** {description}")
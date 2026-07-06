import streamlit as st
from modules.questionnaire import load_questions
from modules.scoring import calculate_dimension_score, classify_risk
from data.dimensions import DIMENSIONS

st.set_page_config(
    page_title="Governance Assessment",
    page_icon="🛡️",
    layout="wide"
)

st.title("AI Governance Assessment")
if "dimension_scores" not in st.session_state:
    st.session_state.dimension_scores = {}

dimension = st.selectbox(
    "Select Governance Dimension",
    list(DIMENSIONS.keys())
)

df = load_questions(DIMENSIONS[dimension])

responses = []

st.divider()

for i, row in df.iterrows():

    score = st.radio(
        row["Question"],
        [1,2,3,4,5],
        format_func=lambda x:
        [
            "",
            "1 - Not Implemented",
            "2 - Initial",
            "3 - Partially Implemented",
            "4 - Mostly Implemented",
            "5 - Fully Implemented"
        ][x],
        key=f"{dimension}_{i}"
    )

    responses.append(score)

st.divider()

if st.button("Save Dimension Score"):

    score = calculate_dimension_score(responses)

    st.session_state.dimension_scores[dimension] = score

    risk = classify_risk(score)

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Dimension Score", f"{score}%")

    with c2:
        st.metric("Risk", risk)

    st.success(f"{dimension} score saved successfully.")
    st.subheader("Debug Session State")
    st.json(st.session_state.dimension_scores)
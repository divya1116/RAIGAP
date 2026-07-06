import streamlit as st

from modules.scoring import (
    calculate_overall_score,
    classify_risk,
)

from modules.charts import (
    bar_chart,
    radar_chart,
)

from modules.recommendation import generate_recommendations


# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("Executive AI Governance Dashboard")


# ----------------------------------------------------
# CHECK SESSION
# ----------------------------------------------------

if "dimension_scores" not in st.session_state:

    st.warning("Please complete at least one governance assessment.")

    st.stop()

scores = st.session_state.dimension_scores

if len(scores) == 0:

    st.warning("Please complete at least one governance assessment.")

    st.stop()


# ----------------------------------------------------
# CALCULATE METRICS
# ----------------------------------------------------

overall = calculate_overall_score(scores)

risk = classify_risk(overall)

completed = len(scores)

compliance = (
    "Compliant"
    if overall >= 75
    else "Needs Improvement"
)


# ----------------------------------------------------
# KPI CARDS
# ----------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Governance Index", f"{overall}%")

with col2:
    st.metric("Risk Level", risk)

with col3:
    st.metric("Dimensions Completed", f"{completed}/8")

with col4:
    st.metric("Compliance", compliance)


# ----------------------------------------------------
# BAR CHART
# ----------------------------------------------------

st.divider()

st.subheader("Governance Dimension Scores")

fig = bar_chart(scores)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ----------------------------------------------------
# RADAR CHART
# ----------------------------------------------------

st.divider()

st.subheader("Governance Maturity Radar")

fig = radar_chart(scores)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ----------------------------------------------------
# DIMENSION DETAILS
# ----------------------------------------------------

st.divider()

st.subheader("Dimension Details")

for dimension, score in scores.items():

    st.write(f"### {dimension}")

    st.progress(score / 100)

    st.write(f"**Score:** {score:.2f}%")

    st.write("")


# ----------------------------------------------------
# AI RECOMMENDATIONS
# ----------------------------------------------------

st.divider()

st.subheader("AI Governance Recommendations")

recommendations = generate_recommendations(scores)

for recommendation in recommendations:

    st.info(recommendation)
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def bar_chart(scores):
    """
    Generate a horizontal bar chart of governance scores.
    """

    if not scores:
        return go.Figure()

    df = pd.DataFrame({
        "Dimension": list(scores.keys()),
        "Score": list(scores.values())
    })

    fig = px.bar(
        df,
        x="Score",
        y="Dimension",
        orientation="h",
        text="Score",
        color="Score",
        color_continuous_scale="Blues"
    )

    fig.update_traces(
        texttemplate="%{text:.0f}%",
        textposition="outside"
    )

    fig.update_layout(
        title="Governance Dimension Scores",
        xaxis_title="Score (%)",
        yaxis_title="",
        xaxis=dict(range=[0, 100]),
        height=500,
        coloraxis_showscale=False,
        template="plotly_white",
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig


def radar_chart(scores):
    """
    Generate a radar chart for governance maturity.
    """

    if not scores:
        return go.Figure()

    categories = list(scores.keys())
    values = list(scores.values())

    # Close the radar chart
    categories.append(categories[0])
    values.append(values[0])

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            name="Governance Score",
            line=dict(width=3)
        )
    )

    fig.update_layout(
        title="Governance Maturity Radar",
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        template="plotly_white",
        height=600,
        margin=dict(l=40, r=40, t=60, b=40)
    )

    return fig
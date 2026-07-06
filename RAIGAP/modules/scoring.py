# modules/scoring.py

DIMENSION_WEIGHTS = {
    "Privacy & Data Protection": 15,
    "Fairness & Bias": 15,
    "Transparency & Explainability": 15,
    "Security": 15,
    "Accountability": 10,
    "Human Oversight": 10,
    "Robustness & Reliability": 10,
    "Regulatory Compliance": 10,
}


def calculate_dimension_score(scores):
    maximum = len(scores) * 5
    obtained = sum(scores)

    return round((obtained / maximum) * 100, 2)


def calculate_overall_score(all_scores):
    """
    Calculates the average score of completed dimensions.
    This is used during assessment before all 8 dimensions are finished.
    """

    if len(all_scores) == 0:
        return 0

    return round(sum(all_scores.values()) / len(all_scores), 2)


def classify_risk(score):

    if score >= 85:
        return "Low Risk"

    elif score >= 60:
        return "Medium Risk"

    return "High Risk"
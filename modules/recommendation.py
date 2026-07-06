def generate_recommendations(scores):

    recommendations = []

    for dimension, score in scores.items():

        if score < 60:

            recommendations.append(
                f"{dimension}: Immediate improvement is recommended."
            )

        elif score < 80:

            recommendations.append(
                f"{dimension}: Governance controls should be strengthened."
            )

    if len(recommendations) == 0:

        recommendations.append(
            "Excellent governance maturity. Continue continuous monitoring and periodic audits."
        )

    return recommendations
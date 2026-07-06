def generate_action_plan(scores):

    plan = []

    for dimension, score in scores.items():

        if score >= 80:
            continue

        if score < 40:

            priority = "High"

            timeline = "30 Days"

        elif score < 60:

            priority = "Medium"

            timeline = "60 Days"

        else:

            priority = "Low"

            timeline = "90 Days"

        plan.append({

            "Dimension": dimension,

            "Score": score,

            "Priority": priority,

            "Timeline": timeline,

            "Recommendation":
                f"Strengthen governance controls for {dimension}."

        })

    return plan
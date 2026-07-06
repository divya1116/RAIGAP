from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch


def generate_report(
    filename,
    organization,
    ai_system,
    overall_score,
    risk,
    scores,
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    title_style.alignment = TA_CENTER

    heading = styles["Heading2"]

    normal = styles["BodyText"]

    story = []

    # ---------------------------------------------------
    # Cover
    # ---------------------------------------------------

    story.append(Paragraph(
        "Responsible AI Governance & Regulatory Impact Assessment Platform",
        title_style
    ))

    story.append(Spacer(1, 0.3 * inch))

    story.append(
        Paragraph("<b>Governance Assessment Report</b>", heading)
    )

    story.append(Spacer(1, 0.2 * inch))

    story.append(
        Paragraph(f"<b>Organization:</b> {organization}", normal)
    )

    story.append(
        Paragraph(f"<b>AI System:</b> {ai_system}", normal)
    )

    story.append(Spacer(1, 0.3 * inch))

    # ---------------------------------------------------
    # Executive Summary
    # ---------------------------------------------------

    story.append(
        Paragraph("Executive Summary", heading)
    )

    story.append(
        Paragraph(
            f"The assessed AI system achieved an overall governance "
            f"score of <b>{overall_score}%</b>, resulting in an "
            f"<b>{risk}</b> classification.",
            normal,
        )
    )

    story.append(Spacer(1, 0.2 * inch))

    # ---------------------------------------------------
    # Score Table
    # ---------------------------------------------------

    story.append(
        Paragraph("Governance Dimension Scores", heading)
    )

    data = [["Dimension", "Score"]]

    for dimension, score in scores.items():

        data.append([dimension, f"{score}%"])

    table = Table(data, colWidths=[4.5 * inch, 1.5 * inch])

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("GRID", (0,0), (-1,-1), 1, colors.grey),
            ("BACKGROUND", (0,1), (-1,-1), colors.whitesmoke),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0,0), (-1,0), 10),
        ])
    )

    story.append(table)

    story.append(Spacer(1, 0.3 * inch))

    # ---------------------------------------------------
    # Recommendations
    # ---------------------------------------------------

    story.append(
        Paragraph("Recommendations", heading)
    )

    for dimension, score in scores.items():

        if score < 60:

            story.append(
                Paragraph(
                    f"• Strengthen governance controls for <b>{dimension}</b>.",
                    normal,
                )
            )

    doc.build(story)
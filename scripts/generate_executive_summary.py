#!/usr/bin/env python3
"""
Generate a 1-page executive summary PDF for decision-makers.
Targets stakeholders who need quick, actionable insights.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfgen import canvas
from datetime import datetime
import os

# Color scheme matching the website
ACCENT_COLOR = HexColor('#0a3d62')
ACCENT_MUTED = HexColor('#1f5b89')
TEXT_ACCENT = HexColor('#ff6b35')
TEXT_PRIMARY = HexColor('#212529')
TEXT_SECONDARY = HexColor('#495057')
BG_PRIMARY = HexColor('#f8f9fa')

def create_executive_summary(output_path='assets/docs/executive_summary.pdf'):
    """Generate a professional 1-page executive summary PDF."""
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=0.65*inch,
        leftMargin=0.65*inch,
        topMargin=0.4*inch,
        bottomMargin=0.4*inch
    )
    
    # Container for the 'Flowable' objects
    story = []
    
    # Define custom styles
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=ACCENT_COLOR,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Subtitle style
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=TEXT_SECONDARY,
        spaceAfter=18,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    # Section header style
    section_style = ParagraphStyle(
        'CustomSection',
        parent=styles['Heading2'],
        fontSize=11,
        textColor=ACCENT_COLOR,
        spaceAfter=6,
        spaceBefore=10,
        fontName='Helvetica-Bold',
        leftIndent=0
    )
    
    # Key metric style
    metric_style = ParagraphStyle(
        'CustomMetric',
        parent=styles['Normal'],
        fontSize=10,
        textColor=TEXT_PRIMARY,
        spaceAfter=6,
        fontName='Helvetica-Bold',
        leftIndent=0
    )
    
    # Body text style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=9,
        textColor=TEXT_PRIMARY,
        spaceAfter=6,
        leading=11,
        leftIndent=0
    )
    
    # Bullet style
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=8.5,
        textColor=TEXT_PRIMARY,
        spaceAfter=4,
        leading=10,
        leftIndent=12,
        bulletIndent=6
    )
    
    # Executive Summary Title
    story.append(Paragraph("EXECUTIVE SUMMARY", title_style))
    story.append(Paragraph("English-Spanish Cognate Analysis", subtitle_style))
    story.append(Spacer(1, 0.12*inch))
    
    # Key Metrics Box - Use Paragraph objects to process HTML tags
    metric_bold_style = ParagraphStyle(
        'MetricBold',
        parent=styles['Normal'],
        fontSize=11,
        textColor=TEXT_PRIMARY,
        fontName='Helvetica-Bold',
        leading=12
    )
    metric_normal_style = ParagraphStyle(
        'MetricNormal',
        parent=styles['Normal'],
        fontSize=9,
        textColor=TEXT_PRIMARY,
        fontName='Helvetica',
        leading=11
    )
    
    metrics_data = [
        [Paragraph('<b>86.8%</b>', metric_bold_style), Paragraph('True Cognates', metric_normal_style), 
         Paragraph('<b>7.4%</b>', metric_bold_style), Paragraph('False Friends', metric_normal_style)],
        [Paragraph('<b>1 in 13</b>', metric_bold_style), Paragraph('Similar words trick learners', metric_normal_style), 
         Paragraph('<b>2.95</b>', metric_bold_style), Paragraph('Mean frequency (false friends)', metric_normal_style)],
        [Paragraph('<b>20.0%</b>', metric_bold_style), Paragraph('FFR: Family/Kinship', metric_normal_style), 
         Paragraph('<b>3.69%</b>', metric_bold_style), Paragraph('FFR: Technology/Tools', metric_normal_style)],
    ]
    
    metrics_table = Table(metrics_data, colWidths=[1.2*inch, 2.1*inch, 1.2*inch, 2.1*inch])
    metrics_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), white),
        ('TEXTCOLOR', (0, 0), (-1, -1), TEXT_PRIMARY),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(metrics_table)
    story.append(Spacer(1, 0.1*inch))
    
    # Core Findings
    story.append(Paragraph("CORE FINDINGS", section_style))
    
    findings = [
        "<b>1. The False Friends Paradox:</b> High-frequency false friends (mean frequency 2.95 vs. true cognates) appear early in learning, creating outsized confusion. Abstract domains (Emotions: 13.33%, Family: 20.00% FFR) pose highest risk.",
        "<b>2. Strategic Loanword Patterns:</b> English→Spanish loans (frequency 2.84) dominate modern tech vocabulary—essential for contemporary communication. Spanish→English loans (frequency 3.76) are cultural specialties.",
        "<b>3. Complexity ≠ Similarity:</b> Levenshtein similarity shows near-zero correlation with complexity (r=0.008). Word length and syllables predict complexity (r≥0.76). Health/Medicine domains trend most complex.",
        "<b>4. Historical Patterns:</b> 55.3% of false friends emerged before 1400; only 5.3% in modern times. Ancient false friends remain the primary learning challenge.",
    ]
    
    for finding in findings:
        story.append(Paragraph(finding, body_style))
        story.append(Spacer(1, 0.06*inch))
    
    story.append(Spacer(1, 0.08*inch))
    
    # Strategic Recommendations
    story.append(Paragraph("STRATEGIC RECOMMENDATIONS", section_style))
    
    recommendations = [
        "<b>Curriculum Design:</b> Flag high-frequency false friends (<i>actual</i>, <i>embarazada</i>, <i>sensible</i>) with explicit warnings in early-stage instruction. Sequence safe domains (Technology) before high-risk domains (Family, Emotions).",
        "<b>Resource Allocation:</b> Prioritize false friend instruction in Family/Kinship and Emotions/Psychology domains where FFR exceeds 13%. Leverage 86.8% true cognate foundation for rapid vocabulary expansion.",
        "<b>Application Development:</b> Adaptive systems should prioritize false friend practice based on frequency data. Error prediction models benefit from domain-specific FFR rates. Personalize learning paths by complexity metrics (length, syllables) rather than similarity.",
    ]
    
    for rec in recommendations:
        story.append(Paragraph(rec, body_style))
        story.append(Spacer(1, 0.06*inch))
    
    story.append(Spacer(1, 0.08*inch))
    
    # Bottom footer with date
    footer_text = f"Generated: {datetime.now().strftime('%B %Y')} | Full report available at findings.html"
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=7,
        textColor=TEXT_SECONDARY,
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )
    story.append(Paragraph(footer_text, footer_style))
    
    # Build PDF
    doc.build(story)
    print(f"Executive summary PDF generated: {output_path}")
    return output_path

if __name__ == '__main__':
    create_executive_summary()


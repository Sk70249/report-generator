from reportlab.pdfgen import canvas
def generate_pdf(text):
    c=canvas.Canvas("report.pdf")
    c.drawString(0,830,text)
    c.save()

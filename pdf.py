from reportlab.pdfgen import canvas
c=canvas.Canvas("report.pdf")
def generate_pdf(text):
    c.drawString(0,800,text)
    c.save()
def edit_text(color,size,font_name):
    c.setFillColor(color)
    c.setFont(font_name, size, leading = None)


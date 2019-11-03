def genpdf(x):
    from reportlab.pdfgen import canvas
    c=canvas.Canvas("report.pdf")
    c.drawString(0,830,x)
    c.save()

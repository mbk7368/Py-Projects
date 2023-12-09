from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

report = SimpleDocTemplate("C:\\Users\\mbk73\\Desktop\\mypdffile.pdf")
styles = getSampleStyleSheet()

reporttitle = paragraph("A Complete Inventory of my fruit", styles["h1"])

fruit={"elderberries":1,"figs":1,"apples":2,"durians":3,"bananas":5,"cherries":8,"grapes":13}

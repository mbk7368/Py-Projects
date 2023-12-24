from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.units import inch
import os

report = SimpleDocTemplate("C:\\Users\\mbk73\\Desktop\\mypdffile.pdf")
styles = getSampleStyleSheet()

reporttitle = Paragraph("A Complete Inventory of my fruit", styles["h1"])

fruit={"elderberries":1,"figs":1,"apples":2,"durians":3,"bananas":5,"cherries":8,"grapes":13}
table_data = []
for k, v in fruit.items():
    table_data.append([k,v])
tablestyle = [("GRID",(0,0),(-1,-1), 1,colors.black)]
reportTable = Table(data=table_data, style=tablestyle, hAlign="LEFT")
reportpie = Pie(width=3*inch, height=3*inch)
reportpie.data = []
reportpie.labels = []
for fruitname in sorted(fruit):
    reportpie.data.append(fruit[fruitname])
    reportpie.labels.append(fruitname)
reportchart = Drawing()
reportchart.add(reportpie)

report.build([reporttitle, reportTable, reportchart])
os.startfile("C:\\Users\\mbk73\\Desktop\\mypdffile.pdf")
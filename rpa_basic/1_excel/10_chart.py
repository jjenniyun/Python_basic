from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# 차트 만들기
from openpyxl.chart import BarChart, Reference

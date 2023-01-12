from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("img.png")

# C3위치에 IMG.PNG파일의 이미지 삽입
# ws.add_image(img, "C3")

# wb.save("sample_image.xlsx")
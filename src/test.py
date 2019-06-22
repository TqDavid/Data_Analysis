import cv2
import numpy as np
import os

from openpyxl import load_workbook
from openpyxl import Workbook

# im = cv2.imdecode(
#     np.fromfile(r"C:\Users\柳博\Downloads\space-tech-remote-sensing-ob-detection-dataset\val\images\P5789.png",
#                 dtype=np.uint8), cv2.IMREAD_COLOR)
#
# print(im.shape)

# print(os.getcwd())

execlname = "play.xlsx"
if os.path.exists(os.path.join(os.getcwd(), execlname)):
   wb = load_workbook(execlname)
   if "total" in wb.sheetnames:
       ws = wb.get_sheet_by_name("total")
   else:
       ws = wb.create_sheet("total")
else:
    wb = Workbook()
    ws = wb.active
    ws.title = "total"

ws["A1"] = "hello"
wb.save(execlname)



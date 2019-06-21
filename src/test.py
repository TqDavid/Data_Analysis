import cv2
import numpy as np

im = cv2.imdecode(
    np.fromfile(r"C:\Users\柳博\Downloads\space-tech-remote-sensing-ob-detection-dataset\val\images\P5789.png",
                dtype=np.uint8), cv2.IMREAD_COLOR)

print(im.shape)

import os

data_root = r"C:\Users\柳博\Downloads\space-tech-remote-sensing-ob-detection-dataset"

train_image = os.path.join(data_root, "train", "images")
train_labelTxt = os.path.join(data_root, "train", "labelTxt")
val_image = os.path.join(data_root, "val", "images")
val_labelTxt = os.path.join(data_root, "val", "labelTxt")
test_image = os.path.join(data_root, "test", "images")

small_data_root = r"C:\Users\柳博\Downloads\space-tech-remote-sensing-ob-detection-dataset\GoogleEarthSmallDataset"
small_train_image = os.path.join(small_data_root, "train", "images")
small_train_labelTxt = os.path.join(small_data_root, "train", "labelTxt")
small_val_image = os.path.join(small_data_root, "val", "images")
small_val_labelTxt = os.path.join(small_data_root, "val", "labelTxt")


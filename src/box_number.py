import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd
import json
import cfg

# 文件数量
train_image = os.listdir(cfg.train_image)
train_labelTxt = os.listdir(cfg.train_labelTxt)
val_image = os.listdir(cfg.val_image)
val_labelTxt = os.listdir(cfg.val_labelTxt)
test_image = os.listdir(cfg.test_image)

#
class2id = dict()
with open("18class.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        strs = line.split(" ")
        class_name = strs[1]
        class_id = int(strs[2])
        class2id[class_name] = class_id

print(class2id)

train_class2count = dict()

for key, value in class2id.items():
    train_class2count[key] = 0

train_difficult2count = dict()
train_difficult2count[0] = 0
train_difficult2count[1] = 1

# 来源
train_imagesource2count = dict()

for label_file_name in train_labelTxt:
    try:
        with open(os.path.join(cfg.train_labelTxt, label_file_name), encoding="utf-8") as f:
            lines = f.readlines()
            imagesource = lines[0].split(":")[1]
            if imagesource not in train_imagesource2count.keys():
                train_imagesource2count[imagesource] = 1
            else:
                train_imagesource2count[imagesource] += 1
            for line in lines[4:]:
                line = line.strip()
                if len(line) == 0:
                    continue
                strs = line.split(" ")
                class_name = strs[-2]
                difficult = int(strs[-1])
                if class_name in train_class2count.keys():
                    train_class2count[class_name] += 1
                else:
                    print(label_file_name, line)
                if difficult == 0 or difficult == 1:
                    train_difficult2count[difficult] += 1
    except BaseException:
        print(label_file_name)

print(train_class2count)
print(train_difficult2count)
print(train_imagesource2count)

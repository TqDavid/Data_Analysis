# 竞赛标准 （从官网复制）
[官网](http://rscup.bjxintong.com.cn/#/theme/2)

比赛初赛算法评价主要采用平均精度均值 (mAP) 指标。 首先计算预测目标窗口和真实标记窗口的交并比IoU (Intersection-over-Union)， 若交并比大于0.5则预测正确。然后计算不同类别目标检测的平均精度 (AP)， 最后对所有目标类别的平均精度进行均值计算，即为平均精度均值。mAP值越高，模型对各类别目标检测的性能越好，排名越靠前。 比赛决赛成绩将基于算法模型精度、效率、规模等指标加权，对算法模型性能进行综合评估与排名。

# DOTA(A Large-scale Dataset for Object Detection in Aerial Images)
[原链接](http://captain.whu.edu.cn/dotaweb/tasks.html)
## Task 1 Detection with oriented bounding boxes (Recommended)
The evaluation protocol for oriented bounding box is a little different from the protocol in the original PASCAL VOC. We use the intersection over the union area of two polygons(ground truth and prediction) to calculate the IoU. The rest follows the PASCAL VOC.

面向边界框的评估协议与原PASCAL VOC中的评估协议有一定的不同。我们使用两个多边形联合面积上的交点(地面真值和预测)来计算IoU,其余部分遵循PASCAL VOC。
## Task 2 Detection with horizontal bounding boxes
The evaluation protocol for horizontal bounding boxes follows the PASCAL VOC benchmark, which uses mean Average Precision(mAP) as the primary metric.
水平边界框的评估协议遵循PASCAL VOC基准，该基准使用平均精度(mAP)作为主要度量。
import cv2 as cv
import numpy as np
"""
图像轮廓特征查找：外接矩形、最小外接矩形、最小外接圆
"""
# 读图及预处理
img = cv.imread("../images/tu.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# 查找轮廓
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# 遍历绘制
for cnt in contours:
    # 外接矩形
    x, y, w, h = cv.boundingRect(cnt)
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

    # 最小外接矩形
    # 1. 计算最小外接矩形 -> 得到旋转矩形参数
    rect = cv.minAreaRect(cnt)
    # 2. 获取角点数组 -> 得到旋转矩形的四个顶点坐标
    box = cv.boxPoints(rect).astype(np.int32)
    # 3. 绘制最小外接矩形
    cv.drawContours(img, [box], -1, (0,255,0), 2)

    # 最小外接圆
    # 1.计算最小外接圆 -> 得到圆心和半径
    (x_circle, y_circle), radius = cv.minEnclosingCircle(cnt)
    # 2. 绘制最小外接圆
    cv.circle(img, (int(x_circle), int(y_circle)), int(radius), (0, 0, 255), 2)

# 显示图像
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()

import numpy as np
from skimage import exposure,data
import matplotlib.pyplot as plt

# 计算直方图
# image =data.camera()*1.0
# hist1=np.histogram(image, bins=2)   #用numpy包计算直方图
# hist2=exposure.histogram(image, nbins=2)  #用skimage计算直方图
# print(hist1)
# print(hist2)

# 绘制直方图
# img = data.camera()
# plt.figure("hist")
# arr = img.flatten()
#
# n, bins, patches = plt.hist(arr, bins=256, normed=1,
#                             edgecolor='None',facecolor='red')
# plt.show()

# 直方图均衡化
img=data.moon()
print(type(img))
plt.figure("hist",figsize=(8,8))

arr=img.flatten()
print(arr)
plt.subplot(221)
plt.imshow(img,plt.cm.gray)  #原始图像
plt.subplot(222)
plt.hist(arr, bins=256, normed=1,edgecolor='None',facecolor='red') #原始图像直方图

img1=exposure.equalize_hist(img)
arr1=img1.flatten()
print(arr1)
plt.subplot(223)
plt.imshow(img1,plt.cm.gray)  #均衡化图像
plt.subplot(224)
plt.hist(arr1, bins=256, normed=1,edgecolor='None',facecolor='red') #均衡化直方图

plt.show()
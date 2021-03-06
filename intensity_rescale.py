import numpy as np
from skimage import exposure
import matplotlib.pyplot as plt
import SimpleITK as sitk

image_path = "06-t1c.nii.gz"
his_path = "06-t1c_intensity_rescale.nii.gz"

img = sitk.ReadImage(image_path)
# print(img)
# print(type(img))
sitk.Show(img, title="pelvic")

img_array = sitk.GetArrayFromImage(img)
# print(type(img_array))
print(img_array.shape)
# print(img_array)
arr = img_array.flatten()
# print(arr)
plt.subplot(211)
plt.title('Rescale intensity')
plt.hist(arr,bins=256,normed=1,edgecolor='None',facecolor='red') #原始图像

img1_array=exposure.rescale_intensity(img_array,out_range=(0,255))
print(img1_array.shape)

img1=sitk.GetImageFromArray(img1_array)
img1.SetOrigin([-171.553, -89.1038, -8.17377])
img1.SetSpacing([0.46875, 0.46875, 5])
#Spacing: [0.46875, 0.46875, 5]
#Origin: [-171.553, -89.1038, -8.17377]
# img1_reshape=img1_array.reshape(20,552,768)
# img1=sitk.GetImageFromArray(img1_reshape)

sitk.Show(img1, title="pelvic_intensity_rescale")
arr1=img1_array.flatten()
plt.subplot(212)
plt.hist(arr1,bins=256,normed=1,edgecolor='None',facecolor='red') #rescale图像


plt.savefig('Rescale intensity.png')
# sitk.WriteImage(img1,his_path)
sitk.WriteImage(img1,his_path)
plt.show()
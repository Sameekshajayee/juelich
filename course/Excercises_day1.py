from os.path import join
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1. Digit Seven
#a. Define the path to your file (Use Join)
path = r'C:\Users\samee\Masters Internship\course_material\course_material\excercises\d1'
file = 'digit_array.npy'
filepath = join(path,file)

# b. Use np.load to load the file 'digit_array.npy'
digit_array= np.load(filepath)

#c. Use plt.imshow() and plt.show() to visualize the image
plt.imshow(digit_array,cmap='gray')
plt.show()

#d. Extract the shape of the image. Print the width and height of the image
shape = digit_array.shape
width = shape[1]
height = shape[0]
print(f'Width of the image is {width} and height of the image {height}')

#e. Try to crop the vertical and horizontal black border by slicing

plt.imshow(digit_array[4:26, 3:24], cmap='gray')
plt.show()

#f. Visualize the cropped image and print the new width and height
newshape = digit_array[4:26, 3:24].shape
print(f'Width of the image is {newshape[1]} and height of the image is {newshape[0]}')



#2. Apollo Bordeaux Dogge
#a. Path to the file "apollo.jpg"
apollo= 'apollo.jpg'
apollo_path=join(path, apollo)

#b. Use the variable np.array(Image.open(file_path)) to visualise the image of a cute dog.

apollo_img= np.array(Image.open(apollo_path))
plt.imshow(apollo_img)
plt.show()

#c. Visualize the individual RGB
#Red Channel
plt.imshow(apollo_img[...,0])
plt.show()

#Blue Channel
plt.imshow(apollo_img[...,2])
plt.show()

#d. The red buldog
apollo_img [:,:,1]=0
apollo_img[:,:,2]=0
plt.imshow(apollo_img)
plt.show()

#e. The blue ear buldog
rgb= np.array(Image.open(apollo_path))
rgb[200:1400, 2400:3200,0]=0
rgb[200:1400, 2400:3200,1]=0
plt.imshow(rgb)
plt.show()


#3. MRI Image
#a. Define the path
mri= 'numpy_array_image.npy'
mri_img_path = join(path,mri)
#b. np.load will load and create a numpy array from the file
mri_img= np.load(mri_img_path)

#c. Theh tumor will be good at slice 30, visualise that part
plt.imshow(mri_img[:,:,30], cmap='gray')
plt.show()

#d. Crop only the tumor region for this slice
tumor_region= mri_img[150:180, 40:70, 30]
plt.imshow(tumor_region,cmap='gray')
plt.show()

#e. Play around crop interesting organs
#ventrical region
plt.imshow(mri_img[80:150,60:115,110], cmap='gray')
plt.show()
#putamen
plt.imshow(mri_img[90:130,58:72,100], cmap='gray')
plt.show()

#f. So, far we only visualized the axial view. Let's inspect the tumor region horizontally and sagittal
#sagittal view
plt.imshow(mri_img[:,85,:], cmap='gray')
plt.show()
plt.imshow(np.rot90(mri_img[:,85,:]), cmap='gray')
plt.show()

#Coronal
plt.imshow(np.rot90(mri_img[90,:,:]), cmap='gray')
plt.show()
# Nucleus Caudatus
plt.imshow(np.rot90(mri_img[90,60:120,80:120]), cmap='gray')
plt.show()
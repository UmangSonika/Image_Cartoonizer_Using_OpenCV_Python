#First let's import all the necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

#Now let's take image path using command line arguement

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Image_Path")
args=vars(ap.parse_args())

image_org_= cv2.imread(args["image"]) #whenever we will say args["image"] this will be equal to whatever command we have written after --image.

#if you don't want to use command line arguements, then just simply replace the above line with the following line.
# image_org_ = cv2.imread("image.JPG")
#here i am assuming you have a JPG image in the same path as your code.

image_org_mat = cv2.cvtColor(image_org_,cv2.COLOR_BGR2RGB) #converting image format from BGR to RGB

#we are going to use matplotlib for presenting two images in one window.
#Matplotlib and OpenCV have one thing different and that is OpenCV reads image in BGR format while matplotlib reads image in RGB format.
# That is why to make a image read by OpenCV compatible with matplotlib we have written the above statement.

image_org = cv2.resize(image_org_,(int((image_org_.shape[1])/2),int((image_org_.shape[0])/2))) #this is optional

#The above line decreases the size of the image and it is optional to you if you want to resize the image or not.
#Here i have made the size half of original size.

image = image_org #assigning alias for original image


#now we are going to scale the image down two time using pyrDown function in cv2

for _ in range(2):
    image = cv2.pyrDown(image)

#Now we will apply bilateral filter on the scaled down image N no. of time.
#I have done it 50 time and you can change the value for your convinience   

for _ in range(50):
    bil = cv2.bilateralFilter(image,9,9,7)
    # I am using the block size as 9

#Now we will scale up the image to its original dimensions using pyrUp function.
    
for _ in range(2):
    image = cv2.pyrUp(image)

# If you want to see the image at this position ...
#cv2.imshow("image1",image)

#For most of Image processing we convert the image into its equivalent grayscale image for quick responses and that is what we are doing in the next line. 

gray = cv2.cvtColor(image_org,cv2.COLOR_BGR2GRAY)

#cv2.imshow("gray",gray)
#the above line will show the gray_scaled image


#Now we will use median blurr for the smoothening funtion of image.
# I am doing it with blocksize 7 and you can change it as your wish.

image_blurr = cv2.medianBlur(gray,7)

# Now to detect the edges in the image we will use adaptive thresold method with block size 9

img_edge = cv2.adaptiveThreshold(image_blurr,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,2)

#since we are done with all the filter so now we will convert our image back to BGR from Gray

img_edge = cv2.cvtColor(img_edge,cv2.COLOR_GRAY2BGR)

#This is the most important part. Here we are going to use the bitwise and operator to merge two images
# we are going to using this operator on original_image and then merge it with the img_edge
#So basically what this wil do is just enhance the edges or boundaries and smoothen the other areas so as to create a cartoon effect.

cartoon = cv2.bitwise_and(image_org,img_edge)

#Now again we will have to change BGR to RGB for matplotlib

cartoon_mat = cv2.cvtColor(cartoon,cv2.COLOR_BGR2RGB)

total = [image_org_mat,cartoon_mat] #array having the two images 
title = ["Original_Image","Cartoon_Image"] #title for each image

#cv2.imshow("image",image_org)
#cv2.imshow("image2",cartoon_mat)
#The above two lines can be used if you don't know matplotlib

for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(total[i]) #this will show the image in the window having 1 row and 2 column
    plt.xticks([]),plt.yticks([]) #This will remove the scaling of images
    plt.title(title[i]) #This will print the title on top of each column

plt.show()    #To show the window
    
#At  last if you want to save your cartoon image then add the following code too..
#cv2.imwrite("cartoon.JPG",cartoon_mat)

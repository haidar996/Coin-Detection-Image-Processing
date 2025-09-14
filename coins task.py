#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np

import cv2


# Load the image
image = cv2.imread('D:/image processing/Data/Data/MathWorks Images/testCoinImage1.png')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayimage',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[39]:


_, otsu_thresholded = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('threshhold',otsu_thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[40]:


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))


# In[119]:


opened_image = cv2.morphologyEx(otsu_thresholded, cv2.MORPH_OPEN, kernel)
cv2.imshow('openning',opened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[41]:


erosion_image = cv2.erode(otsu_thresholded, kernel, iterations=1)
cv2.imshow('erosion',erosion_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[42]:



dilated_image = cv2.dilate(erosion_image, kernel, iterations=1)
cv2.imshow('dialation',dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[43]:


final_mask = cv2.bitwise_and(image, image, mask=erosion_image)
cv2.imshow('final_mask',final_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[44]:


gaussian_blurred = cv2.GaussianBlur(final_mask, (5, 5), sigmaX=3, sigmaY=2)
                                    
                                    
                                    
                                    
                                    
                                
edges = cv2.Canny(gaussian_blurred, 30, 100)
cv2.imshow('edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[45]:


erosion_image1 = cv2.erode(erosion_image, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)), iterations=5)
cv2.imshow('erosion_image1',erosion_image1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[46]:


final_mask1=cv2.bitwise_and(edges, edges, mask=erosion_image1)
cv2.imshow('final_mask1',final_mask1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[47]:


dilated_image1=cv2.dilate(final_mask1, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)), iterations=30)
cv2.imshow('dilated_image1',dilated_image1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[48]:


p1=cv2.bitwise_and(dilated_image1, dilated_image1, mask=dilated_image)
p2=cv2.bitwise_and(image, image, mask=p1)
cv2.imshow('p1',p2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[49]:


circles = cv2.HoughCircles(p1, 
                             cv2.HOUGH_GRADIENT, 
                             dp=1.15, 
                             minDist=100, 
                             param1=50, 
                             param2=30, 
                             minRadius=0, 
                             maxRadius=0)

# If some circles are detected, draw them on the original image
if circles is not None:
    circles = np.uint16(np.around(circles))  # Round the circle parameters
    for i in circles[0, :]:
        # Draw the outer circle
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Draw the center of the circle
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)
for i in circles[0, :]:  
    
    print(i[2]) 
cv2.imshow('image',image)
cv2.imshow('p1',p1)
cv2.waitKey(0)
cv2.destroyAllWindows()    


# In[13]:


cv2.imwrite('C:/Users/Laptop Syria/Desktop/saved_image3.jpg', image)


# In[ ]:





# In[ ]:





import cv2
import numpy as np
from matplotlib import pyplot as plt


image1 = cv2.imread("sample1.png")
image2 = cv2.imread("sample2.png")

# Convert images to greyscale
im1_Grey = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
im2_Grey = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Detect ORB features and compute descriptor
## Only for comparision
orb = cv2.ORB_create()
keypoints1, descriptors1 = orb.detectAndCompute(im1_Grey, None)
keypoints2, descriptors2 = orb.detectAndCompute(im2_Grey, None)
image1_o = cv2.drawKeypoints(im1_Grey, keypoints1, None, color=(0,255,0), flags=0)
image2_o = cv2.drawKeypoints(im2_Grey, keypoints2, None, color=(0,255,0), flags=0)

# Detect SIFT features and compute descriptor
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(im1_Grey, None)
kp2, des2 = sift.detectAndCompute(im2_Grey, None)

# Check key points detected
image1_s = cv2.drawKeypoints(im1_Grey, kp1, None, color=(0,0,255), flags=0)
image2_s = cv2.drawKeypoints(im2_Grey, kp2, None, color=(0,0,255), flags=0)

# Show features detected by ORB and SIFT
plt.imshow(image1_o),plt.show()
plt.imshow(image2_o),plt.show()
plt.imshow(image1_s),plt.show()
plt.imshow(image2_s),plt.show()

# Match features detected by SIFT
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# Select good matches
good=[]
good_without_list = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
        good_without_list.append(m)

# Draw good matches
img3 = cv2.drawMatchesKnn(image1, kp1, image2, kp2, good, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# cv2.imwrite("matches.jpg", img3)

# Extract location of good matches
points1 = np.float32([kp1[m.queryIdx].pt for m in good_without_list])
points2 = np.float32([kp2[m.trainIdx].pt for m in good_without_list])

# Find Homography
h, status = cv2.findHomography(points1, points2)

# Use Homography
height, width, channels = image2.shape
imReg = cv2.warpPerspective(image1, h, (width, height))

# Save aligned image
outFilename = "aligned1.jpg"
print("Saving aligned image: ", outFilename)
# cv2.imwrite(outFilename, imReg)
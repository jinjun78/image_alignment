import cv2
import numpy as np

def alignSIFT(im1, im2, out1, out2):
    im1_Grey = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2_Grey = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # Detect SIFT features and compute descriptor
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(im1_Grey, None)
    kp2, des2 = sift.detectAndCompute(im2_Grey, None)

    print("Total features detected in Reference Image: ", len(kp1),
          "\nTotal features detected in Target Image: ", len(kp2))

    # Match features detected by SIFT
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Select good matches
    good = []
    good_without_list = []
    for m, n in matches:
        if m.distance < 0.65 * n.distance:
            good.append([m])
            good_without_list.append(m)

    print("Number of good matches found: ", len(good))

    # Draw good matches
    good_match = cv2.drawMatchesKnn(im1, kp1, im2, kp2, good, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    match_name = out1
    print("Saving matching image: ", match_name)
    cv2.imwrite(match_name, good_match)

    # Extract location of good matches
    points1 = np.float32([kp1[m.queryIdx].pt for m in good_without_list])
    points2 = np.float32([kp2[m.trainIdx].pt for m in good_without_list])

    # Find Homography
    h, status = cv2.findHomography(points1, points2)
    # Use Homography
    height, width, channels = im2.shape
    imReg = cv2.warpPerspective(im1, h, (width, height))

    # Save aligned image
    outFilename = out2
    print("Saving aligned image: ", outFilename)
    cv2.imwrite(outFilename, imReg)
    # return outFilename


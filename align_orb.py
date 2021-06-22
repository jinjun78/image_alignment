from __future__ import print_function
import cv2
import numpy as np

MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 0.15

def alignORB(im1, im2, out1, out2):
    # Convert images to grayscale
    im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # Detect ORB features and compute descriptor
    orb = cv2.ORB_create(MAX_FEATURES)
    keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

    # Detect ORB features and compute descriptor
    # image1_o = cv2.drawKeypoints(im1Gray, keypoints1, None, color=(0,255,0), flags=0)
    # image2_o = cv2.drawKeypoints(im2Gray, keypoints2, None, color=(0,255,0), flags=0)

    # Show features detected by ORB
    # plt.imshow(image1_o),plt.show()
    # plt.imshow(image2_o),plt.show()

    # Match features
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = matcher.match(descriptors1, descriptors2, None)

    # Sort matches by score
    matches.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    # Draw top matches
    imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
    matchesFilename = out1
    cv2.imwrite(matchesFilename, imMatches)

    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    # Find homography
    h, status = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = im2.shape
    imReg = cv2.warpPerspective(im1, h, (width, height))

    print("Aligning images ...")

    # Write aligned image to disk
    outFilename = out2
    print("Saving aligned image: ", outFilename)
    cv2.imwrite(outFilename, imReg)

    print('Estimated homography : \n', h)

# if __name__ == '__main__':
#
#     # Read images with opencv
#     refFilename = "P2 S001_r.png"  #reference image
#     imFilename = "P2 S002_g.png"  #image to be aligned
#     ref = cv2.imread(refFilename, cv2.IMREAD_COLOR)
#     tar = cv2.imread(imFilename, cv2.IMREAD_COLOR)
#     print("Reference image : ", refFilename,
#           "\nImage to be aligned : ", imFilename)
#
#     alignImages(ref, tar)



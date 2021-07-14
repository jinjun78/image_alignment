import cv2
import numpy as np
from PIL import Image
from tabulate import tabulate
import test_alignment as test
import test_quality as quality

MAX_FEATURES = 500


def alignORB(im1, im2, out1, percent):
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
    numGoodMatches = int(len(matches) * percent)
    matches = matches[:numGoodMatches]

    print("Number of good matches found: ", len(matches))

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
    return(h)

def warpImage(im,h):
    # Use homography
    height, width, channels = im.shape
    imReg = cv2.warpPerspective(im, h, (width, height))  # warping im3 with h from im1 and im2 matching
    return(imReg)

refFilename = "S007_clr_br.png" #reference image
imFilename = "S008_clr_br.png"  #target image
applyFile = "Conor.jpg" # image to be applied
ref = cv2.imread(refFilename, cv2.IMREAD_COLOR)
tar = cv2.imread(imFilename, cv2.IMREAD_COLOR)
app = cv2.imread(applyFile, cv2.IMREAD_COLOR)
conorbig = cv2.imread("ConorBig.jpg", cv2.IMREAD_COLOR)

percent = 0.2 ## Good Match Percent
### Name the id of output image
para = str(percent).replace(".", "")
# Change the name tag for different attempts
file_id = "h%s"%para

matchFilename = "matches_%s.jpg" %file_id  # features matching image
outFilename = "aligned_%s.jpg" %file_id #aligned image
align_h = alignORB(ref, tar, matchFilename, percent)
warped_im = warpImage(app, align_h)
cv2.imwrite("warped_im.jpg", warped_im)
warped_big = warpImage(conorbig, align_h)
cv2.imwrite("warped_big_im.jpg",warped_big)

# Result testing
# Convert to PIL images
ref = Image.fromarray(cv2.cvtColor(ref, cv2.COLOR_BGR2RGB))
app = Image.fromarray(cv2.cvtColor(app, cv2.COLOR_BGR2RGB))
out = Image.fromarray(cv2.cvtColor(warped_im, cv2.COLOR_BGR2RGB))
## Match reference image and target image respectively with the aligned image,
## make the new image into two of the channels of RGB array
ims = [test.alignImages(ref, out, 1, 0),
       test.alignImages(app, out, 1, 0)]
nrows, ncols = (1, 2)
w, h = ims[0].size
imnew = Image.new("RGB", (w * ncols, h * nrows))
for i, im in enumerate(ims):
    row = int(i / ncols)
    col = i % ncols
    imnew.paste(im, (w * col, h * row))

testFilename = "test_%s.jpg" % file_id  # quality test image
print("Saving alignment quality test image: ", testFilename)
imnew.save(testFilename,quality=100)

dist1, corr1 = quality.eucli_dist(app, out)
table = [["Source", "Euclidean Distance", "Correlation Coefficient"],
         ["Applied Image", dist1, corr1]]
print(tabulate(table, headers="firstrow",tablefmt="pretty"), "\n")

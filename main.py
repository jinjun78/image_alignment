from RGB_split import Split
import alignment as aln
import cv2


# This script is for alignment of R channel of "P2 SOO1" and B channel of "P2 S002"
image1 = "sample1.png"
image2 = "sample2.png"

if __name__ == '__main__':
    refFilename = image1  #reference image
    imFilename = image2  #image to be aligned
    ref = cv2.imread(refFilename, cv2.IMREAD_COLOR)
    tar = cv2.imread(imFilename, cv2.IMREAD_COLOR)
    print("Reference image : ", refFilename,
          "\nImage to be aligned : ", imFilename)
    aln.alignImages(ref, tar)

from RGB_split import Split
import alignment as aln
import cv2


# This script is for alignment of R channel of "P2 SOO1" and B channel of "P2 S002"
image1 = "P2 S001.png"
image2 = "P2 S002.png"

if __name__ == '__main__':
    refFilename = Split(image1).save_r()  #reference image
    imFilename = Split(image2).save_b()  #image to be aligned
    ref = cv2.imread(refFilename, cv2.IMREAD_COLOR)
    tar = cv2.imread(imFilename, cv2.IMREAD_COLOR)
    print("Reference image : ", refFilename,
          "\nImage to be aligned : ", imFilename)
    aln.alignImages(ref, tar)

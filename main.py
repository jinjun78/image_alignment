import align_orb as aln_olb
import align_sift as aln_sift
import test_alignment as test
import cv2
from PIL import Image


if __name__ == '__main__':
    refFilename = "sec1_colour.png" #reference image
    imFilename = "sec2_colour.png"  #target image
    ref = cv2.imread(refFilename, cv2.IMREAD_COLOR)
    tar = cv2.imread(imFilename, cv2.IMREAD_COLOR)
    print("Reference image : ", refFilename,
          "\nImage to be aligned : ", imFilename)
    # aln_olb.alignORB(ref, tar)
    align = aln_sift.alignSIFT(ref, tar)

    ref = Image.open(refFilename)
    tar = Image.open(imFilename)
    out = Image.open(align)
    print("Saving alignment quality test image: ", align)
    test.alignImages(ref,out,0,1)

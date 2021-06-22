import align_orb as aln_orb
import align_sift as aln_sift
import test_alignment as test
import cv2
from PIL import Image


if __name__ == '__main__':
    # Alignment
    refFilename = "sec1_colour.png" #reference image
    imFilename = "sec2_colour.png"  #target image
    ref = cv2.imread(refFilename, cv2.IMREAD_COLOR)
    tar = cv2.imread(imFilename, cv2.IMREAD_COLOR)
    print("Reference image : ", refFilename,
          "\nImage to be aligned : ", imFilename)

    matchFilename = "results/matches_auto.jpg" #features matching image
    outFilename = "results/aligned_auto.jpg" #aligned image
    ## Aligning function option: ORB
    align = aln_orb.alignORB(ref, tar, matchFilename, outFilename)
    ## Aligning function option: SIFT
    # align = aln_sift.alignSIFT(ref, tar, matchFilename, outFilename)

    # Result testing
    ref = Image.open(refFilename)
    tar = Image.open(imFilename)
    out = Image.open(outFilename)
    ## Match reference image and target image respectively with the aligned image,
    ## make the new image into two of the channels of RGB array
    ims = [test.alignImages(ref,out,0,1),
           test.alignImages(tar,out,0,1)]
    nrows, ncols = (1, 2)
    w, h = ims[0].size
    imnew = Image.new("RGB", (w * ncols, h * nrows))
    for i, im in enumerate(ims):
        row = int(i / ncols)
        col = i % ncols
        imnew.paste(im, (w * col, h * row))
    print("Saving alignment quality test image: ", outFilename)
    imnew.resize(reversed(ims[0].size)).save("results/test_auto.jpg")

import align_orb as aln_orb
import align_sift as aln_sift
import test_alignment as test
import cv2
from PIL import Image
import sys


sys.stdout = open("results/output.txt", "a")

if __name__ == '__main__':
    # Alignment
    refFilename = "section1_colour.png" #reference image
    imFilename = "section2_colour.png"  #target image
    ref = cv2.imread(refFilename, cv2.IMREAD_COLOR)
    tar = cv2.imread(imFilename, cv2.IMREAD_COLOR)
    print("Reference image : ", refFilename,
          "\nImage to be aligned : ", imFilename)

    ## Aligning option1: ORB
    percent = 0.25 ## Good Match Percent
    ### Name the id of output image
    para = str(percent).replace(".", "")
    file_id = "colour_o%s"%para

    matchFilename = "results/matches_%s.jpg" %file_id  # features matching image
    outFilename = "results/aligned_%s.jpg" %file_id #aligned image
    align = aln_orb.alignORB(ref, tar, matchFilename, outFilename, percent)

    ## Aligning option2: SIFT
    # distance = 0.85
    ### Name the id of output image
    # para = str(distance).replace(".", "")
    # file_id = "colour_s%s" % para

    # matchFilename = "results/matches_%s.jpg" %file_id #features matching image
    # outFilename = "results/aligned_%s.jpg" %file_id #aligned image
    # align = aln_sift.alignSIFT(ref, tar, matchFilename, outFilename, distance)

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
    print("Saving alignment quality test image: ", outFilename, "\n")
    imnew.resize(reversed(ims[0].size)).save("results/test_%s.jpg" %file_id)


sys.stdout.close()
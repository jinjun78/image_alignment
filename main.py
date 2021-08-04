import cv2
from PIL import Image
import numpy
from align.sizes import resize_and_crop as resize
from align.contrast_n_brightness import contrast_and_brightness
from align import align_orb as aln_orb, align_sift as aln_sift, \
    test_alignment as test, test_quality as quality
from tabulate import tabulate
import sys


sys.stdout = open("results/output.txt", "a")

if __name__ == '__main__':
    # File path
    refFilename = "S007.jpg" #reference image
    imFilename = "S008.jpg"  #target image
    path1 = "original/P2 " + refFilename
    path2 = "original/P2 " + imFilename

    # Image preprocessing
    img1 = Image.open(path1)
    img2 = Image.open(path2)
    size = (int(img1.size[0] / 30), int(img1.size[1] / 30))
    ## Resize image into a 50 times smaller size
    resized_1 = resize(img1, size)
    resized_2 = resize(img2, size)
    ## Improve brightness and contrast of the images
    img1_prc = contrast_and_brightness(resized_1)
    img2_prc = contrast_and_brightness(resized_2)

    # Alignment
    print("Reference image : ", refFilename,
          "\nImage to be aligned : ", imFilename)
    ref = numpy.array(img1_prc)
    tar = numpy.array(img2_prc)
    ## Conver RGB to BGR
    ref = ref[:, :, ::-1].copy()
    tar = tar[:, :, ::-1].copy()

    # Aligning option1: ORB
    percent = 0.5# Good Match Percent
    ### Name the id of output image
    para = str(percent).replace(".", "")
    # Change the name tag for different attempts
    file_id = "full_o%s"%para

    matchFilename = "results/matches_%s.jpg" %file_id  # features matching image
    outFilename = "results/aligned_%s.jpg" %file_id #aligned image
    align = aln_orb.alignORB(ref, tar, matchFilename, outFilename, percent)

    # # Aligning option2: SIFT
    # distance = 0.75
    # ## Name the id of output image
    # para = str(distance).replace(".", "")
    # file_id = "clr_br_s%s" % para
    #
    # matchFilename = "results/matches_%s.jpg" %file_id #features matching image
    # outFilename = "results/aligned_%s.jpg" %file_id #aligned image
    # align = aln_sift.alignSIFT(ref, tar, matchFilename, outFilename, distance)

    # Result testing
    ref = img1_prc
    tar = img2_prc
    out = Image.open(outFilename)
    ## Match reference image and target image respectively with the aligned image,
    ## make the new image into two of the channels of RGB array
    ims = [test.alignImages(ref,out,1,0),
           test.alignImages(tar,out,1,0)]
    nrows, ncols = (1, 2)
    w, h = ims[0].size
    imnew = Image.new("RGB", (w * ncols, h * nrows))
    for i, im in enumerate(ims):
        row = int(i / ncols)
        col = i % ncols
        imnew.paste(im, (w * col, h * row))

    testFilename = "results/test_%s.jpg" %file_id #quality test image
    print("Saving alignment quality test image: ", testFilename)
    imnew.resize(reversed(ims[0].size)).save(testFilename)

    dist1, corr1 = quality.eucli_dist(ref, out)
    dist2, corr2 = quality.eucli_dist(tar, out)
    table = [["Source", "Euclidean Distance", "Correlation Coefficient"],
             ["Reference Image", dist1, corr1],
             ["Target Image", dist2, corr2]]
    print(tabulate(table, headers="firstrow",tablefmt="pretty"), "\n")
sys.stdout.close()
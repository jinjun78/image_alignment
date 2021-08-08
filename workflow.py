import cv2
from PIL import Image
import numpy
import pandas
from align.sizes import resize_and_crop as resize
from align.contrast_n_brightness import contrast_and_brightness
from align import align_orb as aln_orb, align_sift as aln_sift, \
    test_alignment as test, test_quality as quality
from tabulate import tabulate

class Worlflow():
    def __init__(self, ref, im, num):
        self.ref = ref
        self.im = im
        self.num = num

        path1 = "final_output/aligned/good/{}".format(ref)
        path2 = "original/P2 {}".format(im)

        # Image preprocessing
        img1 = Image.open(path1)
        img2 = Image.open(path2)
        # size = (int(img1.size[0] / 40), int(img1.size[1] / 40))
        size = img1.size
        ## Resize image into a 50 times smaller size
        # resized_1 = resize(img1, size)
        resized_2 = resize(img2, size)
        ## Improve brightness and contrast of the images
        # img1_prc = contrast_and_brightness(resized_1)
        img1_prc = img1
        img2_prc = contrast_and_brightness(resized_2)
        # Alignment
        print("Reference image : ", self.ref,
              "\nImage to be aligned : ", self.im)
        ref = numpy.array(img1_prc)
        tar = numpy.array(img2_prc)
        ## Conver RGB to BGR
        ref = ref[:, :, ::-1].copy()
        tar = tar[:, :, ::-1].copy()

        # Aligning option1: ORB
        MAX_FEATURES = (500,1000)
        data = []
        for f in MAX_FEATURES:
            for p in numpy.arange(0.1, 1.1, 0.1):
                percent = float('%1f' %p) # Good Match Percent
                ### Name the id of output image
                para = str(percent).replace(".", "")
                # Change the name tag for different attempts
                file_id = "{}_{}_{}".format(self.num, f, percent)

                matchFilename = "final_output/aligned/matches_%s.jpg" %file_id  # features matching image
                outFilename = "final_output/aligned/aligned_%s.jpg" %file_id #aligned image
                align = aln_orb.alignORB(ref, tar, matchFilename, outFilename, percent, f)

                # Result testing
                out = Image.open(outFilename)
                # Match reference image and target image respectively with the aligned image,
                # make the new image into two of the channels of RGB array
                ims = [test.alignImages(img1_prc,out,1,0),
                       test.alignImages(img2_prc,out,1,0)]
                nrows, ncols = (1, 2)
                w, h = ims[0].size
                imnew = Image.new("RGB", (w * ncols, h * nrows))
                for i, im in enumerate(ims):
                    row = int(i / ncols)
                    col = i % ncols
                    imnew.paste(im, (w * col, h * row))

                testFilename = "final_output/quality test/test_%s.jpg" %file_id #quality test image
                print("Saving alignment quality test image: ", testFilename)
                new_size = (ims[0].size[0], int(ims[0].size[1]/2))
                imnew.resize(new_size).save(testFilename)

                dist1, corr1 = quality.eucli_dist(img1_prc, out)
                dist2, corr2 = quality.eucli_dist(img2_prc, out)
                data.append([file_id, dist1, corr1, dist2,corr2])


        columns = ['image','ED1', 'CC1', 'ED2', 'CC2']
        df = pandas.DataFrame(data, columns=columns)
        print(df.sort_values(by=['CC2'], ascending=False))
        print(df.sort_values(by=['ED2']))
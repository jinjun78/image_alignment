import cv2
from PIL import Image
import numpy
import pandas
from align.sizes import resize_and_crop as resize
from align.contrast_n_brightness import contrast_and_brightness
from align import align_orb as aln_orb, align_sift as aln_sift, \
    test_alignment as test, test_quality as quality
from tabulate import tabulate
import time

class Worlflow():
    def __init__(self, ref, im, count):
        self.ref = ref
        self.im = im
        self.count = count

        start_time = time.time()
        # path1 = "original/P2 {}".format(self.ref)
        path1 = "final_output/4th/alignment/{}".format(self.ref)
        path2 = "original/P2 {}".format(self.im)

        # Image preprocessing
        img1 = Image.open(path1)
        img2 = Image.open(path2)

        # IF count =1: Resize image into a 30 times smaller size
        # size = (int(img1.size[0] / 30), int(img1.size[1] / 30))
        # resized_1 = resize(img1, size)
        # resized_2 = resize(img2, size)
        # ## Improve brightness and contrast of the images
        # img1_prc = contrast_and_brightness(resized_1)
        # img2_prc = contrast_and_brightness(resized_2)

        # IF count >1: Resize target image into the size of reference image
        size = (int(img2.size[0] / 30), int(img2.size[1] / 30))
        resized_1 = resize(img1, size)
        resized_2 = resize(img2, size)
        img1_prc = resized_1
        img2_prc = contrast_and_brightness(resized_2)


        # Alignment
        print("Reference image : ", self.ref,
              "\nImage to be aligned : ", self.im)
        ref = numpy.array(img1_prc)
        tar = numpy.array(img2_prc)
        ## Conver RGB to BGR
        ref = ref[:, :, ::-1].copy()
        tar = tar[:, :, ::-1].copy()
        prepro_time = time.time()

        # Aligning option1: ORB
        MAX_FEATURES = (500, 1000)
        data = []
        align_time = time.time()
        for f in MAX_FEATURES:
            for p in numpy.arange(0.1, 1.1, 0.1):
                percent = float('%1f' % p)  # Good Match Percent
                ### Name the id of output image
                para = str(percent).replace(".", "")
                # Change the name tag for different attempts
                file_id = "{}_{}_{}".format(self.count, f, percent)
                saving_path = "final_output/4th/"
                matchFilename = "%salignment/matches_%s.jpg" % (saving_path, file_id)  # features matching image
                outFilename = "%salignment/aligned_%s.jpg" % (saving_path, file_id)  # aligned image
                # Align image
                single_time = time.time()
                align = aln_orb.alignORB(ref, tar, matchFilename, outFilename, percent, f)
                single_time2 = time.time()

                # Result testing
                out = Image.open(outFilename)
                # Match reference image and target image respectively with the aligned image,
                # make the new image into two of the channels of RGB array
                ims = [test.alignImages(img1_prc, out, 1, 0),
                       test.alignImages(img2_prc, out, 1, 0)]
                nrows, ncols = (1, 2)
                w, h = ims[0].size
                imnew = Image.new("RGB", (w * ncols, h * nrows))
                for i, im in enumerate(ims):
                    row = int(i / ncols)
                    col = i % ncols
                    imnew.paste(im, (w * col, h * row))

                testFilename = "%stesting/test_%s.jpg" % (saving_path,file_id)  # quality test image
                print("Saving alignment quality test image: ", testFilename)
                new_size = (ims[0].size[0], int(ims[0].size[1] / 2))
                imnew.resize(new_size).save(testFilename, quality=90)

                corr1 = quality.correlation(img1_prc, out)
                corr2 = quality.correlation(img2_prc, out)
                data.append([file_id, corr1, corr2])
        aligned_time = time.time()

        columns = ['image', 'CC1', 'CC2']
        df = pandas.DataFrame(data, columns=columns)
        table_name = "%stesting/table_%d.csv" % (saving_path,self.count)
        df.to_csv(table_name, index=False)
        opt_CC = df.sort_values(by=['CC2'], ascending=False)
        end_time = time.time()

        output = [[" ", "time(s)"],
                  ["Total run time", end_time-start_time],
                  ["Total alignment and testing time", aligned_time-align_time],
                  ["Preprocessing time", prepro_time-start_time],
                  ["Single alignment time", single_time2-single_time]]
        out_table = tabulate(output,tablefmt="pretty")

        print("Best Alignment:\t",opt_CC[:3])
        # print(df.sort_values(by=['CC2'], ascending=False))
        print(out_table)
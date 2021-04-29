from PIL import Image
import cv2

Image.MAX_IMAGE_PIXELS = 400000000


class Split:

    def __init__(self, image):
        self.image = image
        self.outname = image[:-4]

        self.im = Image.open(self.image).convert('LA')


    def save_r(self):
        r = self.im.split()[0]
        outfile = str(self.outname) + '_r.png'
        r.save(outfile)
        return outfile
        print(self.outname, ": R channel split and saved.")

    def save_g(self):
        g = self.im.split()[1]
        outfile = str(self.outname) + '_g.png'
        g.save(outfile)
        return outfile
        print(self.outname, ": G channel split and saved.")

    def save_b(self):
        b = self.im.split()[2]
        outfile = str(self.outname) + '_b.png'
        b.save(outfile)
        return outfile
        print(self.outname, ": B channel split and saved.")

    # print(outname, ": RGB channels separated and saved.")

    # Test if image is opened in greyscale
    def testgrey(self):
        self.im.save('greyscale.png')




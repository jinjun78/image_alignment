from PIL import Image
import numpy as np
from align.sizes import resize_and_crop

def alignImages(im1,im2,chX=0,chY=1):
  # Generally, images are of different sizes, so crop "from middle" to match
  targwidth = min((im1.size[0],im2.size[0]))
  targheight = min((im1.size[1],im2.size[1]))

  # im1 = resize_and_crop(im1,(targwidth,targheight),crop_origin="middle")
  # im2 = resize_and_crop(im2,(targwidth,targheight),crop_origin="middle")

  # Convert images to greyscale and cast as an array of unsigned 8 bit integers
  arr1 = np.array(im1.convert('L'),dtype=np.uint8)
  arr2 = np.array(im2.convert('L'),dtype=np.uint8)

  # Build an empty 3D array filled with zeros (unsigned 8 bit integers) to represent a black RGB image
  arr = np.zeros([arr1.shape[0],arr1.shape[1],3],dtype=np.uint8)
  # Copy the resized greyscale images into two of the "channels" of our "RGB" array
  arr[:,:,chX]=arr1
  arr[:,:,chY]=arr2
  # Convert "RGB" array into an image
  im = Image.fromarray(arr)
  return(im)

if __name__ == "__main__":
 # Let's have a look at all possible combinations of channels
 im1 = Image.open("sec2_colour.png")
 im2 = Image.open("results/aligned_orb_clr.jpg")
 ims = [
     alignImages(im1,im2,0,1),
     alignImages(im1,im2,1,2),
     alignImages(im1,im2,0,2),
     alignImages(im1,im2,1,0),
     alignImages(im1,im2,2,1),
     alignImages(im1,im2,2,0)
     ]
 nrows,ncols=(2,3)
 w,h = ims[0].size
 imnew = Image.new("RGB",(w*ncols,h*nrows))
 for i,im in enumerate(ims):
     row = int(i/ncols)
     col = i%ncols
     imnew.paste(im,(w*col,h*row))
 #imnew.save("test.jpg")
 imnew.resize(reversed(ims[0].size)).save("results/test_orb_clr.jpg")


from PIL import Image
import numpy as np
from sizes import resize_and_crop


# Calculate Euclidean Distance
ref = Image.open("sec1_colour.png").convert('L')
tar = Image.open("sec2_colour.png").convert('L')
aligned= Image.open("results/aligned_orb_clr.jpg").convert('L')

targwidth = min((ref.size[0],aligned.size[0]))
targheight = min((ref.size[1],aligned.size[1]))

im1 = resize_and_crop(ref,(targwidth,targheight), crop_origin="middle")
im2 = resize_and_crop(aligned,(targwidth,targheight), crop_origin="middle")

# Convert images to greyscale and cast as an array of unsigned 8 bit integers
arr1 = np.array(im1, dtype=np.uint8)
arr2 = np.array(im2, dtype=np.uint8)


dist1 = np.linalg.norm(arr1-arr2)
dist2 = np.sqrt(np.sum(np.square(arr1-arr2)))
print(dist1)
print(dist2)
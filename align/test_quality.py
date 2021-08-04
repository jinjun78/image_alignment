from PIL import Image
import numpy as np
from sizes import resize_and_crop
from scipy.spatial import distance

def eucli_dist (source, aligned):
    # Calculate Euclidean Distance
    targwidth = min((source.size[0],aligned.size[0]))
    targheight = min((source.size[1],aligned.size[1]))

    im1 = resize_and_crop(source,(targwidth,targheight), crop_origin="middle")
    im2 = resize_and_crop(aligned,(targwidth,targheight), crop_origin="middle")

    # Convert images to greyscale and cast as an array of integers
    arr1 = np.array(im1, dtype=np.int64)
    arr2 = np.array(im2, dtype=np.int64)

    # Drop pixels from both images which are black in array
    to_keep = arr2>0
    arr1 = arr1[to_keep]
    arr2 = arr2[to_keep]

    dist = np.linalg.norm((arr1-arr2))
    # dist2 = np.sqrt(np.sum(np.square(arr1-arr2)))


    # Convert 2D arrays of greyscale pixel intensities into 1D vectors
    f1 = arr1.flatten()
    f2 = arr2.flatten()

    # Drop pixels from both images which are black in array
    to_keep = f2 > 0
    f1 = f1[to_keep]
    f2 = f2[to_keep]

    # Calculate correlation between (non-zero) pixel intensities in the two images
    corr = np.corrcoef(f1, f2)[0,1]

    return dist, corr
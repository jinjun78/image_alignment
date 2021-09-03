import os
import czifile as cz
from PIL import Image
import numpy as np

# This path is for opening images from Netfolders of Filr
filrpath = '''D:\\Filr\\NetFolders\\'''  # Users should edit this to match their machine
datapath = '''RDW ION06\\06\\mitodisease\\Amy V\\Post-doc and fellowship\\Jo Elson\\P2\\'''
fpath = os.path.join(filrpath, datapath)


# Creat a list for all files in the directory
fnames = [f for f in os.listdir(fpath) if f.endswith(".czi")]

# Choose first two files
for i in fnames[:2]:
    arr = cz.imread(os.path.join(fpath, i))
    outname = i[:-4]
    imarr = arr[0, 0, 0, :, :, :]

    r = imarr[:,:,0]
    g = imarr[:,:,1]
    b = imarr[:,:,2]

    # Image.fromarray(r).save(outname+"_r.tiff")
    # Image.fromarray(r).save(outname+"_g.tiff")
    # Image.fromarray(r).save(outname+"_b.tiff")
    # print(outname, ": RGB channels separated and saved.")

# Should do quantifications on imarr, but note that it contains 16-bit integers
# Need to convert to 8-bit to make an RGB image (with PIL)
    imarr2 = np.array(np.round((imarr-np.min(imarr))/(np.max(imarr)-np.min(imarr))*255.0), dtype=np.uint8)
    Image.fromarray(imarr2).save(outname + ".jpg")
    print("Saved", outname+".jpg")
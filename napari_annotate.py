import napari
from napari.utils.settings import SETTINGS
SETTINGS.application.ipy_interactive = False

from PIL import Image
import numpy as np
import cv2

def warpImage(im,h):
    # Use homography
    height, width, channels = im.shape
    imReg = cv2.warpPerspective(im, h, (width, height))  # warping im3 with h from im1 and im2 matching
    return(imReg)

im1 = Image.open("S005_clr_br.png")
im2 = Image.open("S006_clr_br.png")

w1,h1=im1.size
w2,h2=im2.size

w = w1+w2
h = np.max([h1,h2])
im = Image.new("RGB", (w,h))
im.paste(im1,(0,0))
im.paste(im2,(w1,0))

arr = np.array(im,dtype=np.uint8)

viewer = napari.view_image(arr,name="Matching fibres between sections")
layer_pts = viewer.add_shapes(data=None,shape_type="line", edge_width=1,edge_color="yellow")
napari.run()

if len(layer_pts.data)>0:
    points1 = np.array([[p[0][0],p[0][1]] for p in layer_pts.data])
    points2 = np.array([[p[1][0],p[1][1]-w1] for p in layer_pts.data])

    h, status = cv2.findHomography(points1, points2, cv2.RANSAC)
    cv2im = np.array(im1)
    cv2im = cv2im[:,:,::-1].copy()
    wim = warpImage(cv2im,h)
    wimp = Image.fromarray(cv2.cvtColor(wim, cv2.COLOR_BGR2RGB))
    wimp.show()




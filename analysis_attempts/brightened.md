## Samples Description 
#### Reference image
![reference image](../sec1_bright.png)

A cropped section from P2 S007.jpg. The image is brightened version of the reference image from [greybackground](./greybackground.md)   

#### Target image
![target image](../sec2_bright.png)

A cropped section from P2 S008.jpg. The image is brightened version of the target image from [greybackground](./greybackground.md)

### Method 1
[align_sift.py](../align_sift.py) was run to align the two samples. Features of the images were detected by [SIFT](https://docs.opencv.org/master/da/df5/tutorial_py_sift_intro.html) detector and matched by [cv2.BFMatcher.knnMatch](https://docs.opencv.org/master/d3/da1/classcv_1_1BFMatcher.html). Matches with distance smaller than *0.75* were used for warping.
#### Features & matches
![](../results/matches_br075.jpg)

|  Matching Data  |   |
| -----------------------------------  | --- |
| Total features detected in Ref Image |  935  |
| Total features detected in Tar Image |  830  |
|          Euclidean Distance          | <0.75 |
|     Number of good matches found     |  48   |
#### Alignment
![](../results/aligned_br075.jpg)
#### Quality test
![](../results/test_br075.jpg)

### Method 2
[align_sift.py](../align_sift.py) was run to align the two samples. Features of the images were detected by [SIFT](https://docs.opencv.org/master/da/df5/tutorial_py_sift_intro.html) detector and matched by [cv2.BFMatcher.knnMatch](https://docs.opencv.org/master/d3/da1/classcv_1_1BFMatcher.html). Matches with distance smaller than *0.60* were used for warping.
#### Features & matches
![](../results/matches_br060.jpg)

|  Matching Data  |   |
| -----------------------------------  | --- |
| Total features detected in Ref Image | 935  |
| Total features detected in Tar Image | 830  |
|          Euclidean Distance          | <0.6 |
|     Number of good matches found     |  19  |
#### Alignment
![](../results/aligned_br060.jpg)
#### Quality test
![](../results/test_br060.jpg)

### Method 3
[align_sift.py](../align_sift.py) was run to align the two samples. Features of the images were detected by [SIFT](https://docs.opencv.org/master/da/df5/tutorial_py_sift_intro.html) detector and matched by [cv2.BFMatcher.knnMatch](https://docs.opencv.org/master/d3/da1/classcv_1_1BFMatcher.html). Matches with distance smaller than *0.55* were used for warping.
#### Features & matches
![](../results/matches_br055.jpg)

|  Matching Data  |   |
| -----------------------------------  | --- |
| Total features detected in Ref Image |  935  |
| Total features detected in Tar Image |  830  |
|          Euclidean Distance          | <0.55 |
|     Number of good matches found     |  14   |
#### Alignment
![](../results/aligned_br055.jpg)
#### Quality test
![](../results/test_br055.jpg)
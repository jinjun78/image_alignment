# Image alignment
Attempts to automatically align section images.

## Samples Description 
![](sec1_con_resized.png)

A cropped section from P2 S007.jpg with size of 8 times smaller, higher contrast and a grey background.

![](sec2_con_resized.png)

A cropped section from P2 S008.jpg with size of 8 times smaller, higher contrast and a grey background.

### Method 1
'align_orb.py' was run to align the two samples. Features of the images were detected by ORB detector. Features were matched by cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING and top 15% matches were selected for warping.

#### Features & matches
![](results/matches_orb.jpg)
#### Alignment
![](results/aligned_orb.jpg)

### Method 2
'align_sift.py' was run to align the two samples. Features of the images were detected by SIFT detector and matched by cv2.BFMatcher.knnMatch. Matches with distance smaller than *0.75* were used for warping.
#### Features & matches
![](results/matches_075.jpg)
#### Alignment
![](results/aligned_075.jpg)

### Method 3
'align_sift.py' was run to align the two samples. Features of the images were detected by SIFT detector and matched by cv2.BFMatcher.knnMatch. Matches with distance smaller than *0.65* were used for warping.
#### Features & matches
![](results/matches_065.jpg)
#### Alignment
![](results/aligned_065.jpg)

### Method 4
'align_sift.py' was run to align the two samples. Features of the images were detected by SIFT detector and matched by cv2.BFMatcher.knnMatch. Matches with distance smaller than *0.6* were used for warping.
#### Features & matches
![](results/matches_060.jpg)
#### Alignment
![](results/aligned_060.jpg)

### Method 5
'align_sift.py' was run to align the two samples. Features of the images were detected by SIFT detector and matched by cv2.BFMatcher.knnMatch. Matches with distance smaller than *0.55* were used for warping.
#### Features & matches
![](results/matches_055.jpg)
#### Alignment
![](results/aligned_055.jpg)

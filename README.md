# image_alignment
imaging aligning and its quality test

## Samples Description 
**resource image: "sec1_con_resized.png"**

A cropped section from P2 S007.jpg with size of 8 times smaller, higher contrast and a grey background.

**target image: a section of P2 S008.jpg**

A cropped section from P2 S007.jpg with size of 8 times smaller, higher contrast and a grey background.

## Methods
1. 'align_orb.py' was run to align the two samples. Features of the images were detected by ORB detector. Features were matched by cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING and top 15% matches were selected for warping.

2. 'align_sift.py' was run to align the two samples. Features of the images were detected by SIFT detector and matched by cv2.BFMatcher.knnMatch. Matches with distance smaller than *0.75* were used for warping.

3. 'align_sift.py' was run to align the two samples. Features of the images were detected by SIFT detector and matched by cv2.BFMatcher.knnMatch. Matches with distance smaller than *0.65* were used for warping.

4. 'align_sift.py' was run to align the two samples. Features of the images were detected by SIFT detector and matched by cv2.BFMatcher.knnMatch. Matches with distance smaller than *0.6* were used for warping.

5. 'align_sift.py' was run to align the two samples. Features of the images were detected by SIFT detector and matched by cv2.BFMatcher.knnMatch. Matches with distance smaller than *0.55* were used for warping.

## Results
The results are stored at the branch of "results". The results are described as below.

Matches and aligned result of method 1 are named as "matches_orb.jpg" and "aligned_orb.jpg" respectively.

Matches and aligned result of method 2 are named as "matches_075.jpg" and "aligned_075.jpg" respectively.

Matches and aligned result of method 3 are named as "matches_065.jpg" and "aligned_065.jpg" respectively.

Matches and aligned result of method 4 are named as "matches_060.jpg" and "aligned_060.jpg" respectively.

Matches and aligned result of method 5 are named as "matches_055.jpg" and "aligned_055.jpg" respectively.



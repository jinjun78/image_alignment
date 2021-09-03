# Aligning cross-sectional images of human skeletal muscle tissue biopsies using machine learning

Independent, stochastic clonal expansion of mtDNA mutations within single cells is thought to be the driver behind the progression of mitochondrial DNA (mtDNA) diseases. [Lawless et al. (2020)](https://doi.org/10.1098/rsob.200061) and [Piotrowicz (2020)](http://mito.ncl.ac.uk/clonexp/clonal_expansion/) describe our current, limited understanding of how clonal expansion occurs.

[Elson et al. (2002)](https://sci-hub.mksa.top/10.1016/s0960-8966(02)00047-0) captured a large number of serial sections from patients with mitochondrial disease, recording how mitochondrial function fluctuates along their length by visual inspection of a small proportion of the fibres in the sections.  Here, we re-imaged the same sections using a modern, high-resolution microscope and aim to automatically segment and quantify mitochondrial function using computer vision and machine learning approaches.

The reason we're interested in analysing these data is because we want to observe a) the pattern of heterogeneity in respiratory chain function between different fibres in muscle cross sections (this is already studied a lot by mitochondrial researchers) and b) how respiratory chain function varies along the length of individual fibres (this is much more unusual, in fact this is the only dataset that has been gathered to address this issue to date).

The first step in this analysis is to make the connection between the same fibres in adjacent section images, either by pixel or by fibre, either manually or automatically.  Note that in [Elson et al. (2002)](https://sci-hub.mksa.top/10.1016/s0960-8966(02)00047-0) alignment was carried out manually by fibre.  We hope to automate alignment to allow us to examine more fibres and to speed up the workflow.  We also hope to replace visual inspection of fibres with a quantitative measure of mitochondrial function, based on numerical analysis of the newly captured images.

## [Aligning raw images](./analysis_attempts/README.md)
Some attempts at automatically lining up pixels in images from adjacent serial sections using [OpenCV](https://opencv.org/).

## Usage
1. Fill in file names of reference image and target image, and the time of alignment in the ![main.py](main.py) file. Also change the name of output log file if needed.

2. Change the solution of preprocessing and the path of reference image in ![workflow](workflow.py) script by hashtag according to the alignment time.

3. Run ![main.py](main.py) file in python to make alignment of the images.

3. Output log is saved in text format. Aligned images and test alignments from different parameters are saved in path previously edited on ![workflow](workflow.py).

4. Run ![best_integrate](best_integrate.py) to save a new csv file of all the best alignments.

4. Run ![line_plot](line_plot.py) to plot lines plot of alignment time and correlation coefficient.

5. Run ![catplot](catplot.py) to plot a category plot of good matches percentage and max features.

## Directories
1. [analysis_attempts](analysis_attempts) inclueds the history of attempts of aligning images.

2. [original](original) includes original adjacent sectional images in the JPEG file format.

3. [align](align) includes scripts that used in the workflow.

4. [final_output](final_output) includes the the sources of final alignment in the dissertation.




from workflow import Worlflow
import sys


# '''All the output stored in a single text file as named.
#    Remember to change text file name each time.'''
sys.stdout = open("final_output/log1.txt", "w")

if __name__ == '__main__':
    ref = "S001.jpg"  # reference image file name
    im = "S002.jpg"          # target image file name
    time = 1                  # the time of alignment
    Worlflow(ref, im, time)  # automatic workflow of alignment

sys.stdout.close()

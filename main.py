from workflow import Worlflow
import sys

sys.stdout = open("final_output/log5.txt", "w")
if __name__ == '__main__':
    ref = "aligned_4_1000_0.1.jpg"
    im = "S004.jpg"
    time = 5
    Worlflow(ref, im, time)

sys.stdout.close()

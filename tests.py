#!/bin/python3
from time import sleep
from spout import ProgressBar

def __sleep(pb, duration):
    for _ in range(pb.stages):
        sleep(duration)
        pb.checkpoint()

def __test(color):
    pb = ProgressBar(width=30, pad=30, color=color)
    
    pb.begin(label="Cleaning Files", stages=10)
    __sleep(pb, 0)
    pb.end()

    pb.begin(label="Wiping Cache", stages=5)
    __sleep(pb, 1)
    pb.end()

    pb.begin(label="Performing Checks", stages=7)
    __sleep(pb, 0.1)
    pb.end()
    
    pb.begin(label="Finalizing Program", stages=10)
    __sleep(pb, 0.1)
    pb.end()

def main():
    # test driver
    __test(color=True)
    __test(color=False)

if __name__ == '__main__':
    main()

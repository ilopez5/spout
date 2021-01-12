#!/bin/python3
import time

# colors
_blue   = '\033[38;5;39m'
_yellow = '\033[38;5;226m'
_white  = '\033[m'

class ProgressBar():
    def __init__(self, stages, width=30, pad=20, color=True):
        self.progress = 0
        self.stages   = stages
        self.width    = width
        self.pad      = pad
        self.start    = time.perf_counter()
        self.current  = self.start
        self.label    = str()
        self.color    = color

    def checkpoint(self):
        assert(self.progress <= self.stages)
        self.current = time.perf_counter()
        self.progress += 1
        print(self, end="\r" if self.progress < self.stages else '')

    def begin(self, label):
        # reset if past usage was incomplete
        if self.progress:
            self.reset()
        self.label = label
        print(self, end='\r')

    def reset(self):
        self.progress = 0
        self.start    = time.perf_counter()
        self.current  = self.start
        self.label    = str()
        print("\n", end='')

    def _get_label(self):
        if self.color:
            return _yellow + self.label + _white
        return self.label

    def _get_bar(self, size):
        if self.color:
            return _blue + '#'*size + _white
        return '#'*size

    def __str__(self):
        size    = self.progress * (self.width // self.stages)
        prefix  = self._get_label() + '.' * (self.pad - len(self.label))
        used    = self._get_bar(size)
        free    = ' ' * (self.width - size)
        elapsed = round(self.current - self.start, 2)
        return f"{prefix}[{used}{free}] {elapsed:.2f}s"

def sleep(pb, duration):
    for _ in range(pb.stages):
        time.sleep(duration)
        pb.checkpoint()
    return

def test(color):
    pb = ProgressBar(stages=5, width=30, pad=30, color=color)
    
    pb.begin("Cleaning Files")
    sleep(pb, 0.2)
    pb.reset()

    pb.begin("Wiping Cache")
    sleep(pb, 0.5)
    pb.reset()

    pb.begin("Performing Checks")
    sleep(pb, 1)
    pb.reset()
    
    pb.begin("Finalizing Program")
    sleep(pb, 1.2)
    pb.reset()

def main():
    test(color=True)
    test(color=False)

if __name__ == '__main__':
    main()

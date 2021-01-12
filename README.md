[![Generic badge](https://img.shields.io/badge/Stage-v1.1-blue.svg)](#)

# SPOUT

## A Custom Python Progress Bar

There are many progress bar implementations out there, such as 
[progress2](https://pypi.org/project/progressbar2/) and 
[tdqm](https://pypi.org/project/tqdm/). However, I wanted to try my
hand at making one, and having it be independent of wrapping any Python 
iterable as the aforementioned libraries seem to do.

## Usage:
```python
pb = ProgressBar(width=30, pad=30, color=True)

pb.begin(label="Performing Operation 1", stages=10)
pb.checkpoint()
...
pb.checkpoint()
pb.end()

pb.begin(label="Performing Operation 2", stages=5)
...
pb.end()
```

## Configurations:
- `stages`- sets the number of stages to be completed for the bar (required)
- `width` - sets the width (in characters) of the progress bar
- `pad`   - sets the width (in characters) of the label + padding (e.g."Label...")
- `color` - allows for colored output vs uncolored.

## Example:
[![asciicast](https://asciinema.org/a/shtO7TgOfkMGdbeBdErE9LeHM.svg)](https://asciinema.org/a/shtO7TgOfkMGdbeBdErE9LeHM)

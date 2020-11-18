## Algorithm task

Write a program, that takes a number on the input and expresses all the different ways the input can be represented as the sum of 1,3 and 4 simultaneously.

## Solution

See implemented algorithm on [github - TBD!!!](https://git).

Code is written in Python 3.8, venv is created using Poetry. To launch the script, follow steps bellow:

``` sh
# create venv
poetry install

# activate venv
poetry shell

# run recursive algorithm
python recursion.py 8

# run iterative algorithm
python iteration.py 8
```

There are two implementations of the algorithm. First implementation is recursive - `recursion.py`. This implementation is more straightforward, however it is not optimal from the point of memory usage.

The second implementation is iterative - `iteration.py`. This implementation uses stack to remember path taken through the tree, so there is much lower memory usage. However the algorithm itself is not as straightforward.

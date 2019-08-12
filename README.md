# Game Of Life

A short (but quite inefficient) program to calculate Game Of Life generations.

## What is the Game of Life?
The Game of Life is a cellular automaton consisting of a collection of cells. Starting with an initial configuration (generation 0), each cell lives, dies or multiplies according to these rules:

For a space that is 'populated':
- Each cell with one or no neighbors dies from loneliness.
- Each cell with four or more neighbors dies from overpopulation.
- Each cell with two or three neighbors survives.

For a space that is 'empty':
- Each cell with three neighbors becomes populated.

## What does this do?

The output of the program will be the configuration after a specified number of generations.

## Input File

There is an example input GameOfLife.txt that can be referred to.

The first line of the text file should contain two integers ```r``` and ```c```, denoting rows and columns respectively, e.g.
```
9 9
```

The second line should contain the number of generations ```g```, e.g.
```
4
```

The next r lines should have c characters each, representing the initial configuration.
"." denotes a board with no living cells in it, while "x" denotes a board with a living cell in it.
Example:
```
.........
.........
....x....
...xxx...
...x.x...
....x....
.........
.........
.........
```



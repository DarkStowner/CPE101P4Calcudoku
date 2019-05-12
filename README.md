# CPE101P4Calcudoku

## CPE 101

## Project 4 - Calcudoku

Group of Two
Due: 5/22 for 100%
5/23 for 80%

# Purpose

To have more understanding on iteration (loop) and using multidimensional lists, as well as implementing
an exhaustive search algorithm.

# Description

For this program, you will be writing a solver for 5x5 Calcudoku puzzles. A Calcudoku puzzle is an NxN
grid where the solution satisfies the following:

● Each row can only have the numbers 1 through N with no duplicates

● Each column can only have the numbers 1 through N with no duplicates

● The sum of the numbers in a cage (areas with a bold border) should equal the number shown in the
upper left portion of the cage. (the upper left value in cage used for demonstration purpose.)
Puzzle sample input and output files can be downloaded from PolyLearn.

## Input File:

```
Puzzle input files are provided with the following format:
```
```
9
5 0 5
8 1 2 6
```

The first line contains the number of cages in the puzzle. After the first line, each subsequent line describes
a cage. The first number of a line is the sum of the values in the cage, and all numbers afterward refer to
the positions of the cells that make up the cage. In the puzzle, the cell positions are numbered starting with
0 for the upper left cell and increase by 1 from left- to right.

Input sample is shown below (Each line is in bold):
Number of cages: 9 => it means it will cover 25 cells from index 0 to index 24.
Cage number 0: 5 0 5 => it means for cage 0 the sum is 5, we have 2 cells, cell numbers 0 and 5
Cage number 1: 8 1 2 6
Cage number 2: 8 3 8
Cage number 3: 6 4 9 14
Cage number 4: 13 7 12 13
Cage number 5: 5 10 15
Cage number 6: 14 11 16 20 21
Cage number 7: 6 17 18 22
Cage number 8: 10 19 23 24

## Output

Your program should display a solution to the puzzle in the following format (This is output based on the
above input.)

### 4 1 2 5 3

### 1 5 4 3 2

### 2 3 5 4 1

### 3 4 1 2 5

### 5 2 3 1 4

# Implementation

## Solving a Puzzle

Your program will solve puzzles using an exhaustive search (or "brute force") approach, in which it tries
(potentially) all possible solutions until it finds the correct one. Your algorithm should perform the
following pseudocode:

1. Initialize all cells to 0
2. Increment the value in the current cell by 1 (starting from the top-left cell)
    a. If the incremented value is greater than the maximum possible value, set the current cell to
       0 and move back to the previous cell
    b. Otherwise, check if the number is valid. If so, continue to the next cell to the right
       (advancing to the next row when necessary)
3. Repeat Step 2 until the puzzle is fully populated and valid

In order for this algorithm to work, you will need to write functions to test if a puzzle is in a valid state. As
you populate the puzzle with numbers, it becomes invalid if:

```
● Duplicates exist in any row or column
● The sum of values in a fully populated cage does not equal the required sum
```

```
● The sum of values in a partially populated cage equals or exceeds the required sum
```
## Minimum Required Program Structure

In the function headers below, the parameter grid refers to a 2D list of integers representing the cells of the
puzzle and cages refers to a 2D list of integers representing the values read from input. Some suggested
functions:

```
1) In calcudoku.py you at least have a main function.
```
## main()

The main function (with optional helper functions) should perform the following steps:

```
● Store the data from the puzzle input file in a 2D list of integers
● Create a 5x5 grid using a 2D list and fill it with zeros
● Use a single while loop to validly populate every cell in the grid
● Count all checks and backtracks for terminal output at the end
```
```
2) In func_calcudoku.py, the following functions are suggested:
```
## transpose (grid)

Return the transposition of the given grid. Assume that the grid has a square number of elements but make
assumptions about the actual size.

## validate_all (grid, cages)

Return True if all 3 validation functions below return True and False otherwise.

## validate_rows (grid)

Return True if all rows contain no duplicate positive numbers and False otherwise.

## validate_cols (grid)

Return True if all columns contain no duplicate positive numbers and False otherwise. It is recommended
that you transpose the grid (convert its rows to columns and columns to rows) and pass this transposition
to validate_rows to reuse your existing code.

## validate_cages (grid, cages)

Return True if the sum of values in a fully populated cage equals the required sum or the sum of values in
a partially populated cage is less than the required sum and False otherwise.

# Testing

## 3) In tests.py You are required to write at least 3 tests for each function (except main). Since we are

```
emphasizing test-driven development, you should write tests for each function first. In doing so,
you will have a better understanding as to what the functions take as input and produce as output,
which makes writing the function definitions easier.
```
Each puzzle can be found in a separate file:
test1_in.in, test2_in.in, test3_in.in


Your program should be run using:
python3 calcudoku.py < test1_in.in

You should compare your output with the corresponding output files using diff (without the use of any
flags):

test1_out.out, test2_out.out, test3_out.out

# Submission

Submit your .py files and a pdf file in the PolyLearn:
1) calcudoku.py
2) func_calcudoku.py
3) tests.py
4) Readme.pdf file that includes responsibility of each member and Pseudocode for each function.

# Rubric:

```
1) Implementation of functions without error. 10 Points
2) Main program runs without error 10 Points
3) Test cases (3 for each function except main) 5 Points
4) Signature purpose statement for each function 5 Points
5) Pseudocode (pdf file) 10 Points
6) 6 input files for testing the program (each 10 points) 60 Points
```


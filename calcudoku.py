# Project 4
#
# Name: Nathan Tang and Jules Hajjar
# Instructor: Sussan Einakian
# Section: 06

from solverFuncs import *
def main():
    puzzle=[[0 for i in range(5)] for j in range(5)]
    cage_list = getcages()
    col = 0
    row = 0
    trial = 0

    while row < 5:
        puzzle[row][col] += 1
        trial += 1
        if allCheck(puzzle,cage_list):
            col += 1
            if col == 5:
                col = 0
                row += 1
        elif puzzle[row][col] == 5:
            while puzzle[row][col] == 5:
                puzzle[row][col] = 0
                col -= 1
                if col < 0 :
                    col = 4
                    row -= 1
    displayPuzzle(puzzle)
if __name__ == '__main__':
   main()

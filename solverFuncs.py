def getcages():
    cage_count=input()
    cage_list=[]
    for i in range(0,int(cage_count)):
        cage_string=input()
        cage_list.append(cage_string.split())
        for j in range(0,len(cage_list[i])):
            cage_list[i][j] = int(cage_list[i][j])
    return cage_list

def displayPuzzle(puzzle2D):
    puzzle = []
    for i in puzzle2D:
        for j in i:
            puzzle.append(j)
    puzzle_line = ""
    for j in range(0, len(puzzle),5):
        for i in range(j,j+5):
            puzzle_line += str(puzzle[i])
            puzzle_line += " "
        print(puzzle_line)
        puzzle_line = ""

def rowsCheck(puzzle):
    for i in range(5):
        for j in range(5):
            if puzzle[i].count(puzzle[i][j]) > 1 and puzzle[i][j] != 0:
                return False
    return True

def colsCheck(puzzle):
    for j in range(5):
        col=[]
        for i in range(5):
            col.append(puzzle[i][j])
            if col.count(puzzle[i][j]) > 1 and puzzle[i][j] != 0:
                return False
    return True

def cagesCheck(puzzle,cage_list):
    for cage in cage_list:
        values_list=[]
        for num in cage[1:]:
            values_list.append(puzzle[num//5][num%5])
        if (sum(values_list) != cage[0] and 0 not in values_list) or (0 in values_list and sum(values_list) >= cage[0]):
            return False
    return True

def allCheck(puzzle,cage_list):
    return cagesCheck(puzzle,cage_list) and colsCheck(puzzle) and rowsCheck(puzzle)

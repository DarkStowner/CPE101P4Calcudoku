# Project 4
#
# Name: Nathan Tang and Jules Hajjar
# Instructor: Sussan Einakian
# Section: 06

#this function gets the input from user and creates a 2d made of
#x elements (also specified in input) list with the following structure :
#[[cage_sum,cellindex1,cellindex2,...],[cage_sum,...],...]
def getcages():
    cage_count=input()#first input is number of cages
    cage_list=[]
    for i in range(0,int(cage_count)):#we run this loop as many times as there are cages
        cage_string=input()#the following input is given as string
        cage_list.append(cage_string.split())#creates the 2D list with the structure mentioned above, splits the string into a list beforehand
        for j in range(0,len(cage_list[i])):
            cage_list[i][j] = int(cage_list[i][j])
    return cage_list#the index of each sub-list is the cage number in this output

##################################################################
#Print "Puzzle:"
#Print the puzzle string, going back to the next line every 5 number
##################################################################

#Takes the string puzzle as an input and prints a formatted version of 5x5 numbers
#string -> void
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

##################################################################
#1. Create an empty list newPuzzle
#2. Put the puzzle string in the list splitting the entries every 5 number
#Repeat step 2 5 times to end up with a list of 5 entries of 5 numbers representing the 5 lines of the puzzle
##################################################################

#Create 2D list on puzzle line by line
#string -> list
def puzzle2D(puzzle):
    newPuzzle = [] #create empty list
    for row in range(0,25,5): #repeat 5 times
        leftright_puzzle = puzzle[row:row+5:1] #create new list containing one line of 5 numbers of puzzle
        newPuzzle.append(leftright_puzzle) #append every line of puzzle to new list cointaining all lines in order one by one
    return newPuzzle #return that new list

def validate_row(puzzle,row):
    if len(set(puzzle[row])) < 5  and (0 in set(puzzle[row])):#set() does not allow duplicates
        return False
    return True


#Checks lines of the puzzle and compares
def validate_rows(puzzle):
    for i in range(len(puzzle)):
        if len(set(puzzle[i])) < 5:#set() does not allow duplicates
            return False
        else:
            continue
    return True

def validate_cols(puzzle):
    col=[]
    cols=[]
    for k in range(0,5):
        col=[]
        for j in range(0,5):
            col.append(puzzle[j][k])
        cols.append(col)
    for i in range(len(cols)):
        if len(set(cols[i])) < 5:#set() does not allow duplicates
            return False
        else:
            continue
    return True

def validate_cage(cellidx,cage_list,puzzle):
    sum = 0
    for i in range(len(cage_list)):
        for j in range(1,len(cage_list[i])):
            if cellidx == cage_list[i][j]:
                cageidx = i
                for g in range(1,len(cage_list[i])):#loop for every cell of the cage
                    sum+=puzzle[cage_list[i][g]]#add the given cells values together (via index lookup of puzzle)
                if sum <= cage_list[i][0]:
                    sum=0
                    return True
    return False#return false immediately if not completed

def validate_cages(puzzle2D,cage_list):
    puzzle = []
    for i in puzzle2D:
        for j in i:
            puzzle.append(j)
    for i in range(len(cage_list)): #loop for every cage
        sum=0
        for j in range(1,len(cage_list[i])):#loop for every cell of the cage
            sum+=puzzle[int(cage_list[i][j])]#add the given cells values together (via index lookup of puzzle)
        if sum == cage_list[i][0]:
            sum=0
            continue#continue if that cage's condition has been fulfilled
        else:
            return False#return false immediately if not completed
    return True

def validate_all(puzzle,cages):
    if (validate_cages(puzzle,cages) == True) and (validate_rows(puzzle) == True) and (validate_cols(puzzle) == True):
        return True
    else:
        return False

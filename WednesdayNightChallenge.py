# TASK 1
# given a 5x5 grid, add the last column and row, then flip the card at the
# coordinate specified by the user
five_by_five_grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','X','X'],
    ['X','0','0','X','X'],]

# first step is to add colum 6 and row 6
def pretty (grid):
    #go through rows in list
    #assume that the lenth of the first row, is the number of the columns.
    for r in range(0,len(grid)): 
        for c in range(0,len(grid[0])):
            print(five_by_five_grid[r][c], end=' ')
        print('')
    #go through col in list
    #print index

def is_an_X(input):
    return input == 'X'


#This funciton calculates if the number of Xs is odd or even. Then provides the required rows and column to correct 
def find_error(grid):
    #create blank lists to use has counters
    counter_r=[0 for d in range(0, len( grid[1]) ) ]
    counter_c=[0 for d in range(0,len(grid) ) ]

    #go through rows
    for row in range(0,len(grid) ):
        #go through the colmmns
        for col in  range(0, len( grid[1]) ):
            if grid[row][col] == 'X':
                counter_r[row] += 1
                counter_c[col] += 1
        if  counter_r[row]%2 == 0:
            new  ='0'
        else:
            new = 'X'
        counter_r[row]=new

    #make the column counter jsut be Xs and 0s too.
    for col in range(0,len(grid[1])):
        if counter_c[col] %2 == 0:
            counter_c[col]="0"
        else:
            counter_c[col]="X"

    return (counter_r, counter_c)

#This function adds a row and a column to the right and bottom or a gird, so that the number of Xs in each row and column is even.
def append_grid(grid,counter_r, counter_c):
    
    for row in range(0,len(grid)):
        grid[row].append(counter_r[row])

    #since the for loop above added one more column to the grid, add another item to the column counter.
    no_of_Xs= sum(is_an_X(x) for x in counter_r)
    if no_of_Xs %2 ==0:
        new = 0
    else:
        new='x'
    counter_c.append(new)
    grid.append(counter_c)
    return grid

# This function allows a user to 'flip' one of the items in a grid.  Ie if it was X then it turns into a 0.
def flip(grid):
    print("This is what the grid currently looks like.")
    pretty(grid)
    flip_val=input('please enter co-ordinates to flip, row, col:')
    row= int(flip_val[0])
    col = int(flip_val[2])
    print(grid[row][col])
    print(grid[row][col]=="X")

    if grid[row][col] == "X":
        print('it was true')
        grid[row][col] = "0"
    else:
        grid[row][col] = "X"
        print('it was false')
    print("This is what the changed grid looks like")
    pretty(grid)
    return grid

#This function is to find the co-ordinates of a 'flip' in the grid.
def correct_grid(grid):
    #Use a previous function which puts Xs to indicate where the grid's rows and columns have an odd number of Xs
    #Where the function returns an X, it means there is an odd number of Xs in that row or col
       
    (counter_r, counter_c)=find_error(grid)
    print(counter_r)
    print(counter_c)

    if counter_r.count('X') == 0 and counter_r.count('X') == 0:
        print("No errors were found in your grid")
        return grid

    row=counter_r.index("X")
    col=counter_c.index("X")

    print("There was an error at row", row, ", column ", col)
    print("The grid now looks like this"
    if grid[row][col] == "X":
        grid[row][col] = "0"
    else:
        grid[row][col] = "X"
    
    
    pretty(grid)
    return grid
    

#TASK 1

pretty(five_by_five_grid)

print  (find_error(five_by_five_grid))
(counter_r, counter_c) = find_error(five_by_five_grid)
new_grid = append_grid(five_by_five_grid,counter_r, counter_c)
pretty(new_grid)


#TASK 2
# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)
# output the grid with the flipped card
flipped_grid = flip(new_grid)

# Task 3
#This is a bonus task I made for myself.
correct_grid(flipped_grid)
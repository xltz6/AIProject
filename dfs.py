#generate 4*4 grid
grid = {}
for row in range(1,5):
    for column in range(1,5):
        grid[(row, column)] = 0
        
#set dirty position
grid[(1,2)] = 1
grid[(1,4)] = 1
grid[(2,2)] = 1
grid[(2,3)] = 1
grid[(3,1)] = 1
grid[(4,2)] = 1
grid[(4,4)] = 1
#print out the grid 
for row in range(1,5):
    for column in range(1,5):
            print [row,column],':',grid[(row, column)]

#global variable if find the dirty set it to 1 and when state chages set it back to 0 
found = 0
#global variable for path cost
cost = 0
#global variable for solution path
path = []
#global variable for visited set
visited = []
#global variable set for record the visited node and use for tracing back
traceback = []
#global variable for record the row number of dirty position
newrow = 0
#global variable for record the column number of dirty position
newcol = 0


def dfs_clean(grid,dirty,startrow,startcol):
    global found
    global newrow
    global newcol
    global visited
    #path for start position
    path.append([startrow,startcol])
    newrow = startrow
    newcol = startcol
    #run dfs each time found a dirty position and clean the visited set, finished when all dirts are cleaned
    while dirty != 0:
        found = 0
        print(dirty)
        visited = []
        dfs(grid, newrow, newcol)
        dirty -= 1
    return


#dfs graph search
def dfs(grid, startrow, startcol):
    global visited
    global traceback
    global found
    global count
    global newrow
    global newcol
    if [startrow, startcol] in visited:
        return
    #add visited position and traced path
    visited.append([startrow, startcol])
    traceback.append([startrow, startcol])
    #visited 5 state according to tie-breaking rule: up, left, stay for sucking, right, down
    for [row,col] in [[r,c] for [r,c] in [startrow-1,startcol],[startrow,startcol-1],[startrow, startcol],[startrow,startcol+1],[startrow+1,startcol] if 1 <= r <= 4 and 1 <= c <= 4 and ([r,c] not in visited or [r,c] == visited[-1])]:
        print(row,col)
        if found == 0:
            #if for current node, there is no up state and left state choice right now
            if(row == startrow and col == startcol):
                #check if it is dirty 
                if(grid[(row, col)] == 1):
                    #if it is dirty,staying for sucking 
                    path.append([row,col])
                    #chang position to clean
                    grid[(row, col)] = 0
                    #set found dirty flag to 1
                    found = 1
                    #record the dirty position and state changes
                    newrow = row
                    newcol = col
                    print("dirty place")
                    print(newrow, newcol)
                    print("-----------")
            else:
                #if current node has up, left choices
                path.append([row,col])
                dfs(grid,row, col)
        
                
        if found == 1:
            #go to states that we don't need
            dfs(grid, row, col)
    if found == 0:  
        #print(traceback)
        #trace back if it has all surround position visited
        traceback.pop()
        if traceback:
            path.append(traceback[-1])
    #print(traceback.pop())
    return 

        
        
        

#counting how many dirty positions in the grid
dirty = 0
for row in range(1,5):
        for column in range(1,5):
            if(grid[(row, column)]) == 1 :
                dirty = dirty + 1

                
#call clean function
dfs_clean(grid,dirty, 3, 2)

#print path
print 'The solution path should be :',path 
#print path cost
print(len(path))
i = 0
while i < len(path)-1:
    a = path[i]
    b = path[i+1]
    if (a[0] - b[0]) == 0:
        if (a[1] - b[1]) != 0:
            cost += 1.3
    else:
        cost += 1
    i += 1
print 'The path cost should be:',cost



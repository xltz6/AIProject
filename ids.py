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
print grid


#global variable for solution path
path = []
nodes = []
solution = []
found = 0
newrow = 0
newcol = 0
cost = 0

def ids_clean(grid,dirty,startrow,startcol):
    global found
    global newrow
    global newcol
    global solution

    newrow = startrow
    newcol = startcol
    solution.append([newrow, newcol])
    #run ids each time found a dirty position and clean the visited set, finished when all dirts are cleaned
    while dirty != 0:
        found = 0
        print "dirty number:",dirty
        ids(grid, newrow, newcol)
        dirty -= 1
    return

def ids(grid, startrow, startcol):
    global path
    #for 4*4 grid, run ids the maxDepth is 4, which means the iteration could be 4
    for maxDepth in range(1,5):
        #each iteration,ids create a tree, but only the last one is we need
        path = []
        dfs(grid,startrow,startcol,maxDepth)
        
        
def dfs(grid,startrow,startcol,maxDepth):
    global found
    global newrow
    global newcol
    global path
    global nodes
    global solution
    #each time run dfs the mexDepth minus 1 until it equals 0 return
    if maxDepth <= 0:
        return
    for [row,col] in [[r,c] for [r,c] in [startrow-1,startcol],[startrow,startcol-1],[startrow, startcol],[startrow,startcol+1],[startrow+1,startcol] if 1 <= r <= 4 and 1 <= c <= 4]:
        nodes.append([row, col])
        if found == 0:
            #if for current node, there is no up state and left state choice right now
            if(row == startrow and col == startcol):
                path.append([row, col])
                #check if it is dirty 
                if(grid[(row, col)] == 1):
                    #if it is dirty,staying for sucking
                    solution = solution + path
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
                path.append([row, col])
                dfs(grid,row, col,maxDepth-1)
            #find the only path to the dirty place, pop out the nodes that we don't need
            path.pop()
        
        if found == 1:
            #go to states that we don't need
            dfs(grid, row, col, maxDepth-1)

    return 
    
    

#counting how many dirty positions in the grid
dirty = 0
for row in range(1,5):
        for column in range(1,5):
            if grid[(row, column)] == 1:
                dirty = dirty + 1
ids_clean(grid,dirty, 3, 2)

#print out the first 10 nodes to expand
n = 0
print "the first 10 nodes to expand:"
while n < 10:
    print(nodes[n])
    n += 1

#print the solution path
print 'The solution path should be :',solution
print(len(solution))

#count for path cost
i = 0
while i < len(solution)-1:
    a = solution[i]
    b = solution[i+1]
    if (a[0] - b[0]) == 0:
        if (a[1] - b[1]) != 0:
            cost += 1
    else:
        cost += 1.3
    i += 1
print 'The path cost should be:',cost
    
    
#function iterativeDeepeningDepthFirstSearch(node) {
#    // Repeatedly depth-first search up-to a maximum depth of 6.
#    for (var maxDepth = 1; maxDepth < 6; maxDepth++) {
#        depthFirstSearch(node, maxDepth);
#    }
#}
#
#function depthFirstSearch(node, maxDepth) {
#    // If reached the maximum depth, stop recursing.
#    if (maxDepth <= 0) {
#        return;
#    }
#
#    // Recurse for all children of node.
#    for (var i=0, c=node.children.length; i<c; i++) {
#        depthFirstSearch(node.children[i], maxDepth-1);
#    }
#}
    
    
    
    
    
    
    
    
    
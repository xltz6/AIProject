from threading import Timer
import thread, time, sys
def timeout():
    thread.interrupt_main()

# generate 4*4 grid
grid = {}
for row in range(1, 6):
    for column in range(1, 7):
        grid[(row, column)] = 0
# set dirty position
grid[(1, 2)] = 1
grid[(1, 4)] = 1
grid[(1, 6)] = 1
grid[(2, 1)] = 1
grid[(2, 3)] = 1
grid[(2, 4)] = 1
grid[(3, 1)] = 1
grid[(3, 5)] = 1
grid[(3, 6)] = 1
grid[(4, 2)] = 1
grid[(4, 4)] = 1
grid[(5, 3)] = 1
grid[(5, 4)] = 1
grid[(5, 6)] = 1
print grid

# global variable for solution path
path = []
nodes = []
solution = []
found = 0
dirty = 0
cost = 0
maxDepth = 0
count = 0


# Timeout a long running function with the default expiry of 10 seconds.
# @timeout(30, os.strerror())
def ids_clean(grid, startrow, startcol):
    global path
    global maxDepth
    global dirty
    global count
    global solution

    #until found all the nodes in one iteration, maxDepth add 1 each time which means the ids tree go one deep level
    while found == 0:
        #go dfs each iteration, each iteration restart to find dirty position
        depth = 0
        solution = []
        print "limit:", maxDepth
        count = dirty
        nodes.append([startrow, startcol])
        dfs(grid, startrow, startcol, depth)
        maxDepth += 1
    return
    time.sleep(1)

def dfs(grid, startrow, startcol, depth):
    global found
    global dirty
    global path
    global nodes
    global solution
    global count

    #if the depth of dfs search,
    if depth >= maxDepth:
        return
    for [row, col] in [[r, c] for [r, c] in [startrow - 1, startcol], [startrow, startcol - 1], [startrow, startcol], [startrow, startcol + 1], [startrow + 1, startcol] if 1 <= r <= 5 and 1 <= c <= 6]:
        #nodes.append([row, col])
        print([row, col])
        if found == 0:
        # if for current node, there is no up state and left state choice right now
            if (row == startrow and col == startcol):
                nodes.append([row, col])
                path.append([row, col])
                # check if it is dirty
                if (grid[(row, col)] == 1):
                    # if it is dirty,staying for sucking
                    solution = solution + path
                    # chang position to clean
                    grid[(row, col)] = 0
                    # set found dirty flag to 1
                    count -= 1
                    if count == 0:
                        found = 1
                    print("dirty place")
                    print(row, col)
                    print("-----------")
            else:
                # if current node has up, left choices
                nodes.append([row, col])
                path.append([row, col])
                dfs(grid, row, col, depth + 1)

            #find the only path to the dirty place, pop out the nodes that we don't need
            path.pop()
        else:
            dfs(grid, row, col, depth + 1)



    return


# counting how many dirty positions in the grid
dirty = 0
for row in range(1, 6):
    for column in range(1, 7):
        if grid[(row, column)] == 1:
            dirty = dirty + 1

try:
    Timer(1800, timeout).start()
    ids_clean(grid, 3, 2)
except:
    print(len(nodes))
#ids_clean(grid, 3, 2)



# print out the first 10 nodes to expand
n = 0
print "the first 10 nodes to expand:"
while n < 10:
    print(nodes[n])
    n += 1

# print the solution path
print 'The solution path should be :', solution
print(len(solution))

# count for path cost
i = 0
while i < len(solution) - 1:
    a = solution[i]
    b = solution[i + 1]
    if (a[0] - b[0]) == 0:
        if (a[1] - b[1]) != 0:
            cost += 1
    else:
        cost += 1.3
    i += 1
print 'The path cost should be:', cost

# function iterativeDeepeningDepthFirstSearch(node) {
#    // Repeatedly depth-first search up-to a maximum depth of 6.
#    for (var maxDepth = 1; maxDepth < 6; maxDepth++) {
#        depthFirstSearch(node, maxDepth);
#    }
# }
#
# function depthFirstSearch(node, maxDepth) {
#    // If reached the maximum depth, stop recursing.
#    if (maxDepth <= 0) {
#        return;
#    }
#
#    // Recurse for all children of node.
#    for (var i=0, c=node.children.length; i<c; i++) {
#        depthFirstSearch(node.children[i], maxDepth-1);
#    }
# }







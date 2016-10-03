import time

# generate 4*4 grid
grid = {}
for row in range(1, 5):
    for column in range(1, 5):
        grid[(row, column)] = 0

# set dirty position
grid[(1, 2)] = 1
grid[(1, 4)] = 1
grid[(2, 2)] = 1
grid[(2, 3)] = 1
grid[(3, 1)] = 1
grid[(4, 2)] = 1
grid[(4, 4)] = 1

# global variable if find the dirty set it to 1 and when state chages set it back to 0
found = 0
# global variable for path cost
cost = 0
# global variable for solution path
path = []
# global variable for visited set
visited = []
# global variable set for record the visited node and use for tracing back
nodes = []
# global variable for record the row number of dirty position
newrow = 0
# global variable for record the column number of dirty position
newcol = 0


def astar_clean(grid, dirty, startrow, startcol):
    global found
    global newrow
    global newcol
    global visited
    # path for start position
    path.append([startrow, startcol])
    newrow = startrow
    newcol = startcol
    # run astar each time found a dirty position and clean the visited set, finished when all dirts are cleaned
    while dirty != 0:
        found = 0
        print(dirty)
        visited = []
        astar(grid, newrow, newcol)
        dirty -= 1
    return


#atar graph search
def astar(grid, startrow, startcol):
    global visited
    global traceback
    global found
    global count
    global newrow
    global newcol
    if [startrow, startcol] in visited:
        return
    # add visited position and traced path
    visited.append([startrow, startcol])

    # next step can go 5 state according to tie-breaking rule: up, left, stay for sucking, right, down
    # run calculate_next() to calculate the minimum cost.
    # f() = g() + h(), g() could be the cost to next step(up, down cost 1.3, left, right cost 1, suck costs 0)
    # and f() could be the manhattan distance to the dirt
    next = calculate_next(startrow, startcol)
    for [row, col] in next:
        if found == 0:
            if (row == startrow and col == startcol):
                if (grid[(row, col)] == 1):
                    # sucking
                    path.append([row, col])
                    nodes.append([row, col])
                    # chang position to clean
                    grid[(row, col)] = 0
                    # set found dirty flag to 1
                    found = 1
                    # record the dirty position and state changes
                    newrow = row
                    newcol = col
                    print("dirty place")
                    print(newrow, newcol)
                    print("-----------")

            else:
                # if current node has up, left choices
                if ([row, col] not in visited):
                    path.append([row, col])
                    nodes.append([row, col])
                    astar(grid, row, col)

        if found == 1:
            # go to states that we don't need
            astar(grid, row, col)
    if found == 0:
        # trace back if it has all surround position visited
        path.pop()
        if path:
            nodes.append(path[-1])
    return

#calculate the minimum cost for next step
def calculate_next(startrow,startcol):
    global visited
    cost = []
    node = []
    if grid[(startrow, startcol)] == 1:
        for [row, col] in [[r, c] for [r, c] in [startrow - 1, startcol], [startrow, startcol - 1], [startrow, startcol], [startrow, startcol + 1], [startrow + 1, startcol] if 1 <= r <= 4 and 1 <= c <= 4 and ([r, c] not in visited or [r, c] == visited[-1])]:
            if row == startrow - 1 and col == startcol:
                up = 1.3 + manhattan(row, col)
                cost.append(up)
                node.append([row, col])
            if row == startrow and col == startcol - 1:
                left = 1 + manhattan(row, col)
                cost.append(left)
                node.append([row, col])
            if row == startrow and col == startcol:
                suck = 0 + manhattan(row, col)
                cost.append(suck)
                node.append([row, col])
            if row == startrow and col == startcol + 1:
                right = 1 + manhattan(row, col)
                cost.append(right)
                node.append([row, col])
            if row == startrow + 1 and col == startcol:
                down = 1.3 + manhattan(row, col)
                cost.append(down)
                node.append([row, col])
            for i in range(len(cost)):
                for j in range(0, len(cost) - i - 1):
                    if cost[j] > cost[j + 1]:
                        cost[j], cost[j + 1] = cost[j + 1], cost[j]
                        node[j], node[j + 1] = node[j + 1], node[j]
    else:
        for [row, col] in [[r, c] for [r, c] in [startrow - 1, startcol], [startrow, startcol - 1], [startrow, startcol + 1], [startrow + 1, startcol] if 1 <= r <= 4 and 1 <= c <= 4 and [r, c] not in visited]:
            if row == startrow - 1 and col == startcol:
                up = 1.3 + manhattan(row, col)
                cost.append(up)
                node.append([row, col])
            if row == startrow and col == startcol - 1:
                left = 1 + manhattan(row, col)
                cost.append(left)
                node.append([row, col])
            if row == startrow and col == startcol + 1:
                right = 1 + manhattan(row, col)
                cost.append(right)
                node.append([row, col])
            if row == startrow + 1 and col == startcol:
                down = 1.3 + manhattan(row, col)
                cost.append(down)
                node.append([row, col])
        for i in range(len(cost)):
            for j in range(0, len(cost) - i - 1):
                if cost[j] > cost[j + 1]:
                    cost[j], cost[j + 1] = cost[j + 1], cost[j]
                    node[j], node[j + 1] = node[j + 1], node[j]
    print(node)
    return node

#find the minimum manhattan distance of all dirts from current node
def manhattan(r,c):
    list = []
    short_cost = 11
    for row in range(1, 5):
        for column in range(1, 5):
            if (grid[(row, column)]) == 1:
                list.append([row, column])
    i = 0
    while i < len(list):
        print([list[i][0], list[i][1]])
        print([r, c])
        cost = abs(list[i][0] - r) + abs(list[i][1] - c)
        if cost == short_cost:
            short_cost = cost
        else:
            short_cost = min(short_cost, cost)
        i += 1
    return short_cost


# counting how many dirty positions in the grid
dirty = 0
for row in range(1, 5):
    for column in range(1, 5):
        if (grid[(row, column)]) == 1:
            dirty = dirty + 1

start_time = time.time()
# call clean function
astar_clean(grid, dirty, 3, 2)

# print first 10 nodes to expand
n = 0
print "the first 10 nodes to expand:"
while n < 10:
    print(nodes[n])
    n += 1
# print path
print 'The solution path should be :', path
# print path cost
print(len(path))
i = 0
while i < len(path) - 1:
    a = path[i]
    b = path[i + 1]
    if (a[0] - b[0]) == 0:
        if (a[1] - b[1]) != 0:
            cost += 1
    else:
        cost += 1.3
    i += 1
print 'The path cost should be:', cost

print("--- %s seconds ---" % (time.time() - start_time))
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


# class node:
#     def __init__(self, row, col, cost):
#         self.row = row
#         self.col = col
#         self.cost = cost
#
#     def __repr__(self):
#         return repr((self.row, self.col, self.cost))

def calculate(startrow,startcol):
    node = []
    cost = []
    if (grid[(startrow, startcol)] == 1):
        for [row, col] in [[r, c] for [r, c] in [startrow - 1, startcol], [startrow, startcol - 1], [startrow, startcol], [startrow, startcol + 1], [startrow + 1, startcol] if 1 <= r <= 5 and 1 <= c <= 6 ]:
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
        print(node)
        return node
    else:
        for [row, col] in [[r, c] for [r, c] in [startrow - 1, startcol], [startrow, startcol - 1], [startrow, startcol + 1], [startrow + 1, startcol] if 1 <= r <= 5 and 1 <= c <= 6 ]:
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

def manhattan(r,c):
    list = []
    short_cost = 8
    for row in range(1, 5):
        for column in range(1, 5):
            if (grid[(row, column)]) == 1:
                list.append([row,column])
    i = 0
    while i < len(list):
        print([list[i][0],list[i][1]])
        print([r,c])
        cost = abs(list[i][0] - r) + abs(list[i][1] - c)
        if cost == short_cost:
            short_cost = cost
        else:
            short_cost = min(short_cost, cost)
        i += 1
    print short_cost
    return short_cost
calculate(3,2)




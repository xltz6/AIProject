#import random
from copy import deepcopy
import time
from functools import wraps

class Room:
    parent = []
    room = []
    dirt = 0
    g = 0
    f = 0
    closed = False
    
    def __init__(self,room):
        self.room = room
    
    def __str__(self):
        return str(self.room)
    __repr__ = __str__

class Grid:
    rooms = {} #Should be a dictionary (x,y):Node
    width = 0
    height = 0
    dirt_count = 7
    start = 0
    stop = 0
    closelist = []
    openlist = []
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

#timer
def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s ms" %
               (function.func_name, str((t1-t0)*1000))
               )
        return result
    return function_timer

#generate a Grid obj, inits each room to 0 with the given dimensions and returns it
def generate_grid(height, width):
    grid = Grid(height, width)
    
    for row in range(1,height+1):
        for column in range(1,height+1):
            grid.rooms[(row, column)] = Room([row, column])
            #grid.room[(row,column)]
    dirty_rooms(grid)
    return grid

def dirty_rooms(grid):    
    #set dirty position
    grid.rooms[(1,2)].dirt = 1
    grid.rooms[(1,4)].dirt = 1
    grid.rooms[(2,2)].dirt = 1
    grid.rooms[(2,3)].dirt = 1
    grid.rooms[(3,1)].dirt = 1
    grid.rooms[(4,2)].dirt = 1
    grid.rooms[(4,4)].dirt = 1

def display_grid(grid):
    #print out the grid
    height = grid.height
    width = grid.width
    
    for row in range(1,height+1):
        for column in range(1,width+1):
                print [row,column], ':', grid.rooms[(row, column)]

    
#g - +1:left or right, +1.3:up or down, 0:suck
#h - +number of dirty rooms
#def astar(grid, startrow, startcol):
#should choose the option that reduces the number of dirt first
#if no option to reduce dirt is available, pick the cheapest route    
#while len openl != 0:
#find the node with the least cost

def get_neighbors(r_coord, g):
    neighbors = {}
    #print neighbors
    rx = r_coord[0]
    ry = r_coord[1]
    room = 0
    #print r_coord
    #UP: r - 1
    if rx != 1:
        room = deepcopy(g.rooms[rx-1,ry])
        g.rooms[rx-1,ry].parent = [rx, ry]
        room.parent = [rx, ry]
        #print g.rooms[rx-1,ry].parent
        neighbors["UP"] = room
    #DOWN: r+1
    if rx != g.height:
        room = deepcopy(g.rooms[rx+1,ry])
        g.rooms[rx+1,ry].parent = [rx, ry]
        room.parent = [rx, ry]
        #print g.rooms[rx+1,ry].parent
        neighbors["DOWN"] = room
    #LEFT: c-1
    if ry != 1:
        room = deepcopy(g.rooms[rx,ry-1])
        g.rooms[rx,ry-1].parent = [rx, ry]
        room.parent = [rx, ry]
        #print g.rooms[rx,ry-1].parent
        neighbors["LEFT"] = room
    #RIGHT: c+1
    if ry != g.width:
        room = deepcopy(g.rooms[rx,ry+1])
        g.rooms[rx,ry+1].parent = [rx, ry]
        room.parent = [rx, ry]
        #print g.rooms[rx,ry+1].parent
        neighbors["RIGHT"] = room
    
    return neighbors

def by_cost(a,b):
    if a.f < b.f: #a cheaper b
        #print str(a.room) + " cheaper than " + str(b.room)
        return 1
    elif a.f == b.f: #cost =
        #print str(a.room) + " cost = cost of " + str(b.room)
        if a.room[0] == b.room[0]: #a,b same row
            if a.room[1] < b.room[1]: # dif cols
                return 1 #don't switch
            else:
                return -1 #do switch
        elif a.room[0] > b.room[0]: #dif rows
            return -1
        else:
            return 1
    
    return -1

def backtrack(g):
    path = []
    end = g.closelist.pop()
    print "start -> %s"%g.start.room
    for n in g.closelist:
        path.append([n.parent,n])
        
    return path
        

@fn_timer
def astar():
    print "A* Search:\n"
    g = generate_grid(4,4)
    g.start = Room([3,2])
    g.start.f = 0
    g.openlist.append(g.start)
    
    #HW related data
    count = 1
    
    while len(g.openlist) != 0 and g.dirt_count > 0:
        #pop q off the open list
        node = g.openlist.pop()
        
        #clean if dirty
        if node.dirt == 1:
            node.dirt = 0
        
        #if there is dirt suck
        if g.rooms[node.room[0],node.room[1]].dirt == 1:
#            print str(node.room) + " is cleaned"
            g.rooms[node.room[0],node.room[1]].dirt = 0
            g.dirt_count -= 1
#            print "Dirt count = %d" % g.dirt_count
        
        #get neighbors
        neighbors = get_neighbors(node.room, g)
        
        #Print first 10 expanded nodes
        if count <= 10:
            print "Node %s" % node.room + " was expanded"
        
        #itterate through successors
        for n in neighbors.keys():
            if g.dirt_count == 0: #reached the goal
                break; 
                
            #h = g.dirt_count

            h = g.dirt_count
                
            if n == "UP" or n == "DOWN":
                neighbors[n].f = (node.f + 1.3 + h)
                neighbors[n].g = node.f + 1.3
            if n == "LEFT" or n == "RIGHT":
                neighbors[n].f = (node.f + 1 + h)
                neighbors[n].g =node.f + 1 
            
            add_to_list = True
            
            #Check if there is a cheaper instance in open list
            #Check each neighbor againse open/close list for cheaper instance
            for o in g.openlist:
                if neighbors[n].room == o.room:
                    #TEST
                    #print "\t\tFound same room# in o-list: \n\tCost= " + str(o.f)
                    if neighbors[n].f >= o.f:
                        add_to_list = False
                        break;
                        
            if add_to_list == True:
                #Scan through close list
                for c in g.closelist:
                    if neighbors[n].room == c.room: #there is an inst in clist
                        if neighbors[n].f >= c.f:
                            add_to_list = False   
                            break;

            if add_to_list == True:
                g.openlist.append(deepcopy(neighbors[n]))
    
        g.openlist.sort(by_cost)         
        g.closelist.append(deepcopy(node))
        #end while
        
    backtrace = backtrack(g)
    print backtrace
    print "Cost: %s"%backtrace[-1][1].g
        #TEST
#        print "\t\t" + str(node.room) + " was added to the close list"
#    print "closelist = %s"%g.closelist


#Main function
if __name__ == '__main__':
    astar()
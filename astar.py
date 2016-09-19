class Room:
    parent = -1
    room = []
    dirt = 0
    g = 0
    f = 0
    closed = False
    
    def __init__(self,room):
        self.room = room
    
    def __str__(self):
        return str(self.room) + " Dirty:" + str(bool(self.dirt)) 

class Grid:
    rooms = {} #Should be a dictionary (x,y):Node
    width = 0
    height = 0
    dirt_count = 7
    start = []
    closelist = []
    openlist = []
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    


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

past_states = []
    
#g - +1:left or right, +1.3:up or down, 0:suck
#h - +number of dirty rooms
#def astar(grid, startrow, startcol):
#should choose the option that reduces the number of dirt first
#if no option to reduce dirt is available, pick the cheapest route    
#while len openl != 0:
#find the node with the least cost

def get_neighbors(r_coord, g):
    neighbors = {"UP" : [], "DOWN" : [], "LEFT" : [], "RIGHT" : []}
    
    rx = r_coord[0]
    ry = r_coord[1]
    
    #UP: r - 1
    if r_coord[0] != 1:
        neighbors["UP"] = g.rooms[rx-1,ry]
    #DOWN: r+1
    if r_coord[0] != g.height:
        neighbors["DOWN"] = g.rooms[rx+1,ry]
    #LEFT: c-1
    if r_coord[1] != 1:
        neighbors["LEFT"] = g.rooms[rx,ry-1]
    #RIGHT: c+1
    if r_coord[1] != g.width:
        neighbors["RIGHT"] = g.rooms[rx,ry+1]
    
    return neighbors


#Pseudocode
#initialize the open list
#initialize the closed list
#put the starting node on the open list (you can leave its f at zero)

#while the open list is not empty
#    find the node with the least f on the open list, call it "q"
#    pop q off the open list
#    generate q's 8 successors and set their parents to q
#    for each successor
#    	if successor is the goal, stop the search
#        successor.g = q.g + distance between successor and q
#        successor.h = distance from goal to successor
#        successor.f = successor.g + successor.h
#
#        if a node with the same position as successor is in the OPEN list \
#            which has a lower f than successor, skip this successor
#        if a node with the same position as successor is in the CLOSED list \ 
#            which has a lower f than successor, skip this successor
#        otherwise, add the node to the open list
#    end
#    push q on the closed list
#end

def astar_clean():
    print "A* Search:\n"
    #print "This only executes when %s is executed rather than imported" % __file__
    g = generate_grid(4,4)
    g.start = Room([3,3])
    g.openlist.append(g.start)
    
    #while the open list is not empty
    while (len(g.openlist) != 0 and g.dirt_count > 0):
        #pop q off the open list
        node = g.openlist.pop()
        
        #get neighbors
        neighbors = get_neighbors(node.room, g)
        
        #TEST
        #g.dirt_count = 0 Success
        
        #itterate through successors
        for n in neighbors.values():
            if(g.dirt_count == 0): #reached the goal
                break;
            #print n 
            if neighbors['UP'] 
            n.g = node.g + 
            
    #print next_node
    #print g.start
    #print g.room[(1,1)]
    #display_grid(g)
    #astar_clean(grid, 3, 2)
    


#Main function
if __name__ == '__main__':
    astar_clean()
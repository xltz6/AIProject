class Grid:
    rooms = {} #Should be a dictionary (x,y):Node
    width = 0
    height = 0
    dirt_count = 7
    start = 0
    closelist = []
    openlist = []

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

def generate_grid(height, width):
    grid = Grid(height, width)
    
    for row in range(1,height+1):
        for column in range(1,height+1):
            grid.rooms[(row, column)] = Room([row, column])
            #grid.room[(row,column)]
    dirty_rooms(grid)
    return grid

Project:
    - each node is a grid config -> ([rm#1-wh] & #dirt)
    - each node has a cost to get to: f = g + h
        - g = g.parent + edge_cost
        - h = number of dirts
    - there should be two lists:
        1.) Open list
    
'''
Daniel Wen

This is an implementation of the game 15-puzzle, a sliding puzzle
game where the goal of the game is to get all of the tiles in
order. The program uses the A* search algorithm to determine the
least amount of moves needed to get all tile in order using the least
number of moves. See the bottom of the file for sample inputs.
'''
import heapq
import random, time, math


class PriorityQueue():
    """Implementation of a priority queue
    to store nodes during search."""

    # TODO 1 : finish this class

    # HINT look up/use the module heapq.

    def __init__(self):
        self.queue = []
        self.current = 0

    def next(self):
        if self.current >= len(self.queue):
            self.current
            raise StopIteration

        out = self.queue[self.current]
        self.current += 1

        return out

    def pop(self):
        # Your code goes here
        return heapq.heappop(self.queue)

    def remove(self, nodeId):
        # Your code goes here
        return self.remove(nodeId)

    def __iter__(self):
        return self

    def __str__(self):
        return 'PQ:[%s]' % (', '.join([str(i) for i in self.queue]))

    def append(self, node):
        # Your code goes here
       heapq.heappush(self.queue, node)

    def __contains__(self, key):
        self.current = 0
        return key in [n for v, n in self.queue]

    def __eq__(self, other):
        return self == other

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = []

    def top(self):
        return self.queue[0]

    __next__ = next


def check_pq():
    ''' check_pq is checking if your PriorityQueue
    is completed or not'''
    pq = PriorityQueue()
    temp_list = []

    for i in range(10):
        a = random.randint(0, 10000)
        pq.append((a, 'a'))
        temp_list.append(a)

    temp_list = sorted(temp_list)

    for i in temp_list:
        j = pq.pop()
        if not i == j[0]:
            return False

    return True


# Extension #1
def inversion_count(new_state, size):
    ''' Depends on the size(width, N) of the puzzle,
    we can decide if the puzzle is solvable or not by counting inversions.
    If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
    If N is even, puzzle instance is solvable if
       the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is odd.
       the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is even.
    '''
    # Your code goes here
    return True


def getInitialState(sample):
    sample_list = list(sample)
    random.shuffle(sample_list)
    new_state = ''.join(sample_list)
    if (inversion_count(new_state, 4)):
        return new_state
    else:
        return None


def swap(n, i, j):
    return n[0:i] + n[j] + n[i + 1: j] + n[i] + n[j + 1:] #swaps characters at index i and j


def generateChild(n, size):
    i = n.rfind("_")  #finds index of space
    children = set()  # makes children set
    up = True
    down = True
    left = True
    right = True
    if i < 4:    #if space is on top row, don't move up
        up = False
    if i % size == 0:  #if space is on left column, don't move left
        left = False
    if i % size == size - 1:  #if space is on right column, don't move right
        right = False
    if i > 11:    #if space is on bottom row, don't move down
        down = False
    if up:   #if "up" move is valid
        children.add(swap(n, i - 4, i))  #generates "up" move
    if down:  #if "down" move is valid
        children.add(swap(n, i, i + 4))   #generates "down" move
    if left:  #if "left" move is valid
        children.add(swap(n, i - 1, i))  #generates "left" move
    if right:  #if "right" move is valid
        children.add(swap(n, i, i + 1))  #generates "right" move
    return children


def display_path(path_list, size):
    for n in range(size):
        for i in range(len(path_list)):
            print(path_list[i][n * size:(n + 1) * size], end=" " * size)
        print()
    print("\nThe shortest path length is :", len(path_list))
    return ""


def dist_heuristic(start, goal, size):
    # Your code goes here
    cost = 0
    for i in range(0, len(start)):
        x1, y1 = i % size, int(i / size)
        x2, y2 = goal.index(start[i]) % size, int(goal.index(start[i]) / size)
        cost += abs(x1 - x2) + abs(y1 - y2)
    return cost


def a_star(start, goal="_123456789ABCDEF", heuristic=dist_heuristic):
    frontier = PriorityQueue()
    if start == goal: return []
    size = 4
    frontier.append((heuristic(start, goal, size), start, [start]))  # add starting node to frontier
    explored = {start: heuristic(start, goal, size)}  # dictionary of path costs
    while frontier.size() > 0:  # while frontier is not empty
        cost, node, path = frontier.pop()  # pop lowest estimated cost node
        if node == goal:  # if node is the word
            return path  # return the path
        children = generateChild(node, size)  # generates children of node
        for c in children:  # for each child
            if c in explored and explored[c] > heuristic(c, goal, size) + len(path):  #replaces existing path is new path is less than it
                del explored[c]
            if c not in explored:  #if child has not been visited yet
                explored[c] = heuristic(c, goal, size) + len(path)  #adds path cost to explored dict
                frontier.append((heuristic(c, goal, size) + 1 + len(path), c, path + [c]))   #adds node to frontier

    return None


def main():
    # check PriorityQueue
    if check_pq():
        print("PriorityQueue is good to go.")
    else:
        print("PriorityQueue is not ready.")

    # A star
    ''' This part is for extension
    initial_state = getInitialState("_123456789ABCDEF")
    while initial_state == None:
       initial_state = getInitialState("_123456789ABCDEF")
    '''
    initial_state = input("Type initial state: ")
    cur_time = time.time()
    path = (a_star(initial_state))
    if path != None:
        display_path(path, 4)
    else:
        print("No Path Found.")
    print("Duration: ", (time.time() - cur_time))


if __name__ == '__main__':
    main()

''' Sample output 1
PriorityQueue is good to go.

Initial State: 152349678_ABCDEF
1523    1523    1_23    _123    
4967    4_67    4567    4567    
8_AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 4
Duration:  0.0

Sample output 2
PriorityQueue is good to go.

Initial State: 2_63514B897ACDEF
2_63    _263    5263    5263    5263    5263    5263    5263    5263    52_3    5_23    _523    1523    1523    1_23    _123    
514B    514B    _14B    1_4B    14_B    147B    147B    147_    14_7    1467    1467    1467    _467    4_67    4567    4567    
897A    897A    897A    897A    897A    89_A    89A_    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 16
Duration:  0.005984306335449219

Sample output 3
PriorityQueue is good to go.

Initial state: 8936C_24A71FDB5E
8936    8936    8936    893_    89_3    8943    8943    8_43    84_3    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
C_24    C2_4    C24_    C246    C246    C2_6    C_26    C926    C926    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 37
Duration:  0.34381628036499023
'''

import heapq
import matplotlib.pyplot as plt
import numpy as np

maze = [
    ['S', '.', '#', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '#', '.', '.'],
    ['#', '.', '.', '.', '#', '.', '.'],
    ['.', '#', '#', '.', '.', '.', '.'],
    ['.', '.', '.', '#', '.', '#', 'G']
]

rows = len(maze)
cols = len(maze[0])

# Find Start and Goal
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 'S':
            start = (i, j)
        if maze[i][j] == 'G':
            goal = (i, j)

# Manhattan heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):

    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_list:

        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()
            return path

        for d in directions:

            neighbor = (current[0] + d[0],
                        current[1] + d[1])

            r, c = neighbor

            if (0 <= r < rows and
                0 <= c < cols and
                maze[r][c] != '#'):

                temp_g = g_score[current] + 1

                if (neighbor not in g_score or
                    temp_g < g_score[neighbor]):

                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g

                    f_score = temp_g + heuristic(neighbor, goal)

                    heapq.heappush(
                        open_list,
                        (f_score, neighbor)
                    )

    return None

path = astar(maze, start, goal)

# Create grid
grid = np.zeros((rows, cols))

for i in range(rows):
    for j in range(cols):
        if maze[i][j] == '#':
            grid[i][j] = 1

if path:
    for r, c in path:
        grid[r][c] = 2

# Show visualization
plt.imshow(grid)
plt.title("Maze Solver using A* Algorithm")
plt.show()
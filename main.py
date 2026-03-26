import heapq
import matplotlib.pyplot as plt

GRID_SIZE = 10

start = (0, 0)
end = (9, 9)

# Try changing this later to see different behavior
threats = [(4,4), (5,5), (6,6)]

# Heuristic (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Get neighbors (including diagonal movement)
def get_neighbors(node):
    x, y = node
    neighbors = [
        (x+1,y),(x-1,y),(x,y+1),(x,y-1),  # straight
        (x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)  # diagonal
    ]
    
    valid = []
    for n in neighbors:
        if 0 <= n[0] < GRID_SIZE and 0 <= n[1] < GRID_SIZE:
            if n not in threats:
                valid.append(n)
    return valid

# A* algorithm
def a_star(start, end):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in get_neighbors(current):

            # Diagonal vs straight cost
            if neighbor[0] != current[0] and neighbor[1] != current[1]:
                temp_g = g_score[current] + 1.4
            else:
                temp_g = g_score[current] + 1

            if neighbor not in g_score or temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score = temp_g + heuristic(neighbor, end)
                heapq.heappush(open_list, (f_score, neighbor))

    return None

# Run algorithm
path = a_star(start, end)

# Output path clearly
print("\nFinal Path:")
for step in path:
    print(step)

print("\nPath length:", len(path))

# =========================
# VISUALIZATION (CLEAN)
# =========================

# Draw grid
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        plt.scatter(x, y, s=20)

# Draw threats (RED squares)
for threat in threats:
    plt.scatter(threat[0], threat[1], marker='s', s=200)

# Draw path (LINE + points)
if path:
    x_coords = [p[0] for p in path]
    y_coords = [p[1] for p in path]
    plt.plot(x_coords, y_coords, marker='o')

# Draw start & end
plt.scatter(start[0], start[1], s=200)
plt.scatter(end[0], end[1], s=200)

plt.title("Mission Planner - A* Pathfinding")
plt.grid()
plt.show()
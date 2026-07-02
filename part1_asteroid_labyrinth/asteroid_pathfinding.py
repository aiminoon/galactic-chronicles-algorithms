import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict, deque

#Constants
GRID_CELL_SIZE = 10
DENSITY_THRESHOLD = 3
SIZE_THRESHOLD = 30

file_path = "Asteroid_Field_Data.csv"
df_asteroid = pd.read_csv(file_path)

#Load data (assuming df_asteroid already loaded)
asteroids = df_asteroid [['X', 'Y', 'Size']].to_dict('records')

# Step 1: Populate grid
grid = defaultdict(list)
for a in asteroids:
  gx, gy = int(a['X'] // GRID_CELL_SIZE), int(a['Y'] // GRID_CELL_SIZE)
  grid[(gx, gy)].append(a)
  
#Step 2: Identify safe zones.
safe_zones = set()
for (gx, gy), asts in grid.items():
  count = len(asts)
  avg_size = sum(a['Size'] for a in asts) / count if count else 0
  if count < DENSITY_THRESHOLD and avg_size < SIZE_THRESHOLD:
    safe_zones.add((gx, gy))

#Step 3: BFS Pathfinding
def bfs_path(start, goal, safe_zones):
  queue = deque()
  visited = set()
  parent = {}
  queue.append(start)
  visited.add(start)
  
  directions = [(-1,0), (1,0), (0,-1), (0,1)] # up, down, left, right
  
  while queue:
    current = queue.popleft()
    if current == goal:
      # Reconstruct path
      path = []
      while current != start:
        path.append(current)
        current = parent [current]
      path.append(start)
      return path[::-1]
      
    for dx, dy in directions:
      neighbor = (current[0] + dx, current [1] + dy)
      if neighbor in safe_zones and neighbor not in visited:
        visited.add(neighbor)
        parent [neighbor] = current
        queue.append(neighbor)
        
  return None # No path found
  
# Choose start and goal (manually or programmatically)
start_cell = min(safe_zones)
end_cell = max(safe_zones)

path = bfs_path(start_cell, end_cell, safe_zones)

print(f"Path found:{path is not None}, Length: {len(path) if path else 0}")

#Step 4: Visualize
def visualize(grid, safe_zones, path):
  fig, ax = plt.subplots (figsize=(10, 10))
  for (gx, gy), _ in grid.items():
    color = 'green' if (gx, gy) in safe_zones else 'red'
    ax.add_patch(plt.Rectangle((gx * GRID_CELL_SIZE, gy * GRID_CELL_SIZE), GRID_CELL_SIZE, GRID_CELL_SIZE, edgecolor=color, facecolor=color, alpha=0.3))
  
  if path:
    for cell in path:
      ax.add_patch(plt.Rectangle((cell[0] * GRID_CELL_SIZE, cell [1] * GRID_CELL_SIZE), GRID_CELL_SIZE, GRID_CELL_SIZE, edgecolor='blue', facecolor='blue', alpha=0.6))
  
  plt.title("Safe Zones (Green), Unsafe Zones (Red), Path (Blue)")
  plt.xlabel("X Coordinate")
  plt.ylabel("Y Coordinate")
  plt.xlim(df_asteroid['X'].min(), df_asteroid['X'].max())
  plt.ylim(df_asteroid['Y'].min(), df_asteroid['Y'].max())
  plt.grid(True)
  plt.gca().set_aspect('equal')
  plt.show()
  
visualize(grid, safe_zones, path)

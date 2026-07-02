import pandas as pd
import heapq

# Load the dataset
file_path = "Stargate_Data.csv"
df_stargate = pd.read_csv(file_path)

# Build directed graph from csv data
graph = {}
for _, row in df_stargate.iterrows():
    src = row['From']
    dest = row['To']
    time = row['Time']
    risk = row['Risk']
    if src not in graph:
        graph[src] = []
    graph[src].append((dest, time, risk))
    # Add all nodes (even if they have no outgoing edges)
    if dest not in graph:
        graph[dest] = []


# Custom Dijkstra's Algorithm to minimize (Time + Risk)
def safest_fastest_path(graph, start):
    dist = {node: float('inf') for node in graph}
    risk_level = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    risk_level[start] = 0
    pq = [(0, 0, start)]  # (total_time, total_risk, node)

    while pq:
        total_time, total_risk, node = heapq.heappop(pq)
        if total_time > dist[node]:
            continue
        for neighbor, t, r in graph[node]:
            new_time = total_time + t
            new_risk = total_risk + r
            if (new_time < dist[neighbor]) or (new_time == dist[neighbor] and new_risk < risk_level[neighbor]):
                dist[neighbor] = new_time
                risk_level[neighbor] = new_risk
                prev[neighbor] = node
                heapq.heappush(pq, (new_time, new_risk, neighbor))

    return dist, risk_level, prev


# Identify terminal gates (only appear in 'To' but not in 'From')
from_nodes = set(df_stargate['From'])
to_nodes = set(df_stargate['To'])
terminal_nodes = sorted(to_nodes - from_nodes)

print("Terminal Gates (no outgoing paths):")
print(terminal_nodes)

start_node = 'Gate-01'
end_node = 'Gate-07'  # Destination based on the story context
distances, risks, predecessors = safest_fastest_path(graph, start_node)


# Reconstruct the path
def reconstruct_path(predecessors, end):
    path = []
    node = end
    while node:
        path.append(node)
        node = predecessors[node]
    return path[::-1]


path = reconstruct_path(predecessors, end_node)

# Output results
if distances[end_node] == float('inf'):
    print(f"No path found from {start_node} to {end_node}")
else:
    print("Safest & Fastest Path:", " → ".join(path))
    print("Total Travel Time:", distances[end_node])
    print("Total Risk:", round(risks[end_node], 3))

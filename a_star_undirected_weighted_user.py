import heapq

def read_graph_and_heuristics():
    adj_list = {}
    heuristics = {}
    print("Enter undirected weighted graph (e.g., 'A:B,2,C,3' for A<->B(weight=2), A<->C(weight=3)). Enter empty line to finish:")
    while True:
        line = input().strip()
        if not line:
            break
        try:
            parts = line.split(':')
            node = parts[0].strip()
            neighbors = []
            neighbor_pairs = parts[1].split(',')
            for i in range(0, len(neighbor_pairs), 2):
                neighbor = neighbor_pairs[i].strip()
                weight = float(neighbor_pairs[i+1].strip())
                neighbors.append((neighbor, weight))
            adj_list[node] = neighbors
        except (ValueError, IndexError):
            print("Invalid input. Use format 'node:neighbor1,weight1,neighbor2,weight2'")
    print("Enter heuristic values (e.g., 'A:5' for h(A)=5). Enter empty line to finish:")
    while True:
        line = input().strip()
        if not line:
            break
        try:
            node, h_val = line.split(':')
            heuristics[node.strip()] = float(h_val.strip())
        except ValueError:
            print("Invalid input. Use format 'node:heuristic'")
    # Make graph undirected
    undirected = {}
    for node in adj_list:
        undirected[node] = adj_list[node]
        for neighbor, weight in adj_list[node]:
            if neighbor not in undirected:
                undirected[neighbor] = []
            undirected[neighbor].append((node, weight))
    return undirected, heuristics

def a_star(graph, heuristics, start_node, goal_node):
    if start_node not in graph or goal_node not in graph:
        print("Start or goal node not found.")
        return
    if start_node not in heuristics or goal_node not in heuristics:
        print("Heuristic missing for start or goal node.")
        return
    pq = [(heuristics[start_node], start_node, [start_node], 0)]
    visited = set()
    while pq:
        f_score, node, path, g_score = heapq.heappop(pq)
        if node == goal_node:
            print(f"Shortest Path: {' -> '.join(path)}")
            print(f"Total Cost: {g_score}")
            return
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    new_g = g_score + weight
                    new_f = new_g + heuristics.get(neighbor, float('inf'))
                    new_path = path + [neighbor]
                    heapq.heappush(pq, (new_f, neighbor, new_path, new_g))
    print("No path found to goal.")

def main():
    graph, heuristics = read_graph_and_heuristics()
    if not graph or not heuristics:
        print("Graph or heuristics empty.")
        return
    start_node = input("Enter the starting node: ")
    goal_node = input("Enter the goal node: ")
    a_star(graph, heuristics, start_node, goal_node)

if __name__ == "__main__":
    main()
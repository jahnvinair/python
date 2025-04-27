import pandas as pd
import heapq

def read_graph_and_heuristics(graph_file, heuristic_file):
    # Read graph
    df_graph = pd.read_csv(graph_file)
    adj_list = {}
    for _, row in df_graph.iterrows():
        node = row['node']
        neighbor = row['neighbor']
        weight = float(row['weight'])
        if node not in adj_list:
            adj_list[node] = []
        adj_list[node].append((neighbor, weight))
    # Read heuristics
    df_heur = pd.read_csv(heuristic_file)
    heuristics = {row['node']: float(row['heuristic']) for _, row in df_heur.iterrows()}
    return adj_list, heuristics

def a_star(graph, heuristics, start_node, goal_node):
    if start_node not in graph or goal_node not in graph:
        print("Start or goal node not found.")
        return
    if start_node not in heuristics or goal_node not in heuristics:
        print("Heuristic missing for start or goal node.")
        return
    # Priority queue: (f_score, node, path, g_score)
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
    graph_file = 'graph.csv'
    heuristic_file = 'heuristics.csv'
    try:
        graph, heuristics = read_graph_and_heuristics(graph_file, heuristic_file)
    except FileNotFoundError:
        print("CSV file not found.")
        return
    start_node = input("Enter the starting node: ")
    goal_node = input("Enter the goal node: ")
    a_star(graph, heuristics, start_node, goal_node)

if __name__ == "__main__":
    main()

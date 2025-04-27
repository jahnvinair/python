import heapq

def read_graph_and_heuristics():
    adj_list = {}
    heuristics = {}
    print("Enter directed weighted graph (e.g., 'A:B,2,C,3' for A->B(weight=2), A->C(weight=3)). Enter empty line to finish:")
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
    return adj_list, heuristics

def best_first_search(graph, heuristics, start_node):
    if start_node not in graph or start_node not in heuristics:
        print("Starting node not found or heuristic missing.")
        return
    pq = [(heuristics[start_node], start_node)]
    visited = set()
    print("Best First Search Traversal:", end=' ')
    while pq:
        h_val, node = heapq.heappop(pq)
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor, _ in graph.get(node, []):
                if neighbor not in visited and neighbor in heuristics:
                    heapq.heappush(pq, (heuristics[neighbor], neighbor))
    print()

def main():
    graph, heuristics = read_graph_and_heuristics()
    if not graph or not heuristics:
        print("Graph or heuristics empty.")
        return
    start_node = input("Enter the starting node: ")
    best_first_search(graph, heuristics, start_node)

if __name__ == "__main__":
    main()

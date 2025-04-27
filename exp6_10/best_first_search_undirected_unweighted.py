import heapq

def read_graph_and_heuristics():
    adj_list = {}
    heuristics = {}
    print("Enter undirected unweighted graph (e.g., 'A:B,C' for A<->B,C). Enter empty line to finish:")
    while True:
        line = input().strip()
        if not line:
            break
        try:
            node, neighbors = line.split(':')
            adj_list[node.strip()] = [n.strip() for n in neighbors.split(',')]
        except ValueError:
            print("Invalid input. Use format 'node:neighbor1,neighbor2'")
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
        for neighbor in adj_list[node]:
            if neighbor not in undirected:
                undirected[neighbor] = []
            if node not in undirected[neighbor]:
                undirected[neighbor].append(node)
    return undirected, heuristics

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
            for neighbor in graph.get(node, []):
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

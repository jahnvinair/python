from collections import deque

def read_graph():
    adj_list = {}
    print("Enter nodes and their neighbors (e.g., 'A:B,C' for A connected to B,C). Enter empty line to finish:")
    while True:
        line = input().strip()
        if not line:
            break
        try:
            node, neighbors = line.split(':')
            adj_list[node.strip()] = [n.strip() for n in neighbors.split(',')]
        except ValueError:
            print("Invalid input. Use format 'node:neighbor1,neighbor2'")
    return adj_list

def bfs(graph, start_node):
    if start_node not in graph:
        print("Starting node not found in the graph.")
        return
    queue = deque([start_node])
    visited = set([start_node])
    print("BFS Traversal:", end=' ')
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()

def main():
    graph = read_graph()
    if not graph:
        print("Graph is empty.")
        return
    start_node = input("Enter the starting node: ")
    bfs(graph, start_node)

if __name__ == "__main__":
    main()

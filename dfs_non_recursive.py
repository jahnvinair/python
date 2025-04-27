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

def dfs_non_recursive(graph, start_node):
    if start_node not in graph:
        print("Starting node not found in the graph.")
        return
    stack = [start_node]
    visited = set()
    print("DFS Traversal:", end=' ')
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Push neighbors in reverse to mimic recursive order
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    print()

def main():
    graph = read_graph()
    if not graph:
        print("Graph is empty.")
        return
    start_node = input("Enter the starting node: ")
    dfs_non_recursive(graph, start_node)

if __name__ == "__main__":
    main()
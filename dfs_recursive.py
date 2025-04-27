import pandas as pd

def read_graph(file_path):
    df = pd.read_csv(file_path)
    adj_list = {}
    for index, row in df.iterrows():
        node = row['node']
        neighbors = row['neighbors'].split(',')
        adj_list[node] = neighbors
    return adj_list

def dfs_recursive(graph, node, visited):
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def main():
    file_path = 'graph.csv'
    graph = read_graph(file_path)
    start_node = input("Enter the starting node: ")
    visited = set()
    if start_node in graph:
        print("DFS Traversal:", end=' ')
        dfs_recursive(graph, start_node, visited)
        print()
    else:
        print("Starting node not found in the graph.")

if __name__ == "__main__":
    main()
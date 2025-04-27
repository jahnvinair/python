import csv

def create_graph_csv(filename='graph.csv'):
    # Sample directed weighted graph: A->B(2), A->C(3), B->D(1), C->D(4)
    data = [
        ['node', 'neighbor', 'weight'],
        ['A', 'B', 2],
        ['A', 'C', 3],
        ['B', 'D', 1],
        ['C', 'D', 4]
    ]
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"Created {filename}")

def create_heuristics_csv(filename='heuristics.csv'):
    # Sample heuristic values: h(A)=5, h(B)=3, h(C)=4, h(D)=0
    data = [
        ['node', 'heuristic'],
        ['A', 5],
        ['B', 3],
        ['C', 4],
        ['D', 0]
    ]
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"Created {filename}")

def main():
    create_graph_csv()
    create_heuristics_csv()

if __name__ == "__main__":
    main()
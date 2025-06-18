from typing import List

def dfs(graph: List[List[int]], visited: List[bool], node: int):
    if visited[node]:
        print(f"Node {node} has already been visited. Skipping.")
        return

    visited[node] = True
    print(f"\n--> Visiting node {node}")
    print(f"Current visited list: {visited}")
    print(f"Neighbors of node {node}: {graph[node]}")

    for neighbor in graph[node]:
        print(f"Checking neighbor {neighbor} of node {node}")
        if not visited[neighbor]:
            print(f"Neighbor {neighbor} not visited yet. Going deeper.")
            dfs(graph, visited, neighbor)
        else:
            print(f"Neighbor {neighbor} already visited. Not going deeper.")

# Example usage
if __name__ == "__main__":
    graph = [
        [1, 2],    # Node 0
        [0, 3],    # Node 1
        [0, 4],    # Node 2
        [1],       # Node 3
        [2]        # Node 4
    ]

    visited = [False] * len(graph)

    print("Starting DFS traversal...\n")
    dfs(graph, visited, 0)
    print("\nDFS complete.")

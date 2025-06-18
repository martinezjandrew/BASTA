from typing import List
from collections import deque

def bfs(graph: List[List[int]], start: int):
    visited = [False] * len(graph)  # Keep track of visited nodes
    queue = deque()  # Use deque for efficient pops from the front

    print(f"Starting BFS from node {start}")
    
    # Start with the first node
    visited[start] = True
    queue.append(start)

    while queue:
        node = queue.popleft()  # Remove the node from the front of the queue
        print(f"\n--> Visiting node {node}")
        print(f"Queue state: {list(queue)}")
        print(f"Visited list: {visited}")
        print(f"Neighbors of node {node}: {graph[node]}")

        # Check all neighbors
        for neighbor in graph[node]:
            print(f"Checking neighbor {neighbor} of node {node}")
            if not visited[neighbor]:
                print(f"Neighbor {neighbor} not visited. Adding to queue.")
                visited[neighbor] = True
                queue.append(neighbor)
            else:
                print(f"Neighbor {neighbor} already visited. Skipping.")

    print("\nBFS complete.")

# Example usage
if __name__ == "__main__":
    graph = [
        [1, 2],    # Node 0
        [0, 3],    # Node 1
        [0, 4],    # Node 2
        [1],       # Node 3
        [2]        # Node 4
    ]

    bfs(graph, 0)

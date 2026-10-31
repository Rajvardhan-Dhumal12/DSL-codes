nodes = ['A', 'B', 'C', 'D', 'E']
matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]
visited = []
stack = ['A']
while stack:
    node = stack.pop()
    if node not in visited:
        visited.append(node)
        i = nodes.index(node)
        for j in range(len(nodes) - 1, -1, -1):
            if matrix[i][j] == 1:
                if nodes[j] not in visited:
                    stack.append(nodes[j])

print("DFS Traversal:", visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}
visited = []
queue = ['A']
while queue:
    node = queue.pop(0)

    if node not in visited:
        visited.append(node)

        for x in graph[node]:
            if x not in visited:
                queue.append(x)

print("BFS Traversal:", visited)
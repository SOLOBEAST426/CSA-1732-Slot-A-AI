import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 5, 'B': 4, 'C': 3,
    'D': 3, 'E': 1, 'F': 2, 'G': 0
}

def astar(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = {}

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            new_f = new_cost + heuristic[neighbor]
            heapq.heappush(
                queue,
                (new_f, new_cost, neighbor, path + [neighbor])
            )

    return None, float('inf')

path, cost = astar('A', 'G')
print("Path:", path)
print("Cost:", cost)
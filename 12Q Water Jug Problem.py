from collections import deque

def water_jug():
    capacity1, capacity2 = 4, 3
    target = 2

    queue = deque([(0, 0)])
    visited = {(0, 0)}

    while queue:
        a, b = queue.popleft()
        print("Jug 1:", a, "Jug 2:", b)

        if a == target or b == target:
            print("Target achieved!")
            return

        states = [
            (capacity1, b),
            (a, capacity2),
            (0, b),
            (a, 0),
            (a - min(a, capacity2-b), b + min(a, capacity2-b)),
            (a + min(b, capacity1-a), b - min(b, capacity1-a))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

water_jug()
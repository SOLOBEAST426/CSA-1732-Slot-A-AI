from collections import deque

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            for s in path + [state]:
                print(s)
            return

        m, c, boat = state

        for dm, dc in moves:
            if boat == 1:
                nm, nc = m-dm, c-dc
                nb = 0
            else:
                nm, nc = m+dm, c+dc
                nb = 1

            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue

            rm, rc = 3-nm, 3-nc

            if (nm > 0 and nc > nm) or (rm > 0 and rc > rm):
                continue

            new_state = (nm, nc, nb)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

solve()
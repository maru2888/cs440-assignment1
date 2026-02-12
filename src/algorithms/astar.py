# part 2: A* algorithm implementation
import heapq
from env.grid import neighbors, BLOCKED


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path(parent, goal):
    path = []
    cur = goal
    while cur in parent:
        path.append(cur)
        cur = parent[cur]
    path.append(cur)
    path.reverse()
    return path


def astar(start, goal, grid, tie_mode="larger_g"):
    """
    tie_mode:
        "larger_g" → prefer deeper nodes when f ties
        "smaller_g" → prefer shallower nodes when f ties
    """

    open_heap = []
    heap_counter = 0  # prevents Python from comparing states

    g = {start: 0}
    parent = {}

    expanded = 0

    h0 = manhattan(start, goal)

    if tie_mode == "larger_g":
        heapq.heappush(open_heap, (h0, -0, heap_counter, start))
    else:
        heapq.heappush(open_heap, (h0, 0, heap_counter, start))

    closed = set()

    while open_heap:
        f, g_tiebreak, _, current = heapq.heappop(open_heap)

        if current in closed:
            continue

        closed.add(current)
        expanded += 1

        if current == goal:
            return reconstruct_path(parent, goal), expanded

        for nbr in neighbors(*current):
            if grid[nbr[0]][nbr[1]] == BLOCKED:
                continue

            tentative_g = g[current] + 1

            if nbr not in g or tentative_g < g[nbr]:
                g[nbr] = tentative_g
                parent[nbr] = current

                f_val = tentative_g + manhattan(nbr, goal)

                heap_counter += 1

                if tie_mode == "larger_g":
                    heapq.heappush(open_heap, (f_val, -tentative_g, heap_counter, nbr))
                else:
                    heapq.heappush(open_heap, (f_val, tentative_g, heap_counter, nbr))

    return None, expanded

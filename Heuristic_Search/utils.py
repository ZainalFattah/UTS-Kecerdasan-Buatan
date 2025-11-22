# utils.py
import heapq

def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star(start, goal, grid):
    rows,cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0 + manhattan(start,goal), 0, start, None))  # (f, g, node, parent)
    came_from = {}
    gscore = {start: 0}
    closed = set()
    while open_set:
        f, g, node, parent = heapq.heappop(open_set)
        if node in closed:
            continue
        came_from[node] = parent
        if node == goal:
            break
        closed.add(node)
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nb = (node[0]+dr, node[1]+dc)
            if not (0 <= nb[0] < rows and 0 <= nb[1] < cols):
                continue
            if grid[nb[0]][nb[1]] == 1:
                continue
            tentative_g = g + 1
            if tentative_g < gscore.get(nb, float('inf')):
                gscore[nb] = tentative_g
                fscore = tentative_g + manhattan(nb, goal)
                heapq.heappush(open_set, (fscore, tentative_g, nb, node))
    # reconstruct
    if goal not in came_from:
        return None
    path=[]
    cur=goal
    while cur:
        path.append(cur)
        cur = came_from[cur]
    return list(reversed(path))

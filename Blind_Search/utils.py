# utils.py
from collections import deque

def neighbors(pos, rows, cols):
    r,c = pos
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr,nc = r+dr, c+dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield (nr,nc)

def bfs(start, goal, grid):
    rows,cols = len(grid), len(grid[0])
    q = deque([start])
    visited = {start: None}
    while q:
        node = q.popleft()
        if node == goal:
            break
        for nb in neighbors(node, rows, cols):
            if nb not in visited and grid[nb[0]][nb[1]] == 0:
                visited[nb] = node
                q.append(nb)
    # reconstruct path
    if goal not in visited:
        return None
    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = visited[cur]
    return list(reversed(path))

def dfs(start, goal, grid, max_depth=10000):
    rows,cols = len(grid), len(grid[0])
    stack = [(start, None)]
    visited = {start: None}
    while stack:
        node, parent = stack.pop()
        if node == goal:
            break
        for nb in neighbors(node, rows, cols):
            if nb not in visited and grid[nb[0]][nb[1]] == 0:
                visited[nb] = node
                stack.append((nb, node))
    if goal not in visited:
        return None
    path=[]
    cur=goal
    while cur:
        path.append(cur)
        cur = visited[cur]
    return list(reversed(path))

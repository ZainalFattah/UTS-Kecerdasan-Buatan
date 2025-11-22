# streamlit_app.py
import streamlit as st
import numpy as np
from utils import bfs, dfs

st.title("Blind Search — BFS & DFS (Grid Pathfinding)")

rows = st.number_input("Rows", min_value=5, max_value=25, value=8)
cols = st.number_input("Cols", min_value=5, max_value=25, value=8)

# default grid: 0 free, 1 obstacle
if "grid" not in st.session_state:
    st.session_state.grid = np.zeros((rows, cols), dtype=int)

# allow user to randomize obstacles
if st.button("Random obstacles"):
    prob = st.slider("Obstacle probability", 0.0, 0.5, 0.2)
    st.session_state.grid = (np.random.rand(rows, cols) < prob).astype(int)

# Coordinate inputs
st.subheader("Start & Goal Coordinates")

col1, col2 = st.columns(2)

sr = col1.number_input("Start row", min_value=0, max_value=rows-1, value=0)
sc = col2.number_input("Start col", min_value=0, max_value=cols-1, value=0)

gr = col1.number_input("Goal row", min_value=0, max_value=rows-1, value=rows-1)
gc = col2.number_input("Goal col", min_value=0, max_value=cols-1, value=cols-1)

start = (sr, sc)
goal = (gr, gc)

# ensure start/goal free
grid = st.session_state.grid.copy()
grid[start[0], start[1]] = 0
grid[goal[0], goal[1]] = 0

algo = st.radio("Algorithm", ["BFS", "DFS"])
if st.button("Find path"):
    if algo == "BFS":
        path = bfs(start, goal, grid.tolist())
    else:
        path = dfs(start, goal, grid.tolist())
    if path is None:
        st.warning("No path found")
    else:
        st.success(f"Found path length {len(path)}")
        # show grid with path
        disp = grid.copy().astype(object)
        for r in range(rows):
            for c in range(cols):
                if (r,c) == start:
                    disp[r,c] = "S"
                elif (r,c) == goal:
                    disp[r,c] = "G"
                elif grid[r,c] == 1:
                    disp[r,c] = "X"
                else:
                    disp[r,c] = "."
        for (r,c) in path:
            if (r,c) != start and (r,c) != goal:
                disp[r,c] = "*"
        st.table(disp)

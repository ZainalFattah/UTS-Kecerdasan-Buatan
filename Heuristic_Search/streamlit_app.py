# streamlit_app.py
import streamlit as st
import numpy as np
from utils import a_star, manhattan

st.title("Heuristic Search — A* (Grid)")

rows = st.number_input("Rows", 5, 30, 8)
cols = st.number_input("Cols", 5, 30, 8)
prob = st.slider("Obstacle probability", 0.0, 0.5, 0.2)
if st.button("Generate grid"):
    grid = (np.random.rand(rows, cols) < prob).astype(int)
    st.session_state.grid = grid
else:
    if "grid" not in st.session_state:
        st.session_state.grid = np.zeros((rows, cols), dtype=int)
grid = st.session_state.grid.copy()

sr = st.number_input("Start row", 0, rows-1, 0)
sc = st.number_input("Start col", 0, cols-1, 0)
gr = st.number_input("Goal row", 0, rows-1, rows-1)
gc = st.number_input("Goal col", 0, cols-1, cols-1)
start=(sr,sc); goal=(gr,gc)
grid[start]=0; grid[goal]=0

if st.button("Run A*"):
    path = a_star(start, goal, grid.tolist())
    if not path:
        st.warning("No path found")
    else:
        st.success(f"Path length {len(path)} (heuristic manhattan={manhattan(start,goal)})")
        disp = grid.copy().astype(object)
        for r in range(rows):
            for c in range(cols):
                if (r,c)==start: disp[r,c]="S"
                elif (r,c)==goal: disp[r,c]="G"
                elif grid[r,c]==1: disp[r,c]="X"
                else: disp[r,c]="."
        for (r,c) in path:
            if (r,c)!=start and (r,c)!=goal:
                disp[r,c]="*"
        st.table(disp)

# streamlit_app.py
import streamlit as st
from fuzzy_utils import infer_tip, defuzzify_centroid, tri_membership
import numpy as np
import matplotlib.pyplot as plt

st.title("Restoran — Sistem Tip Fuzzy (Mamdani)")

st.markdown("Fuzzy set: Food(0..10), Service(0..10), Tip(0..20)")

food = st.slider("Food Quality (0..10)", 0.0, 10.0, 7.0)
service = st.slider("Service Quality (0..10)", 0.0, 10.0, 3.0)

res = infer_tip(food, service)
st.write("Memberships and rule activations:")
st.json(res)

tip = defuzzify_centroid(res["low_act"], res["high_act"])
st.success(f"Defuzzified Tip ≈ {tip:.2f}%")

# show membership plots
xs_food = np.linspace(0,10,200)
food_bad_vals = [tri_membership(x,0,0,5) for x in xs_food]
food_good_vals = [tri_membership(x,5,10,10) for x in xs_food]

fig1, ax = plt.subplots()
ax.plot(xs_food, food_bad_vals, label="Food Bad")
ax.plot(xs_food, food_good_vals, label="Food Good")
ax.axvline(food, linestyle="--")
ax.legend()
st.pyplot(fig1)

xs_tip = np.linspace(0,20,300)
low_vals = [tri_membership(x,0,0,10) for x in xs_tip]
high_vals = [tri_membership(x,10,20,20) for x in xs_tip]
fig2, ax2 = plt.subplots()
ax2.plot(xs_tip, low_vals, label="Tip Low")
ax2.plot(xs_tip, high_vals, label="Tip High")
ax2.axvline(tip, color='green', linestyle='--', label=f"defuzz={tip:.2f}")
ax2.legend()
st.pyplot(fig2)

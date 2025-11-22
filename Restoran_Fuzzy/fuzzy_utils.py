# fuzzy_utils.py
import numpy as np

def tri_membership(x, a, b, c):
    if a == b:
        if x <= b: return 1.0
        elif x >= c: return 0.0
        else: return (c - x) / (c - b)
    if b == c:
        if x >= b: return 1.0
        elif x <= a: return 0.0
        else: return (x - a) / (b - a)
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

def infer_tip(food, service):
    food_bad = tri_membership(food, 0,0,5)
    food_good = tri_membership(food, 5,10,10)
    serv_poor = tri_membership(service, 0,0,5)
    serv_ex = tri_membership(service, 5,10,10)
    # rules:
    # R1: IF Service is Poor OR Food is Bad THEN Tip is Low
    low_act = max(serv_poor, food_bad)
    # R2: IF Service is Excellent AND Food is Good THEN Tip is High
    high_act = min(serv_ex, food_good)
    return {
        "food_bad": food_bad,
        "food_good": food_good,
        "serv_poor": serv_poor,
        "serv_ex": serv_ex,
        "low_act": low_act,
        "high_act": high_act
    }

def defuzzify_centroid(low_act, high_act, resolution=1000):
    # universe for tip: 0..20
    xs = np.linspace(0,20,resolution)
    # membership for Low: tri (0,0,10) -> decreasing
    low_vals = np.array([min(tri_membership(x,0,0,10), low_act) for x in xs])
    high_vals = np.array([min(tri_membership(x,10,20,20), high_act) for x in xs])
    agg = np.maximum(low_vals, high_vals)  # aggregate (max)
    if agg.sum() == 0:
        return 0.0
    centroid = (np.sum(xs * agg) / np.sum(agg))
    return centroid

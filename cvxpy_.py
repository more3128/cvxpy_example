# import lib
import cvxpy as cp
import matplotlib.pyplot as plt
import numpy as np

# set initial data
price_a = np.full(12, 325.)
price_b = np.array([300, 300, 290, 275, 275, 280, 260, 250, 230, 200, 210, 190.])
price_c = np.array([100, 110, 98, 115, 200, 220, 210, 500, 500, 490, 487, 550.])
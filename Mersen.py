import numpy as np

def Mersen_generator(n):
    rng = np.random.default_rng()
    return rng.random(n)
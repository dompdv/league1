import data_original
import proba_table
import numpy as np
import itertools


built = proba_table.proba_table2()

original = np.zeros((4,4,4,4,8,8))

for Aa, Ad, Ba, Bd, s1, s2, p in data_original.raw_data():
    s1, s2 = min(s1, 7), min(s2, 7)
    original[Aa, Ad, Ba, Bd, s1, s2] += p

for Aa in range(4):
    for Ad in range(4):
        for Ba in range(4):
            for Bd in range(4):
                t = np.sum(original[Aa, Ad, Ba, Bd])
                if t > 0:
                    original[Aa, Ad, Ba, Bd] /= t

for Aa in range(4):
    for Ad in range(4):
        for Ba in range(4):
            for Bd in range(4):
                for s1 in range(8):
                    for s2 in range(8):
                        print("{},{},{},{},{},{},{:.8f},{:.8f}".format(Aa, Ad, Ba, Bd, s1,s2,
                                                                   original[Aa, Ad, Ba, Bd, s1,s2],
                                                                   built[Aa, Ad, Ba, Bd, s1,s2]))


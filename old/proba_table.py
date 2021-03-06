import numpy as np

def proba_table():
    pE = np.zeros((4, 4, 8))
    pN = np.zeros((4, 4, 8))
    pH = np.zeros((4, 4, 8))
    pN[0, 0] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    pN[0, 1] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    pN[0, 2] = np.array([60, 27, 8, 3, 1, 1, 0, 0])
    pN[0, 3] = np.array([80, 15, 3, 2, 0, 0, 0, 0])
    pN[1, 0] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    pN[1, 1] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    pN[1, 2] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    pN[1, 3] = np.array([60, 27, 8, 3, 1, 1, 0, 0])
    pN[2, 0] = np.array([12, 33, 36, 10, 4, 3, 2, 0])
    pN[2, 1] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    pN[2, 2] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    pN[2, 3] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    pN[3, 0] = np.array([8, 25, 45, 12, 5, 3, 2, 0])
    pN[3, 1] = np.array([12, 33, 36, 10, 4, 3, 2, 0])
    pN[3, 2] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    pN[3, 3] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    pH[0, 0] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    pH[0, 1] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    pH[0, 2] = np.array([60, 27, 8, 3, 1, 1, 0, 0])
    pH[0, 3] = np.array([80, 15, 3, 2, 0, 0, 0, 0])
    pH[1, 0] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    pH[1, 1] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    pH[1, 2] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    pH[1, 3] = np.array([60, 27, 8, 3, 1, 1, 0, 0])
    pH[2, 0] = np.array([12, 33, 36, 10, 4, 3, 2, 0])
    pH[2, 1] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    pH[2, 2] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    pH[2, 3] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    pH[3, 0] = np.array([8, 25, 45, 12, 5, 3, 2, 0])
    pH[3, 1] = np.array([12, 33, 36, 10, 4, 3, 2, 0])
    pH[3, 2] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    pH[3, 3] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    pE[0, 0] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    pE[0, 1] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    pE[0, 2] = np.array([60, 27, 8, 3, 1, 1, 0, 0])
    pE[0, 3] = np.array([80, 15, 3, 2, 0, 0, 0, 0])
    pE[1, 0] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    pE[1, 1] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    pE[1, 2] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    pE[1, 3] = np.array([60, 27, 8, 3, 1, 1, 0, 0])
    pE[2, 0] = np.array([12, 33, 36, 10, 4, 3, 2, 0])
    pE[2, 1] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    pE[2, 2] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    pE[2, 3] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    pE[3, 0] = np.array([8, 25, 45, 12, 5, 3, 2, 0])
    pE[3, 1] = np.array([12, 33, 36, 10, 4, 3, 2, 0])
    pE[3, 2] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    pE[3, 3] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    return     {'N' : pN / 100.0, 'H': pH / 100.0, 'E': pE / 100.0}


def proba_table2():
    p = proba_table()
    r = {}
    for k, t in p.items():
        rp = np.zeros((4,4,4,4,8,8))
        for l1_a in range(4):
            for l1_d in range(4):
                for l2_a in range(4):
                    for l2_d in range(4):
                        for s1 in range(8):
                            for s2 in range(8):
                                rp[l1_a,l1_d,l2_a,l2_d,s1,s2] = t[l1_a, l2_d, s1] * t[l2_a, l1_d, s2]
        r[k] = rp.copy()
    return r


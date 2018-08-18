import numpy as np
import csv


def proba_table2(file='data_built_m_20180813.csv'):
    # construit la matrice de probabilités
    rp = np.zeros((4, 4, 4, 4, 8, 8))
    matrices = set()
    with open(file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if row['Aa'] == '':
                continue
            Aa, Ad, Ba, Bd = int(row['Aa']), int(row['Ad']), int(row['Ba']), int(row['Bd'])
            s1, s2 = int(row['s1']), int(row['s2'])
            matrices.add((Aa, Ad, Ba, Bd))
            p = float(row['p'])
            default_value = 0.03 / (1 + s1 + s2)**2
#            p = p if p > 0 else default_value
            p += default_value
            rp[Aa, Ad, Ba, Bd, min(s1, 7), min(s2, 7)] += p
    '''
    # lissage
    for Aa, Ad, Ba, Bd in matrices:
        sub1 = rp[Aa, Ad, Ba, Bd, :, :]
        sub = rp[Aa, Ad, Ba, Bd, :, :].copy()
        n, m = sub.shape
        w = 1000
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    sub[i, j] = (w * sub1[i, j] + sub1[i + 1, j] + sub1[i + 1, j + 1] + sub1[i, j + 1]) / (w + 3)
                    continue
                if i == 0 and j == m - 1:
                    sub[i, j] = (w * sub1[i, j] + sub1[i + 1, j] + sub1[i + 1, j - 1] + sub1[i, j - 1]) / (w + 3)
                    continue
                if i == n - 1 and j == 0:
                    sub[i, j] = (w * sub1[i, j] + sub1[i - 1, j] + sub1[i - 1, j + 1] + sub1[i, j + 1]) / (w + 3)
                    continue
                if i == n - 1 and j == m - 1:
                    sub[i, j] = (w * sub1[i, j] + sub1[i - 1, j] + sub1[i - 1, j - 1] + sub1[i, j - 1]) / (w + 3)
                    continue
                if i == 0:
                    sub[i, j] = (w * sub1[i, j] + sub1[i, j - 1] + sub1[i, j + 1] + sub1[i + 1, j - 1] +
                                 sub1[i + 1, j] + sub1[i + 1, j + 1]) / (w + 5)
                    continue
                if i == n - 1:
                    sub[i, j] = (w * sub1[i, j] + sub1[i, j - 1] + sub1[i, j + 1] + sub1[i - 1, j - 1] +
                                 sub1[i - 1, j] + sub1[i - 1, j + 1]) / (w + 5)
                    continue
                if j == 0:
                    sub[i, j] = (w * sub1[i, j] + sub1[i - 1, j] + sub1[i + 1, j] + sub1[i - 1, j + 1] + sub1[i, j] +
                                 sub1[i + 1, j + 1]) / (w + 5)
                    continue
                if j == m - 1:
                    sub[i, j] = (w * sub1[i, j] + sub1[i - 1, j] + sub1[i + 1, j] + sub1[i - 1, j - 1] +
                                 sub1[i, j - 1] + sub1[i + 1, j - 1]) / (w + 5)
                    continue
                sub[i, j] = (sub1[i - 1, j - 1] + sub1[i - 1, j] + sub1[i - 1, j + 1] +
                             sub1[i, j - 1] + w * sub1[i, j] + sub1[i, j + 1] +
                             sub1[i + 1, j - 1] + sub1[i + 1, j] + sub1[i + 1, j + 1]) / (w + 8)
        t = np.sum(sub)
        rp[Aa, Ad, Ba, Bd, :, :] = sub / t
    '''
    # renormalisaton à cause du petit 0.0001
    for Aa, Ad, Ba, Bd in matrices:
        t = np.sum(rp[Aa, Ad, Ba, Bd, :, :])
        rp[Aa, Ad, Ba, Bd, :, :] /= t
    return rp


def proba_table3():
    file = 'data_built_20180807.csv'
    vectors = {}
    with open(file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if row['Aa'] == '':
                continue
            k = (int(row['Aa']), int(row['Ad']), int(row['Ba']), int(row['Bd']))
            bm = [float(row['A' + str(i)]) for i in range(8)]
            br = [float(row['D' + str(i)]) for i in range(8)]
            # Remplace les 0 par un petit nombre
            bm = [x if x > 0 else 0.1 for x in bm]
            br = [x if x > 0 else 0.1 for x in br]
            # renormalise à 1
            t = sum(x for x in bm)
            bm = [x / t for x in bm]
            t = sum(x for x in br)
            br = [x / t for x in br]
            vectors[k] = (bm, br)
    # construit la matrice de probabilités
    rp = np.zeros((4, 4, 4, 4, 8, 8))
    for l1_a in range(4):
        for l1_d in range(4):
            for l2_a in range(4):
                for l2_d in range(4):
                    bm, br = vectors[(l1_a, l1_d, l2_a, l2_d)]
                    for s1 in range(8):
                        for s2 in range(8):
                            rp[l1_a, l1_d, l2_a, l2_d, s1, s2] = bm[s1] * br[s2]
    return rp


def proba_table():
    p_e = np.zeros((4, 4, 8))
    p_n = np.zeros((4, 4, 8))
    p_h = np.zeros((4, 4, 8))
    p_n[0, 0] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    p_n[0, 1] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    p_n[0, 2] = np.array([60, 27, 8, 3, 1, 1, 0, 0])
    p_n[0, 3] = np.array([80, 15, 3, 2, 0, 0, 0, 0])
    p_n[1, 0] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    p_n[1, 1] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    p_n[1, 2] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    p_n[1, 3] = np.array([60, 27, 8, 3, 1, 1, 0, 0])
    p_n[2, 0] = np.array([12, 33, 36, 10, 4, 3, 2, 0])
    p_n[2, 1] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    p_n[2, 2] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    p_n[2, 3] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    p_n[3, 0] = np.array([8, 25, 45, 12, 5, 3, 2, 0])
    p_n[3, 1] = np.array([12, 33, 36, 10, 4, 3, 2, 0])
    p_n[3, 2] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    p_n[3, 3] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    p_h[0, 0] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    p_h[0, 1] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    p_h[0, 2] = np.array([60, 27, 8, 3, 1, 1, 0, 0])
    p_h[0, 3] = np.array([80, 15, 3, 2, 0, 0, 0, 0])
    p_h[1, 0] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    p_h[1, 1] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    p_h[1, 2] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    p_h[1, 3] = np.array([60, 27, 8, 3, 1, 1, 0, 0])
    p_h[2, 0] = np.array([12, 33, 36, 10, 4, 3, 2, 0])
    p_h[2, 1] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    p_h[2, 2] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    p_h[2, 3] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    p_h[3, 0] = np.array([8, 25, 45, 12, 5, 3, 2, 0])
    p_h[3, 1] = np.array([12, 33, 36, 10, 4, 3, 2, 0])
    p_h[3, 2] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    p_h[3, 3] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    p_e[0, 0] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    p_e[0, 1] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    p_e[0, 2] = np.array([60, 27, 8, 3, 1, 1, 0, 0])
    p_e[0, 3] = np.array([80, 15, 3, 2, 0, 0, 0, 0])
    p_e[1, 0] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    p_e[1, 1] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    p_e[1, 2] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    p_e[1, 3] = np.array([60, 27, 8, 3, 1, 1, 0, 0])
    p_e[2, 0] = np.array([12, 33, 36, 10, 4, 3, 2, 0])
    p_e[2, 1] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    p_e[2, 2] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    p_e[2, 3] = np.array([40, 38, 13, 4, 2, 1, 1, 1])
    p_e[3, 0] = np.array([8, 25, 45, 12, 5, 3, 2, 0])
    p_e[3, 1] = np.array([12, 33, 36, 10, 4, 3, 2, 0])
    p_e[3, 2] = np.array([16, 42, 27, 7, 4, 2, 1, 1])
    p_e[3, 3] = np.array([20, 50, 18, 5, 3, 2, 1, 1])
    return {'N': p_n / 100.0, 'H': p_h / 100.0, 'E': p_e / 100.0}

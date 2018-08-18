from history_analysis.history import compute_rebuilt_matrices
from calage_backtesting import simulate_bet_over
from collections import OrderedDict

data_from_year = 2011
data_to_year = 2018

from_year = 2015
to_year = 2018

full_data = {}

for t1 in range(1,130,20):
    for t2 in range(1, 130, 20):
        compute_rebuilt_matrices(data_from_year, data_to_year, 'data_built_m.csv',
                                 threshold_1=t1,
                                 threshold_2=t2,
                                 printing=False)
        play_scores, final_model = simulate_bet_over(data_from_year, data_to_year, from_year, to_year,
                                                     proba_table_file='data_built_m.csv',
                                                     printing=False)
        print('Threshold 1,2 = {}, {}'.format(t1, t2))
        for season, r in play_scores.items():
            print("Season {:^5} Total {:^5.0f} {:^5.3f} Prono {:^5.0f} {:^5.3f} Exact {:^5.0f} {:^5.3f} ".format(
                season, r['total'][0], r['total'][1], r['prono'][0], r['prono'][1], r['exact'][0], r['exact'][1]
            ))
        full_data[(t1, t2)] = play_scores


first_row = False
for (t1, t2), scores in full_data.items():
    row = OrderedDict()
    row['T1'] = str(t1)
    row['T2'] = str(t2)
    for season, results in scores.items():
        row[str(season) + '_total'] = str(results['total'][0])
        row[str(season) + '_prono'] = str(results['prono'][0])
        row[str(season) + '_exact'] = str(results['exact'][0])
    if not first_row:
        first_row = True
        print(",".join(row.keys()))
    print(','.join(row.values()))
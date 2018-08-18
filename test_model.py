from modelattackdefense import ModelAttackDefense
import numpy as np

'''
model = ModelAttackDefense(n_teams=2, options={'teams': ['Toulouse', 'Monaco']})
model.account_for(0, 1, 1, 1, 'N')
model.print()
print()
'''

model = ModelAttackDefense(n_teams=2,
                           options={
                               'teams': ['Toulouse', 'Monaco'],
                               'attack_vector':[np.array([1.0,0,0,0]), np.array([0,0,0,1.0])],
                               'defense_vector': [np.array([1.0,0,0,0]), np.array([0.0, 0.0, 0.0, 1.0])]
                           })
model.print()
model.account_for2(0, 1, 3, 1)
model.account_for2(0, 1, 3, 1)
model.account_for2(0, 1, 3, 1)
model.account_for2(0, 1, 3, 1)
model.account_for2(0, 1, 3, 1)
model.print()
print()

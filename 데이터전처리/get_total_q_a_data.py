import pandas as pd

qa_base = pd.read_csv('/home/dacon_project/Data/Load_data/Q_A.csv')
qa_worked = pd.read_csv('/home/dacon_project/Data/Load_data/Q_A_utf-8.csv')
print('qa_base',len(qa_base))
print('dq_worked',len(qa_worked))

total = pd.concat([qa_base,qa_worked])
total.to_csv('/home/dacon_project/Data/Load_data/total_Q_A.csv', index=False)


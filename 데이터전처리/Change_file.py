import pandas as pd
import openpyxl
df = pd.read_csv('/home/dacon_project/Data/Load_data/Multi_Q_A/Multi_Q_A.csv')
df.to_excel('/home/dacon_project/Data/Load_data/Multi_Q_A/Multi_Q_A.xlsx', index=False)
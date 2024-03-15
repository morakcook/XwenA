import pandas as pd
import pandas as pd
from tqdm import tqdm

# instruction 데이터 세트 설정
dataset_name = '/home/dacon_project/Data/Load_data/Test_Q_A/Test_Q_A.csv'
formatted_data = {}
list1 = []
list2 = []
df = pd.read_csv(dataset_name)
for i in range(len(df)):
    if i % 2 == 0:
        list1.append(df.iloc[i]['Q'])
        list2.append(df.iloc[i]['A'])
print('Done.')
formatted_data['Q'] = list1
formatted_data['A'] = list2
df = pd.DataFrame(formatted_data)
df.to_csv('/home/dacon_project/Data/Load_data/작업할데이터.csv', encoding='utf-8', errors='replace', index=False)
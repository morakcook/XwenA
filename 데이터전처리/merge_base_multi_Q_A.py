import pandas as pd

# BASE
dataset_name1 = '/home/dacon_project/Data/Load_data/Test_Q_A/Test_Q_A.csv'
data1 = pd.read_csv(dataset_name1)
# MULTI
dataset_name2 = '/home/dacon_project/Data/Load_data/Multi_Q_A/Multi_Q_A.csv'
data2 = pd.read_csv(dataset_name2)
# 필요한 열을 문자열로 변환
for col in ['Q', 'A']:
    data1[col] = data1[col].astype(str)
    data2[col] = data2[col].astype(str)

# 데이터 포맷팅 및 토크나이징
formatted_data = {}
list1 = []
list2 = []
for i in range(len(data1)):
    if i % 2 != 0:
        list1.append(data1.iloc[i]['Q'])
        list2.append(data1.iloc[i]['A'])
    else:
        list1.append(data2.iloc[int(i/2)]['Q'])
        list2.append(data2.iloc[int(i/2)]['A'])
print('Done.')
formatted_data['Q'] = list1
formatted_data['A'] = list2
df = pd.DataFrame(formatted_data)
df.to_csv('/home/dacon_project/Data/Load_data/Base_Multi_Q_A/BASE_MULTI_Q_A_utf-8.csv', encoding='utf-8', errors='replace', index=False)
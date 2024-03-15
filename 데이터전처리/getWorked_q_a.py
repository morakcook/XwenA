import pandas as pd

# instruction 데이터 세트 설정
dataset_name = '/home/dacon_project/Data/Working_data/데이콘 데이터 증강 작업 - 엑셀gpt데이터증강 정리.csv'

df = pd.read_csv(dataset_name)
# 특정 문자열을 빈 문자열로 대체 (예: '"문자', '"이 문자' 제거)
df.dropna(inplace=True)
df = df.apply(lambda x: x.str.replace('"', '').str.replace('"', ''), axis=1)
df.to_csv(dataset_name, index=False)
import pandas as pd
from tqdm import tqdm
# 데이터 로드
data = pd.read_csv(dataset_name)

# 필요한 열을 문자열로 변환
for col in ['Q1', 'Q2', 'A1', 'A2']:
    data[col] = data[col].astype(str)

# 데이터 포맷팅 및 토크나이징
formatted_data = {}
list1 = []
list2 = []
for _, row in tqdm(data.iterrows()):
    for num in range(2,3):
        list1.append(row[f'Q{num}'])
        list2.append(row[f'A{num}'])
print('Done.')
formatted_data['Q'] = list1
formatted_data['A'] = list2
df = pd.DataFrame(formatted_data)
df.to_csv('/home/dacon_project/Data/Load_data/Quest2_Q_A/Quset2_Q_A_utf-8.csv', encoding='utf-8', errors='replace', index=False)
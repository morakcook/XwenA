# Local 작업

1. CheckPoints : 체크포인트들을 저장하는 폴더
2. Data : 데이터들을 저장합니다.
    2-1. Base_data : 기존에 제공해준 train, test csv파일을 저장합니다.
    2-2. Working_data : 증강한 데이터를 저장합니다.
    2-3. Load_data : 데이터 전처리 작업한 데이터를 저장합니다.
3. Generation : RAG방식을 이용한 텍스트 생성시에 사용됩니다.
4. Myenv : 가상환경입니다.
5. Submission : Generation의 결과물을 저장합니다.
6. Training : 학습을 하는 폴더입니다.
7. 데이터전처리 : 데이터전처리 파일이 있습니다.

# 테스트 결과
1epoch기준
1. train에서 노이즈제거
2. 엑셀gpt데이터 증강
3. 엑셀gpt데이터증강-train가공
4. 엑셀gpt데이터증강-논문에서추출한것만
5. 엑셀gpt데이터증강 정리 - 질문1
6. 엑셀gpt데이터증강 정리 - 질문2
7. 엑셀gpt데이터증강 정리 - 전체

TEST
1. train노이즈/train작업한것 : 데이터수:1161, validaiton_loss:  4.209367275238037
2. 엑셀gpt데이터증강 : 데이터수:1530, validaiton_loss: 3.4904487133026123
3. 엑셀gpt데이터증강-train가공 : 데이터수:1155,, validaiton_loss: 3.546346426010132
4. 엑셀gpt데이터증강-논문에서추출한것만 : 데이터수:374, validaiton_loss: 4.066420078277588
5. 엑셀gpt데이터증강 정리 - 질문1 : 데이터수:763, validaiton_loss: 3.9451777935028076
6. 엑셀gpt데이터증강 정리 - 질문2 : 데이터수:763, validaiton_loss: 3.792416572570801
7. 엑셀gpt데이터증강 정리 - 전체 : 데이터수:1526, validaiton_loss: 3.4450669288635254

# 6번 10epoch으로 모델생성 드리고 -> 
# 기본traindata + 7번 더해서 10epoch으로 모델 생성

# Q2_Q_A.CSV만들고 5+5 로 작업
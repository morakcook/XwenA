# Dacon에서 한솔데코 주관 질의응답 chatBot Project입니다.

## 주제
도배하자 관련 질의응답 챗봇을 만드는 프로젝트입니다.

### 설명
데이콘에서 제공한 BaseLine기반으로 추가적인 모델+학습을 통하여 한솔데코에서 제공한 질문에 대한 답변을 생성하여 한솔데코의 정답과 CosineSimilarity를 비교하여 점수를 측정합니다.
저희 팀은 아래의 방식으로 진행하였습니다. 

- 모델: 42.dot(LLaMa)
    - 설명: 42.dot화사에서 LLaMa기반으로 대규모 한국어 학습을 진행한 모델을 기반으로 진행하였습니다.
    - 
- 진행: PEFT + RAG + 양자화
    - PEFT(Parameter-Efficient Fine-Tuning of Billion-Scale Models on Low-Resource Hardware): 적은 수의 파라미터를 학습하는것만으로 모델 전체를 파인튜닝하는 것과 유사한 효과로 QLORA방식으로 진행되었습니다.
    - RAG(Retrieval-Augmented Generation): 답변을 생성함에 추가적인 자료(Retriver)를 얻는 RAG방식을 사용하여 진행하였습니다.
    - 양자화(Quantizaton): llm모델을 학습함에 있어 높은 gpu사양을 필요로 함으로 양자화를 적용하여 gtx2060의 환경에서 충분한 학습을 진행하였습니다.
    - 
- 결과: 1367명(500팀)중 74등의 결과를 만들었습니다.
- 과제: 충분히 많은 데이터를 사용했음에도 consineSimilarity가 높아지지 않았습니다.
- 해답: 이는 대회이후 GPT API, GEMINI API를 사용한 데이터와 사용하지 않은 데이터를 동일한 학습을 진행한 체크포인트를 기준으로 cosinesimilarity를 측정하여 한솔데코의 답변형식(도배하자 전문가의 답변이 아닙니다)과의 유사도가 적음으로 인한 문제점을 검증하였습니다.

## 프로젝트 시나리오

### 1. 데이터 증강하기
- **설명**: 데이콘에서 제공한 기본 train 데이터을 베이스로 GPT API, GEMINI API를 사용하여 데이터를 증강하였습니다.

### 2. PEFT(Parameter-Efficient Fine-Tuning of Billion-Scale Models on Low-Resource Hardware)
- **모델**: 42.dot(LLaMa), 양자화(Quantizaton)
- **학습 여부**: 학습 진행
- **설명**: 42.dot모델을 사용하며 양자화를 적용해 GTX2060의 환경에서 학습을 진행할수 있습니다.
- **이해**: 학습을 통하여 기존 42.dot제공 모델이 도배하자와 관련된 질의응답이 보다 용이하게 생성하도록 진행하였습니다.

### 3. RAG(Retrieval-Augmented Generation)
- **사용**: 42.dot(LLaMa)
- **설명**: 기존 가공한 데이터(질의웅답 CSV)를 Retriver로 사용하여 답변이 한솔데코의 답변에 더욱 유사하게 나올수 있도록 진행하였습니다.
  
### 4. 최종 결과 확인하기
- **설명**: 생성된 답변을 Embedding Vector로 변환하여 한솔데코 내부의 답변과 Cosine유사도를 측정하여 결과를 확인합니다.
- **이해**:
    1. 도배하자와 관련된 전문적인 답변이 필요합니다.
    2. 한솔데코의 답변 형식과 유사한 답변 형식이 높은 점수를 받습니다.
    3. 답변형식에 템픞릿 혹은 질문의 출현빈도가 낮을수록 좋은 답변입니다.


## 진행화면
<img width="80%" src="https://github.com/morakcook/XwenA/blob/main/static/Images/dacon_project%EC%9B%B9%EB%8D%B0%EB%AA%A8.png"/>

### 진행결과
<img width="80%" src="https://github.com/morakcook/XwenA/blob/main/static/Images/%EB%8D%B0%EC%9D%B4%EC%BD%98%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%EA%B2%B0%EA%B3%BC.png">

### 진행환경
- unbuntu로 linux환경에서 vscode로 진행

## 사용하는 모델 및 라이센스 정의

### 1. 42.dot(LLaMa)
- **원본 출처**: [42dot](https://github.com/42dot/42dot_LLM)
- **라이센스**:
  - **코드 라이센스**: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)
  - **모델 가중치 라이센스**: 직접 학습을 통해 취득
- **사용 목적**: 직접학습과 학습한 체크포인트를 통해 질의응답 챗봇 생성
- **수정 및 통합 사항**: 특정 데이터 학습 진행 및 양자화 적용.


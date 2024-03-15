import os  # os 모듈 운영체제와 상호 작용할 수 있는 기능을 제공
import torch # PyTorch 라이브러리로, 주로 딥러닝과 머신러닝 모델을 구축, 학습, 테스트하는 데 사용
from datasets import load_dataset  # 데이터셋을 쉽게 불러오고 처리할 수 있는 기능을 제공
from transformers import (
    AutoModelForCausalLM, # 인과적 언어 추론(예: GPT)을 위한 모델을 자동으로 불러오는 클래스
    AutoTokenizer, # 입력 문장을 토큰 단위로 자동으로 잘라주는 역할
    BitsAndBytesConfig, # 모델 구성
    HfArgumentParser,  # 파라미터 파싱
    TrainingArguments,  # 훈련 설정
    pipeline,  # 파이프라인 설정
    logging,  #로깅을 위한 클래스
)
# 모델 튜닝을 위한 라이브러리
from peft import LoraConfig, PeftModel
from trl import SFTTrainer
from sklearn.model_selection import train_test_split

model_name = '42dot/42dot_LLM-SFT-1.3B'

checkpoint = "/home/dacon_project/CheckPoints/Total_best_10epoch_Qlora"


compute_dtype = getattr(torch, "float16")

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,  
    bnb_4bit_quant_type="nf4", 
    bnb_4bit_compute_dtype=compute_dtype,  
    bnb_4bit_use_double_quant=False, 
)

base_model = AutoModelForCausalLM.from_pretrained(
    # 로드할 모델 이름
    model_name,  
    # QLoRA 설정
    quantization_config=bnb_config,  
    # 모델을 로드할 장치 지정
    device_map={"": 0}  
)

# PeftModel 클래스를 이용하여 기존 모델에 새로운 모델을 추가합니다.
model = PeftModel.from_pretrained(base_model, checkpoint)

# 모델의 리소스를 정리합니다.
model = model.merge_and_unload()

print(model)
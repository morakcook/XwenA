import os
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
)
from peft import LoraConfig, PeftModel
from trl import SFTTrainer
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import pipeline

# 모델 이름 및 파일 경로 설정
model_name = '42dot/42dot_LLM-SFT-1.3B'
new_model = "/content/gdrive/MyDrive/TeamProjects/Dacon_Project/Hansol/1.도배하자Project/Test_10epoch_Qlora"

# 모델 및 토크나이저 초기화
base_model = AutoModelForCausalLM.from_pretrained(model_name, low_cpu_mem_usage=True, return_dict=True, torch_dtype=torch.float16)
model = PeftModel.from_pretrained(base_model, new_model)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# CUDA 사용 가능 여부 확인 및 모델을 GPU로 이동
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
print(f"Using device: {device}")

# CSV 파일에서 데이터 로드
loader = CSVLoader(file_path='train_data1.csv', encoding='utf-8')
data = loader.load()

# 임베딩 모델 설정 및 FAISS 벡터 스토어 생성
modelPath = "distiluse-base-multilingual-cased-v1"
embeddings = HuggingFaceEmbeddings(model_name=modelPath, model_kwargs={'device':device}, encode_kwargs={'normalize_embeddings': False})
db = FAISS.from_documents(data, embedding=embeddings)
db.save_local("faiss_index")
retriever = db.as_retriever(search_kwargs={"k": 4})

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512, device=0) # device=0: GPU 사용 설정
hf = HuggingFacePipeline(pipeline=pipe)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

template = """
From an architectural expert's perspective, please review the context below and respond to the question strictly within 500 characters. Ensure that your response is in Korean and do not repeat the same words or phrases. Only the answer to the provided question is required.
Context: {context}
Question: {question}
Answer:
"""

custom_rag_prompt = PromptTemplate.from_template(template)
rag_chain = ({"context": retriever | format_docs, "question": RunnablePassthrough()} | custom_rag_prompt | hf | StrOutputParser())

for chunk in rag_chain.stream("도배지에 녹은 자국이 발생하는 주된 원인과 그 해결 방법은 무엇인가요? 건축 전문가적 입장에서 300자 이내로 요약해서 답변해주세요."):
    print(chunk, end="", flush=True)

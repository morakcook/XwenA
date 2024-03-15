import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import concurrent.futures

def generate_text(model, tokenizer, text, max_length=200, num_return_sequences=1):
    with torch.no_grad():
        tokens = tokenizer(text, return_tensors="pt")
        generated_ids = model.generate(
            tokens["input_ids"],
            max_length=max_length,
            num_return_sequences=num_return_sequences,
            pad_token_id=tokenizer.eos_token_id
        )
        generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return generated_text

def main(prompt):
    model_name = '42dot/42dot_LLM-SFT-1.3B'
    new_model = "/home/dacon_project/CheckPoints/10epoch_Qlora"

    # 모델과 토크나이저 불러오기
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    
    base_model = AutoModelForCausalLM.from_pretrained(
        model_name,
        low_cpu_mem_usage=True,
        return_dict=True
    )
    model = PeftModel.from_pretrained(base_model, new_model)


    # 다중 스레딩을 사용하여 병렬 처리
    num_threads = min(os.cpu_count(), 4)  # 사용 가능한 CPU 코어 수의 최대값을 4로 제한합니다.
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for _ in range(num_threads):
            futures.append(executor.submit(generate_text, model, tokenizer, prompt))
        for future in concurrent.futures.as_completed(futures):
            generated_text = future.result()
            print(f"Generated text: {generated_text}")
    return generated_text

if __name__ == "__main__":
    main()

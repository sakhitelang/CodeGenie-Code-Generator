from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
import time
def generate_code(prompt):
    model_id = "codellama/CodeLlama-7b-hf"
    tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)
    start = time.time()
    pipeline = transformers.pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    sequences = pipeline(
            prompt,
            do_sample=True,
            temperature=0.1,
            top_p=0.9,
            num_return_sequences=1,
            eos_token_id=tokenizer.eos_token_id,
            max_length=128,
            truncation=True
        )
    p = ''
    for seq in sequences:
        p = p + seq['generated_text']
    #print(p)
    end = time.time()
    return p, start, end

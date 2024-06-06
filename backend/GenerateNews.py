from transformers import AutoTokenizer, AutoModelForCausalLM
import re

# Load tokenizer and model
model_name = "EleutherAI/gpt-neo-125m"  # or "EleutherAI/gpt-neo-125M" or your preferred model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained("AhmedDaniyal/NewsGen")

# Function to generate text using different strategies
def generate_text(input_text, strategy="top_p", max_length=1000, min_length=200, top_p=0.9, top_k=50, temperature=0.7, num_beams=5, repetition_penalty=1.5):
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    
    if strategy == "top_p":
        output = model.generate(input_ids, max_length=max_length, min_length=min_length, do_sample=True, top_p=top_p, temperature=temperature, repetition_penalty=repetition_penalty)
    elif strategy == "top_k":
        output = model.generate(input_ids, max_length=max_length, min_length=min_length, do_sample=True, top_k=top_k, temperature=temperature, repetition_penalty=repetition_penalty)
    elif strategy == "beam_search":
        output = model.generate(input_ids, max_length=max_length, min_length=min_length, num_beams=num_beams, no_repeat_ngram_size=3, repetition_penalty=repetition_penalty)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")
    
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
    return post_process_text(decoded_output)

# Function to clean and improve generated text
def post_process_text(text):
    # Remove duplicate sentences
    sentences = re.split(r'(?<=[.!?]) +', text)
    unique_sentences = list(dict.fromkeys(sentences))
    cleaned_text = ' '.join(unique_sentences)
    
    # Additional cleaning can be added here
    return cleaned_text

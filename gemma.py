import torch
from transformers import pipeline, BitsAndBytesConfig
from huggingface_hub import login





pipe = pipeline(
    "text-generation",
    model="google/gemma-2-2b-it",
    model_kwargs={"torch_dtype": torch.bfloat16, "load_in_4bit": True},
    #device="cuda",   #replace with "mps" to run on a Mac device
)

messages = [
    {"role": "user", "content": "Me explique em português o que é o um carcinoma."},
]

outputs = pipe(messages, max_new_tokens=256)
assistant_response = outputs[0]["generated_text"][-1]["content"].strip()
print(assistant_response)
# Ahoy, matey! I be Gemma, a digital scallywag, a language-slingin' parrot of the digital seas. I be here to help ye with yer wordy woes, answer yer questions, and spin ye yarns of the digital world.  So, what be yer pleasure, eh? 🦜

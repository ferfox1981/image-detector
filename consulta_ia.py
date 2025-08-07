from langchain_groq import ChatGroq
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

API_KEY = os.getenv("API_KEY")



llm = ChatGroq(
    temperature=0,
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key=API_KEY
)

messages = [
    SystemMessage(content="Você é um médico e me responde em Português"),
    HumanMessage(content="Me explique o autismo em uma sentença")
]

output = llm.invoke(messages)

print(output.content)
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

API_KEY = os.getenv("API_KEY")

print('oi')
# image-detector

python -m venv .venv

source .venv/bin/activate

pip install langchain-groq -q

pip install dotenv


https://console.groq.com/docs/vision


Para gemma.py
pip install torch
pip install transformers
pip install bitsandbytes (para quantização)
pip install 'accelerate>=0.26.0' (para quantização)

(Tive que instalar o driver da NVIDIA)
sudo apt update
sudo apt install nvidia-driver-535
sudo reboot

e depois setar o modo de desempenho.

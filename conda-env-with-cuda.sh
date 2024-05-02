#!/bin/bash

pip install ipykernel ipywidgets &&
pip install pandas pyarrow &&
conda install cudatoolkit=11.8 &&
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 && 
pip install transformers peft accelerate
pip install trl xformers wandb datasets einops gradio sentencepiece bitsandbytes

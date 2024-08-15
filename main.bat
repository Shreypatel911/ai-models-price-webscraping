@echo off

echo Installing dependencies from requirements.txt
pip install -r requirements.txt

python openai-model.py

python aws-model.py

python gcp-model.py

echo All scripts executed successfully.

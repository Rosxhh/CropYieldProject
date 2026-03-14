import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(r'c:\Users\acer\Desktop\CropYieldProject\crop_project\.env')
key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=key)

print("Emergency Model Scan...")
models_to_test = [
    'gemini-1.5-flash-8b', 
    'gemini-flash-lite-latest',
    'gemini-2.5-flash-lite',
    'gemma-3-4b-it',
    'gemma-2-9b-it',
    'gemma-2-2b-it'
]

for name in models_to_test:
    try:
        model = genai.GenerativeModel(name)
        response = model.generate_content("Hi", request_options={"timeout": 7})
        print(f"WORKS: {name}")
    except Exception as e:
        print(f"FAILED ({name}): {str(e)[:50]}...")

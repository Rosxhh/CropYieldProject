import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(r'c:\Users\acer\Desktop\CropYieldProject\crop_project\.env')
key = os.getenv("GEMINI_API_KEY")

print(f"Checking Key: {key[:10]}...")

try:
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content("Hello, respond with ONE word: 'HEALTHY' if you can read this.")
    print(f"RESULT: {response.text.strip()}")
except Exception as e:
    print(f"FAILURE: {str(e)}")

from django.shortcuts import render
import os
import json
import re
import time
from PIL import Image
from dotenv import load_dotenv
from .recommendations import SOIL_DATA

load_dotenv()

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

def soil_predict(request):
    if request.method == "POST" and request.FILES.get("image"):
        uploaded_file = request.FILES["image"]
        try:
            img = Image.open(uploaded_file)
            # Resize image to save bandwidth and stay within API limits
            img.thumbnail((800, 800))
            
            result_class = "Analysis Failed"
            confidence = 0.0
            characteristics = ["Unable to analyze soil at this moment."]
            recommended_crops = []
            tips = ""
            
            token = os.getenv("GEMINI_API_KEY")
            if token and GEMINI_AVAILABLE:
                genai.configure(api_key=token)
                
                # ULTIMATE QUOTA-RESISTANT FALLBACK CHAIN FOR VISION
                model_names = [
                    'gemini-1.5-flash-8b', 
                    'gemini-flash-lite-latest',
                    'gemini-1.5-flash',
                    'gemma-3-4b-it'
                ]
                
                prompt = """
                Analyze this image and identify the primary soil type from these 6 categories ONLY:
                [Sandy, Clay, Loamy, Silty, Peaty, Chalky].
                
                Respond strictly in this JSON format:
                {"type": "TheMatchedType", "confidence": 95.5}
                
                If it does not look like soil, return:
                {"type": "Unknown", "confidence": 0.0}
                """
                
                success = False
                last_error = ""
                
                for m_name in model_names:
                    try:
                        model = genai.GenerativeModel(m_name)
                        
                        # Handle Gemma vs Gemini multimodal syntax
                        if "gemma" in m_name:
                            # Prepend prompt for Gemma vision
                            response = model.generate_content([prompt, img], request_options={"timeout": 20})
                        else:
                            response = model.generate_content([prompt, img], request_options={"timeout": 20})
                        
                        if response and response.text:
                            # Extract JSON
                            json_str = response.text
                            match = re.search(r'\{.*\}', json_str, re.DOTALL)
                            if match:
                                json_str = match.group(0)
                                
                            data = json.loads(json_str)
                            type_extracted = data.get("type", "Unknown")
                            confidence = float(data.get("confidence", 0.0))
                            
                            if type_extracted in SOIL_DATA:
                                result_class = type_extracted
                                soil_info = SOIL_DATA[type_extracted]
                                characteristics = soil_info["characteristics"]
                                recommended_crops = soil_info["crops"]
                                tips = soil_info["tips"]
                                success = True
                                break
                            elif type_extracted == "Unknown":
                                result_class = "Not Recognized as Soil"
                                characteristics = ["The uploaded image does not appear to be soil. Please try again with a clear photo of the ground."]
                                success = True
                                break
                    except Exception as e:
                        print(f"SOIL FALLBACK DEBUG: {m_name} failed: {str(e)[:100]}")
                        last_error = str(e)
                        continue
                
                if not success:
                    result_class = "Service Busy"
                    characteristics = [f"Our AI specialists are currently at capacity. Please try again in 30 seconds. 🚜"]
                    # If it was a quota error specifically, show a cleaner message
                    if "429" in last_error:
                        characteristics = ["Agricultural AI systems are under heavy load. Retrying in 30 seconds... 🌾"]

            else:
                 result_class = "Configuration Error"
                 characteristics = ["AI access not configured. Please check API settings."]
            
            context = {
                "result": result_class,
                "confidence": f"{confidence:.1f}%",
                "characteristics": characteristics,
                "recommended_crops": recommended_crops,
                "tips": tips,
                "image_name": uploaded_file.name
            }
            
            return render(request, "soil_result.html", context)
            
        except Exception as e:
            return render(request, "soil_upload.html", {"error": f"Upload Error: {str(e)}"})

    return render(request, "soil_upload.html")

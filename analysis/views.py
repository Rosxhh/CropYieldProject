import os
import joblib
import numpy as np
from django.shortcuts import render
from django.conf import settings
from recommend.crop_info import get_crop_data

# Load Models
crop_model_path = os.path.join(settings.BASE_DIR, "crop1.pkl")
yield_model_path = os.path.join(settings.BASE_DIR, "yield_model.pkl")

# Pre-load models for performance
try:
    crop_model = joblib.load(crop_model_path)
    yield_model = joblib.load(yield_model_path)
except Exception as e:
    print(f"Error loading models: {e}")
    crop_model = None
    yield_model = None

def smart_analysis(request):
    if request.method == "POST":
        if not crop_model or not yield_model:
            return render(request, "smart_analysis.html", {
                "error": "One or more prediction models are missing on the server."
            })

        try:
            # 1. Extract inputs (Unified for both models)
            nitrogen = float(request.POST.get("nitrogen") or 0)
            phosphorus = float(request.POST.get("phosphorus") or 0)
            potassium = float(request.POST.get("potassium") or 0)
            temperature = float(request.POST.get("temperature") or 0)
            humidity = float(request.POST.get("humidity") or 0)
            ph = float(request.POST.get("ph") or 0)
            rainfall = float(request.POST.get("rainfall") or 0)
            area = float(request.POST.get("area") or 1.0) # Default to 1 hectare if not provided

            # 2. Prediction: Best Crop
            # Crop model expects: N, P, K, temp, hum, ph, rain
            crop_input = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
            crop_prediction = crop_model.predict(crop_input)
            crop_info = get_crop_data(int(crop_prediction[0]))

            # 3. Prediction: Expected Yield
            # Yield model expects: N, P, K, temp, hum, ph, rain, Area
            yield_input = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall, area]])
            yield_prediction = yield_model.predict(yield_input)
            total_yield = round(yield_prediction[0], 2)
            yield_ph = round(total_yield / area, 2) if area > 0 else 0

            # 4. Prepare Context
            context = {
                "result": True,
                "crop": crop_info['name'],
                "crop_details": crop_info,
                "yield": total_yield,
                "yield_ph": yield_ph,
                "inputs": {
                    "nitrogen": nitrogen,
                    "phosphorus": phosphorus,
                    "potassium": potassium,
                    "temperature": temperature,
                    "humidity": humidity,
                    "ph": ph,
                    "rainfall": rainfall,
                    "area": area
                }
            }
            return render(request, "smart_analysis.html", context)

        except ValueError:
            return render(request, "smart_analysis.html", {
                "error": "Please enter valid numeric values for all fields."
            })
        except Exception as e:
            return render(request, "smart_analysis.html", {
                "error": f"An unexpected error occurred during analysis: {str(e)}"
            })

    return render(request, "smart_analysis.html")

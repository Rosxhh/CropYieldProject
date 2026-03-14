import os
import joblib
import numpy as np
from django.shortcuts import render
from django.conf import settings
from .models import YieldPrediction

# Load Model
model_path = os.path.join(settings.BASE_DIR, "yield_model.pkl")
model = joblib.load(model_path)

def predict_yield(request):
    if request.method == "POST":
        try:
            # Extract basic features
            rainfall = float(request.POST.get("rainfall") or 0)
            temperature = float(request.POST.get("temperature") or 0)
            area = float(request.POST.get("area") or 0)
            
            # Extract new agricultural features
            nitrogen = float(request.POST.get("nitrogen") or 0)
            phosphorus = float(request.POST.get("phosphorus") or 0)
            potassium = float(request.POST.get("potassium") or 0)
            humidity = float(request.POST.get("humidity") or 0)
            ph = float(request.POST.get("ph") or 0)

            # Model input: X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall', 'Area']]
            # Order must match training: N, P, K, temp, humidity, ph, rain, area
            input_data = np.array([[
                nitrogen, 
                phosphorus, 
                potassium, 
                temperature, 
                humidity, 
                ph, 
                rainfall, 
                area
            ]])

            prediction = model.predict(input_data)
            total_yield = round(prediction[0], 2)
            yield_per_hectare = round(total_yield / area, 2) if area > 0 else 0

            # SAVE TO DATABASE (Updating model if necessary, for now use existing fields or placeholders)
            # YieldPrediction.objects.create(...)
            
            # Pass all data to result.html for visualization
            context = {
                "yield": total_yield,
                "yield_ph": yield_per_hectare,
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

            return render(request, "result.html", context)

        except Exception as e:
            return render(request, "index.html", {
                "error": f"Numeric analysis failed: {str(e)}"
            })

    return render(request, "index.html")
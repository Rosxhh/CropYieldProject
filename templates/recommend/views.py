import os
import joblib
import numpy as np
from django.shortcuts import render
from django.conf import settings


# --------------------------------------------------
# LOAD MODEL (runs once when server starts)
# --------------------------------------------------
model_path = os.path.join(settings.BASE_DIR, "crop1.pkl")

if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None
    print("Recommendation model file not found!")


# --------------------------------------------------
# VIEW FUNCTION
# --------------------------------------------------
def recommend_crop(request):

    if request.method == "POST":

        if model is None:
            return render(request, "recommend.html", {
                "error": "Model file not found!"
            })

        try:
            # Get form values safely
            nitrogen = float(request.POST.get("nitrogen", 0))
            phosphorus = float(request.POST.get("phosphorus", 0))
            potassium = float(request.POST.get("potassium", 0))
            temperature = float(request.POST.get("temperature", 0))
            humidity = float(request.POST.get("humidity", 0))
            ph = float(request.POST.get("ph", 0))
            rainfall = float(request.POST.get("rainfall", 0))

            # Create input array
            input_data = np.array([[
                nitrogen,
                phosphorus,
                potassium,
                temperature,
                humidity,
                ph,
                rainfall
            ]])

            # Predict
            prediction = model.predict(input_data)
            from .crop_info import get_crop_data
            crop_data = get_crop_data(int(prediction[0]))

            return render(request, "result.html", {
                "crop": crop_data['name'],
                "crop_details": crop_data
            })

        except ValueError:
            return render(request, "recommend.html", {
                "error": "Please enter valid numeric values!"
            })

        except Exception as e:
            return render(request, "recommend.html", {
                "error": f"Unexpected error: {str(e)}"
            })

    return render(request, "recommend.html")
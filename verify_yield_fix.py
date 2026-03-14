import joblib
import os
import numpy as np

# Mocking settings
BASE_DIR = r'c:\Users\acer\Desktop\CropYieldProject\crop_project'
model_path = os.path.join(BASE_DIR, "yield_model.pkl")

try:
    model = joblib.load(model_path)
    # Test with 3 features: Rainfall, Temperature, Area
    input_data = np.array([[120.5, 28.5, 5.2]])
    prediction = model.predict(input_data)
    print(f"SUCCESS: Predicted Yield = {prediction[0]:.2f} Tons")
except Exception as e:
    print(f"FAILURE: {e}")

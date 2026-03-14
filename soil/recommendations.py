# crop_project/soil/recommendations.py

SOIL_DATA = {
    "Sandy": {
        "characteristics": [
            "Excellent drainage, dries out quickly",
            "Warms up fast in spring",
            "Low in essential nutrients (needs frequent fertilizing)"
        ],
        "crops": ["Carrot", "Potato", "Groundnut", "Radish", "Cucumber"],
        "tips": "Add organic matter like compost to improve water retention. Irrigate lightly but frequently."
    },
    "Clay": {
        "characteristics": [
            "High water retention (heavy and sticky when wet)",
            "Nutrient-rich, holds minerals well",
            "Slow to warm up in spring, poor drainage"
        ],
        "crops": ["Rice", "Broccoli", "Cabbage", "Peas", "Aster"],
        "tips": "Avoid working the soil when it's wet to prevent compaction. Add gypsum to improve structure."
    },
    "Loamy": {
        "characteristics": [
            "Ideal agricultural soil (perfect mix of sand, silt, and clay)",
            "Great moisture retention and drainage",
            "High fertility and organic matter"
        ],
        "crops": ["Wheat", "Sugarcane", "Cotton", "Tomato", "Most vegetables"],
        "tips": "Maintain fertility by rotating crops and adding light compost annually."
    },
    "Silty": {
        "characteristics": [
            "Smooth, slippery texture",
            "Moisture retentive and typically very fertile",
            "Prone to compaction and crusting"
        ],
        "crops": ["Lettuce", "Onion", "Turmeric", "Ginger", "Cabbage"],
        "tips": "Avoid walking on wet silty soil. Incorporate organic matter to prevent crusting on the surface."
    },
    "Peaty": {
        "characteristics": [
            "High in organic matter and moisture",
            "Often acidic nature",
            "Dark color, warms up slowly"
        ],
        "crops": ["Root crops", "Legumes", "Spinach", "Brassicas"],
        "tips": "You may need to add lime to reduce acidity. Excellent for crops once drained properly."
    },
    "Chalky": {
        "characteristics": [
            "Highly alkaline (high pH)",
            "Often stony, drains rapidly",
            "Can lead to stunted growth due to iron/manganese lockup"
        ],
        "crops": ["Spinach", "Sweet Corn", "Beetroot", "Cabbage", "Lilac"],
        "tips": "Use acidifying fertilizers. Regularly add bulky organic matter to improve structure and moisture retention."
    }
}

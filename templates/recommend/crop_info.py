# Alphabetical mapping for the 22 crops in the standard recommendation dataset
CROP_MAPPING = {
    0: "apple",
    1: "banana",
    2: "blackgram",
    3: "chickpea",
    4: "coconut",
    5: "coffee",
    6: "cotton",
    7: "grapes",
    8: "jute",
    9: "kidneybeans",
    10: "lentil",
    11: "maize",
    12: "mango",
    13: "mothbeans",
    14: "mungbean",
    15: "muskmelon",
    16: "orange",
    17: "papaya",
    18: "pigeonpeas",
    19: "pomegranate",
    20: "rice",
    21: "watermelon"
}

# Metadata for each crop
CROP_DETAILS = {
    "apple": {
        "icon": "fa-solid fa-apple-whole",
        "description": "Apples grow best in temperate climates with cold winters.",
        "tips": "Prune trees annually and ensure well-drained soil rich in organic matter."
    },
    "banana": {
        "icon": "fa-solid fa-lemon", # FA doesn't have a good banana icon in free, lemon/leaf fallback
        "description": "Bananas are high-yield tropical fruits that love humidity and heat.",
        "tips": "Provide plenty of water and heavy mulching. Protect from strong winds."
    },
    "blackgram": {
        "icon": "fa-solid fa-seedling",
        "description": "A nutritious pulse crop that restores nitrogen to the soil.",
        "tips": "Requires moderate rainfall. Avoid waterlogging at all stages."
    },
    "chickpea": {
        "icon": "fa-solid fa-bowl-food",
        "description": "A drought-tolerant legume that grows well in cool, dry conditions.",
        "tips": "Plant in well-drained soil. Avoid excess nitrogen fertilizer as it's a legume."
    },
    "coconut": {
        "icon": "fa-solid fa-tree",
        "description": "Coconuts thrive in coastal tropical regions with loamy or sandy soil.",
        "tips": "Keep the basin moist and apply organic manure regularly."
    },
    "coffee": {
        "icon": "fa-solid fa-mug-hot",
        "description": "Coffee requires high altitudes, cool temperatures, and consistent rainfall.",
        "tips": "Provide shade trees and maintain slightly acidic soil pH."
    },
    "cotton": {
        "icon": "fa-solid fa-cloud",
        "description": "A cash crop that needs warm temperatures and moderate rainfall.",
        "tips": "Ensure full sunlight and keep the field weed-free during early growth."
    },
    "grapes": {
        "icon": "fa-solid fa-grapes",
        "description": "Grapes grow on vines and require warm, dry summers for sweet fruit.",
        "tips": "Implement a trellis system and prune heavily in winter."
    },
    "jute": {
        "icon": "fa-solid fa-lines-leaning",
        "description": "A fiber crop that grows in hot, humid climates with heavy rainfall.",
        "tips": "Best grown in alluvial soil. Requires significant water for retting."
    },
    "kidneybeans": {
        "icon": "fa-solid fa-beans",
        "description": "A protein-rich pulse that likes cool to moderate temperatures.",
        "tips": "Maintain consistent moisture but avoid soaking the leaves to prevent rot."
    },
    "lentil": {
        "icon": "fa-solid fa-droplet",
        "description": "A hardy pulse crop that can survive in relatively low moisture.",
        "tips": "Sow in early winter. Harvest when pods turn golden brown."
    },
    "maize": {
        "icon": "fa-solid fa-wheat-awn",
        "description": "Maize (Corn) is a versatile cereal that needs warm weather and nitrogen.",
        "tips": "Plant in blocks for better pollination. Control weeds for the first 4 weeks."
    },
    "mango": {
        "icon": "fa-solid fa-fruit-citrus",
        "description": "The king of fruits, mangoes thrive in tropical and subtropical heat.",
        "tips": "Avoid irrigation during the flowering period to improve fruit set."
    },
    "mothbeans": {
        "icon": "fa-solid fa-seedling",
        "description": "An extremely drought-resistant pulse crop for arid regions.",
        "tips": "Grows well even in sandy soil with minimal water."
    },
    "mungbean": {
        "icon": "fa-solid fa-seedling",
        "description": "A fast-growing pulse crop that serves as excellent green manure.",
        "tips": "Short duration crop. Suitable for intercropping with longer-season crops."
    },
    "muskmelon": {
        "icon": "fa-solid fa-circle",
        "description": "Melons love heat and well-drained sandy loams.",
        "tips": "Use mulching to keep fruits off the ground and maintain moisture."
    },
    "orange": {
        "icon": "fa-solid fa-sun",
        "description": "Citrus fruits like oranges need plenty of sunlight and well-aerated soil.",
        "tips": "Prune dead wood and provide consistent water during fruit development."
    },
    "papaya": {
        "icon": "fa-solid fa-circle-dot",
        "description": "A fast-growing tropical fruit that needs excellent drainage.",
        "tips": "Avoid waterlogging as it causes root rot. Apply organic potassium."
    },
    "pigeonpeas": {
        "icon": "fa-solid fa-seedling",
        "description": "A deep-rooted legume that improves soil structure and fertility.",
        "tips": "Requires very little water. Good for field bunding."
    },
    "pomegranate": {
        "icon": "fa-solid fa-circle-nodes",
        "description": "A fruit that thrives in dry, semi-arid climates.",
        "tips": "Perform thinning to get larger fruits. Monitor for fruit borer pests."
    },
    "rice": {
        "icon": "fa-solid fa-water",
        "description": "Rice is a staple crop that grows best in standing water or flooded fields.",
        "tips": "Maintain a consistent water level and use nitrogen-rich fertilizers."
    },
    "watermelon": {
        "icon": "fa-solid fa-van-shuttle", # Fallback or circle
        "description": "Watermelons grow on the ground and need hot days and sandy soil.",
        "tips": "Give plenty of space for vines to spread. Stop watering a week before harvest for higher sugar."
    }
}

def get_crop_data(class_idx):
    name = CROP_MAPPING.get(class_idx, "Unknown")
    details = CROP_DETAILS.get(name, {
        "icon": "fa-solid fa-question",
        "description": "No additional details available.",
        "tips": "Consult a local agricultural expert for guidance."
    })
    return {
        "name": name.capitalize(),
        "icon": details["icon"],
        "description": details["description"],
        "tips": details["tips"]
    }

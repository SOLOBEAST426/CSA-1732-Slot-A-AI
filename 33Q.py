diets = {
    "diabetes": "Choose balanced meals, high-fiber foods, and limit added sugar.",
    "high blood pressure": "Choose low-sodium foods, fruits, and vegetables.",
    "obesity": "Choose balanced portions, vegetables, fruits, and whole grains.",
    "anemia": "Include iron-rich foods such as beans, lentils, and leafy greens."
}

disease = input("Enter disease name: ").lower()

if disease in diets:
    print("Suggested diet:", diets[disease])
else:
    print("No diet information available for this disease.")
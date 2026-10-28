from sklearn.tree import DecisionTreeClassifier

# Training data: [Weather, Temperature]
# Weather: 0 = Sunny, 1 = Rainy, 2 = Cloudy
# Temperature: 0 = Cool, 1 = Hot

X = [
    [0, 1],
    [0, 0],
    [1, 1],
    [1, 0],
    [2, 1],
    [2, 0]
]

# 0 = Do not play, 1 = Play
y = [0, 1, 0, 0, 1, 1]

# Create and train the Decision Tree
model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

# Predict for a new situation
weather = int(input("Enter weather (0-Sunny, 1-Rainy, 2-Cloudy): "))
temperature = int(input("Enter temperature (0-Cool, 1-Hot): "))

prediction = model.predict([[weather, temperature]])

if prediction[0] == 1:
    print("Decision: Play cricket")
else:
    print("Decision: Do not play cricket")

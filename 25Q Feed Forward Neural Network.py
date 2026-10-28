import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0], [1], [1], [0]])

np.random.seed(42)

weights1 = np.random.rand(2, 4)
weights2 = np.random.rand(4, 1)

for epoch in range(10000):
    hidden = sigmoid(np.dot(X, weights1))
    output = sigmoid(np.dot(hidden, weights2))

    error = y - output

    d_output = error * sigmoid_derivative(output)
    d_hidden = np.dot(d_output, weights2.T) * sigmoid_derivative(hidden)

    weights2 += np.dot(hidden.T, d_output) * 0.5
    weights1 += np.dot(X.T, d_hidden) * 0.5

print("Feedforward Neural Network Output:")
for i in range(len(X)):
    hidden = sigmoid(np.dot(X[i], weights1))
    output = sigmoid(np.dot(hidden, weights2))
    print(X[i], "=", round(output[0], 3))

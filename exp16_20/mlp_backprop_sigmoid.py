import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def initialize_mlp(n_inputs, hidden_size=4):
    w1 = np.random.rand(n_inputs, hidden_size) - 0.5
    w2 = np.random.rand(hidden_size, hidden_size) - 0.5
    w3 = np.random.rand(hidden_size, 1) - 0.5
    b1 = np.random.rand(1, hidden_size) - 0.5
    b2 = np.random.rand(1, hidden_size) - 0.5
    b3 = np.random.rand(1, 1) - 0.5
    return w1, w2, w3, b1, b2, b3

def forward_pass(x, w1, w2, w3, b1, b2, b3):
    h1 = sigmoid(np.dot(x, w1) + b1)
    h2 = sigmoid(np.dot(h1, w2) + b2)
    out = sigmoid(np.dot(h2, w3) + b3)
    return h1, h2, out

def backward_pass(x, y, h1, h2, out, w1, w2, w3, b1, b2, b3, learning_rate=0.1):
    # Output layer error
    out_error = y - out
    out_delta = out_error * sigmoid_derivative(out)
    # Second hidden layer
    h2_error = np.dot(out_delta, w3.T)
    h2_delta = h2_error * sigmoid_derivative(h2)
    # First hidden layer
    h1_error = np.dot(h2_delta, w2.T)
    h1_delta = h1_error * sigmoid_derivative(h1)
    # Update weights and biases
    w3 += learning_rate * np.dot(h2.T, out_delta)
    b3 += learning_rate * np.sum(out_delta, axis=0, keepdims=True)
    w2 += learning_rate * np.dot(h1.T, h2_delta)
    b2 += learning_rate * np.sum(h2_delta, axis=0, keepdims=True)
    w1 += learning_rate * np.dot(x.T, h1_delta)
    b1 += learning_rate * np.sum(h1_delta, axis=0, keepdims=True)
    return w1, w2, w3, b1, b2, b3

def main():
    n_inputs = int(input("Enter number of binary inputs (N): "))
    epochs = 1000
    w1, w2, w3, b1, b2, b3 = initialize_mlp(n_inputs)
    
    # Simple dataset (e.g., XOR-like for n=2)
    X = np.random.randint(0, 2, (4, n_inputs))
    y = np.array([[1], [0], [0], [1]])  # Example targets
    if n_inputs > 2:
        y = np.random.randint(0, 2, (4, 1))  # Random targets for larger inputs
    
    for epoch in range(epochs):
        for i in range(len(X)):
            x = X[i:i+1]
            h1, h2, out = forward_pass(x, w1, w2, w3, b1, b2, b3)
            w1, w2, w3, b1, b2, b3 = backward_pass(x, y[i:i+1], h1, h2, out, w1, w2, w3, b1, b2, b3)
    
    print(f"Final Weights (W1):\n{np.round(w1, 2)}")
    print(f"Final Weights (W2):\n{np.round(w2, 2)}")
    print(f"Final Weights (W3):\n{np.round(w3, 2)}")
    print(f"Final Biases (b1):\n{np.round(b1, 2)}")
    print(f"Final Biases (b2):\n{np.round(b2, 2)}")
    print(f"Final Biases (b3):\n{np.round(b3, 2)}")
    print(f"Number of Steps: {epochs}")

if __name__ == "__main__":
    main()

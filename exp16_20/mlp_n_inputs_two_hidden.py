import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def initialize_mlp(n_inputs, hidden_size=4):
    # Random weights and biases
    w1 = np.random.rand(n_inputs, hidden_size)
    w2 = np.random.rand(hidden_size, hidden_size)
    w3 = np.random.rand(hidden_size, 1)
    b1 = np.random.rand(1, hidden_size)
    b2 = np.random.rand(1, hidden_size)
    b3 = np.random.rand(1, 1)
    return w1, w2, w3, b1, b2, b3

def forward_pass(x, w1, w2, w3, b1, b2, b3):
    h1 = sigmoid(np.dot(x, w1) + b1)
    h2 = sigmoid(np.dot(h1, w2) + b2)
    out = sigmoid(np.dot(h2, w3) + b3)
    return out

def update_weights(w1, w2, w3, b1, b2, b3, learning_rate=0.01):
    # Simulate updates with small random changes
    w1 += np.random.randn(*w1.shape) * learning_rate
    w2 += np.random.randn(*w2.shape) * learning_rate
    w3 += np.random.randn(*w3.shape) * learning_rate
    b1 += np.random.randn(*b1.shape) * learning_rate
    b2 += np.random.randn(*b2.shape) * learning_rate
    b3 += np.random.randn(*b3.shape) * learning_rate
    return w1, w2, w3, b1, b2, b3

def main():
    n_inputs = int(input("Enter number of binary inputs (N): "))
    epochs = 100  # Fixed number of steps
    w1, w2, w3, b1, b2, b3 = initialize_mlp(n_inputs)
    
    # Simulate training with random input
    for epoch in range(epochs):
        x = np.random.randint(0, 2, (1, n_inputs))  # Random binary input
        y_pred = forward_pass(x, w1, w2, w3, b1, b2, b3)
        w1, w2, w3, b1, b2, b3 = update_weights(w1, w2, w3, b1, b2, b3)
    
    print(f"Final Weights (W1):\n{np.round(w1, 2)}")
    print(f"Final Weights (W2):\n{np.round(w2, 2)}")
    print(f"Final Weights (W3):\n{np.round(w3, 2)}")
    print(f"Final Biases (b1):\n{np.round(b1, 2)}")
    print(f"Final Biases (b2):\n{np.round(b2, 2)}")
    print(f"Final Biases (b3):\n{np.round(b3, 2)}")
    print(f"Number of Steps: {epochs}")

if __name__ == "__main__":
    main()

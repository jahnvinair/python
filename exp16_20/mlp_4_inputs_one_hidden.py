import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def initialize_mlp():
    # Fixed sizes: 4 inputs, 4 hidden neurons, 2 outputs
    w1 = np.random.rand(4, 4)
    w2 = np.random.rank(4, 2)
    b1 = np.random.rand(1, 4)
    b2 = np.random.rand(1, 2)
    return w1, w2, b1, b2

def forward_pass(x, w1, w2, b1, b2):
    h1 = sigmoid(np.dot(x, w1) + b1)
    out = sigmoid(np.dot(h1, w2) + b2)
    return out

def update_weights(w1, w2, b1, b2, learning_rate=0.01):
    w1 += np.random.randn(*w1.shape) * learning_rate
    w2 += np.random.randn(*w2.shape) * learning_rate
    b1 += np.random.randn(*b1.shape) * learning_rate
    b2 += np.random.randn(*b2.shape) * learning_rate
    return w1, w2, b1, b2

def main():
    epochs = 100
    w1, w2, b1, b2 = initialize_mlp()
    
    for epoch in range(epochs):
        x = np.random.randint(0, 2, (1, 4))  # Random binary input
        y_pred = forward_pass(x, w1, w2, b1, b2)
        w1, w2, b1, b2 = update_weights(w1, w2, b1, b2)
    
    print(f"Final Weights (W1):\n{np.round(w1, 2)}")
    print(f"Final Weights (W2):\n{np.round(w2, 2)}")
    print(f"Final Biases (b1):\n{np.round(b1, 2)}")
    print(f"Final Biases (b2):\n{np.round(b2, 2)}")
    print(f"Number of Steps: {epochs}")

if __name__ == "__main__":
    main()

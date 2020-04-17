import numpy as np

def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1/(1+np.exp(-x))

# Network size
N_input = 4
N_hidden = 3
N_output = 2

np.random.seed(42)
# Make some fake data
X = np.random.randn(4)

weights_input_to_hidden = np.random.normal(0, scale=0.1, size=(N_input, N_hidden))
weights_hidden_to_output = np.random.normal(0, scale=0.1, size=(N_hidden, N_output))

# Forward pass through the network
# Transpose of X to be 1 by 4 
# Perform matrix multiplication of X.T (1x4) by weights_input_to_hidden (4x3)
hidden_layer_in = np.matmul(X.T,  weights_input_to_hidden)
hidden_layer_out = sigmoid(hidden_layer_in)

print('Hidden-layer Output:')
print(hidden_layer_out)

# Transpose of hidden_layer_out to be 1 by 3
# Perform matrix multiplication of hidden_layer_out (1x3) by weights_hidden_to_output (3x2)
output_layer_in = np.matmul(hidden_layer_out.T, weights_hidden_to_output)
output_layer_out = sigmoid(output_layer_in)

print('Output-layer Output:')
print(output_layer_out)
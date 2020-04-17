import numpy as np

def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1/(1+np.exp(-x))

def sigmoid_prime(x):
    """
    # Derivative of the sigmoid function
    """
    return sigmoid(x) * (1 - sigmoid(x))

learning_rate = 0.5
# Input values X1, X2, ...Xn
x = np.array([1, 2, 3, 4])
# Label
y = np.array(0.5)

# Initial weights
w = np.array([0.5, -0.5, 0.3, 0.1])

### Calculate one gradient descent step for each weight

# Linear combination of inputs and weights
h = np.dot(w,x)

# Pass output through the activation function
nn_output = sigmoid(h)

# Error of neural network
error = y - nn_output

# Calculate the error term 
error_term = error * sigmoid_prime(h)

# Calculating the error change
delta_w = learning_rate * error_term * x


print('Neural Network output:')
print(nn_output)
print('Amount of Error:')
print(error)
print('Change in Weights:')
print(delta_w)
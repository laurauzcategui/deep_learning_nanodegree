import numpy as np
from l5_data_prep import features, targets, features_test, targets_test

np.random.seed(21)

def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))


# Hyperparameters
n_hidden = 2  # number of hidden units
epochs = 5000
learnrate = 0.005

n_records, n_features = features.shape
last_loss = None
# Initialize weights
weights_input_hidden = np.random.normal(scale=1 / n_features ** .5,
                                        size=(n_features, n_hidden))
weights_hidden_output = np.random.normal(scale=1 / n_features ** .5,
                                         size=n_hidden)

for e in range(epochs):
    del_w_input_hidden = np.zeros(weights_input_hidden.shape)
    del_w_hidden_output = np.zeros(weights_hidden_output.shape)
    for x, y in zip(features.values, targets):
        ## Forward pass ##
        # Calculate the hidden input [ features * weights ]
        hidden_input = np.dot(x, weights_input_hidden)
        # Apply the activation function
        hidden_output = sigmoid(hidden_input)
        # Calculate the output [ hidden_output * weights in hidden output ] f(w*a)
        output = sigmoid(np.dot(hidden_output,weights_hidden_output))

        ## Backward pass ##
        # Calculate the network's prediction error
        error = y - output 

        # Calculate error term for the output unit
        # Error term is : error * f'(w*a) (derivative of the output function)
        output_error_term = error * output * (1 - output)

        ## propagate errors to hidden layer
        # Now we need to propagate back from the output to the hidden layer

        # Calculate the hidden layer's contribution to the error
        '''
            Here we are scaling the error term from output unit by weights on the hidden unit
        '''
        hidden_error = np.dot(output_error_term, weights_hidden_output)
        
        # Calculate the error term for the hidden layer
        # Error term is: w * error term output * f'(h)
        hidden_error_term = hidden_error * hidden_output * (1-hidden_output)
        
        # TODO: Update the change in weights
        del_w_hidden_output += output_error_term * hidden_output
        del_w_input_hidden += hidden_error_term * x[:, None]

    # TODO: Update weights  (don't forget to division by n_records or number of samples)
    weights_input_hidden += learnrate * del_w_input_hidden / n_records
    weights_hidden_output += learnrate * del_w_hidden_output / n_records

    # Printing out the mean square error on the training set
    if e % (epochs / 10) == 0:
        hidden_output = sigmoid(np.dot(x, weights_input_hidden))
        out = sigmoid(np.dot(hidden_output,
                             weights_hidden_output))
        loss = np.mean((out - targets) ** 2)

        if last_loss and last_loss < loss:
            print("Train loss: ", loss, "  WARNING - Loss Increasing")
        else:
            print("Train loss: ", loss)
        last_loss = loss

# Calculate accuracy on test data
hidden = sigmoid(np.dot(features_test, weights_input_hidden))
out = sigmoid(np.dot(hidden, weights_hidden_output))
predictions = out > 0.5
accuracy = np.mean(predictions == targets_test)
print("Prediction accuracy: {:.3f}".format(accuracy))

import numpy as np
from l5_data_prep import features, targets, features_test, targets_test


def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))

# Use to same seed to make debugging easier
np.random.seed(42)

n_records, n_features = features.shape
last_loss = None

# Initialize weights
weights = np.random.normal(scale=1 / n_features**.5, size=n_features)

# Neural Network hyperparameters
epochs = 1000
learnrate = 0.25

for e in range(epochs):
    del_w = np.zeros(weights.shape)
    for x, y in zip(features.values, targets):
        # Loop through all records, x is the input, y is the target

        # Making a forward pass along with the activation function
        output = sigmoid(np.dot(x,y))

        # Calculating MSE
        error = (y - output)

        # Calculating Error term as error * f(h)*(1-f(h))
        # Sigmoid prime: f(h)*(1-f(h) 
        error_term = error * (output * (1-output))  

        # Calculating delta Weights 
        del_w += error_term * x

    # Update weights using the learning rate and the average change in weights
    weights += (learnrate * del_w) / len(x)

    # Printing out the mean square error on the training set
    if e % (epochs / 10) == 0:
        out = sigmoid(np.dot(features, weights))
        loss = np.mean((out - targets) ** 2)
        if last_loss and last_loss < loss:
            print("Train loss: ", loss, "  WARNING - Loss Increasing")
        else:
            print("Train loss: ", loss)
        last_loss = loss


# Calculate accuracy on test data
tes_out = sigmoid(np.dot(features_test, weights))
predictions = tes_out > 0.5
accuracy = np.mean(predictions == targets_test)
assert round(accuracy,1) == 0.7
print("Prediction accuracy: {:.3f}".format(accuracy))
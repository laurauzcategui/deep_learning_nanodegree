import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



'''
 The following helpers: plot_points and display has been taken as a reference from: 
 https://github.com/udacity/deep-learning-v2-pytorch/blob/master/intro-neural-networks/gradient-descent/GradientDescent.ipynb
'''

def plot_points(X, y):
    '''
    plot_points will generate an scatter plot where students has been rejected or accepted

    parameters: 
    -----------
    X: int, representative of the coordinates of the points to plot 
    Y: int, label that indicates if a student has been accepted (1) and rejected(0)

    '''
    admitted = X[np.argwhere(y==1)]
    rejected = X[np.argwhere(y==0)]
    plt.scatter([coords[0][0] for coords in rejected], [coords[0][1] for coords in rejected], s = 25, color = 'green', edgecolor = 'k')
    plt.scatter([coords[0][0] for coords in admitted], [coords[0][1] for coords in admitted], s = 25, color = 'red',   edgecolor = 'k')

def display(m, b, color='gray', linestyle='--'):
    '''
    display will generate the plot scales for the X and y axis and will draw the line

    parameters: 
    ----------
    m: float, slope of the line 
    b: float, intercept of the line 
    '''
    plt.xlim(-0.05,1.05) # set the x limit 
    plt.ylim(-0.05,1.05) # set the y limit 
    x = np.arange(-10, 10, 0.1)
    plt.plot(x, m*x+b, color=color, linestyle=linestyle)



def stepFunction(t):
    '''
    stepFunction will fire (1) if the linear equation result is greater than 0, otherwise returns 0 

    parameters
    ----------
    t: int, predicted value

    returns: int with the neuron being fired or not
    '''
    if t >= 0:
        return 1
    return 0

def prediction(X, W, b):
    '''
    prediction will execute the matrix multiplication Wx + b 

    parameters
    ----------
    X: numpy 1D array, input elements to perform the equations. Also called features
    W: numpy 1D array, weights for each element in X. 
    b: int, bias unit 

    returns: int representing the prediction after passing through the Step function
    '''
    linearCombination = np.matmul(X,W)+b
    return stepFunction(linearCombination[0])

# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate = 0.01):
    '''
    will apply the perceptron step based on the prediction

    parameters
    ----------
    X: numpy 1D array, input elements to perform the equations. Also called features
    y: numpy 1D array, labels to match the expected output from the prediction
    W: numpy 1D array, weights for each element in X. 
    b: int, bias unit     
    learn_rate: float, learning rate to be used at each perceptron step. optional. Default: 0.01
    '''

    for Xi, Yi in zip(X, y):
        y_hat = prediction(Xi, W, b)
        if y_hat == Yi:
            pass
        elif y_hat == 0:
            W[0] -=  learn_rate * Xi[0]
            W[1] -=  learn_rate * Xi[1]
            b = b + learn_rate
        elif y_hat == 1:   
            W[0] -=  learn_rate * Xi[0]
            W[1] -=  learn_rate * Xi[1]
            b = b - learn_rate
    return W, b
    
def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 50):
    '''
    trainPerceptronAlgorithm runs  the perceptron algorithm repeatedly on the dataset
    returns boundary lines obtained in the iterations

    parameters: 
    -----------
    X: 1D numpy array with tuples: (x1, x2) representing the features 
    y: 1D numpy array representing the labels 
    learn_rate: float, optional. learning rate at which the perceptron step will be applied 
    num_epochs: int, optional. Number of epochs to train the perceptron algorithm

    returns:
    boundary_lines: array with the tuple of coordinates to plot
    '''
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.random.rand(2,1)
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
        if i < num_epochs-1:
            display(-W[0]/W[1], -b/W[1])
    return boundary_lines

def build_arrays(filename):
    '''
    build_arrays will read a csv file with the inputs X and labels y and return a tuple of numpy arrays

    parameters:
    -----------
    filename: string, file containing the dataset to evaluate on

    returns: 
    tuple, numpy arrays, representing inputs and labels 
    '''
    data_frame = pd.read_csv(filename, names=["x1", "x2", "y"])
    X = data_frame[["x1", "x2"]].to_numpy()
    y = data_frame[["y"]].to_numpy()
    return X,y 

if __name__ == "__main__":

    # Setting the random seed, feel free to change it and see different solutions.
    np.random.seed(42)

    X,y = build_arrays("data.csv")

    num_epochs = 50
    lines = trainPerceptronAlgorithm(X, y)

    plt.title("Solution boundary")
    display(lines[num_epochs-1][0][0],lines[num_epochs-1][1][0], 'black','-')

    # plot the points 
    plot_points(X,y)
    plt.show()







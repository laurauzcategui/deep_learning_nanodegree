# Use the numpy library
import numpy as np


def prepare_inputs(inputs):
    # TODO: create a 2-dimensional ndarray from the given 1-dimensional list;
    #       assign it to input_array
    input_array = np.array([inputs])
    
    # TODO: find the minimum value in input_array and subtract that
    #       value from all the elements of input_array. Store the
    #       result in inputs_minus_min
    inputs_minus_min = input_array - min(inputs)

    # TODO: find the maximum value in inputs_minus_min and divide
    #       all of the values in inputs_minus_min by the maximum value.
    #       Store the results in inputs_div_max.
    inputs_div_max =  inputs_minus_min / np.max(inputs_minus_min)

    # return the three arrays we've created
    return input_array, inputs_minus_min, inputs_div_max
    

def multiply_inputs(m1, m2):
    # TODO: Check the shapes of the matrices m1 and m2. 
    #       m1 and m2 will be ndarray objects.
    #
    #       Return False if the shapes cannot be used for matrix
    #       multiplication. You may not use a transpose
    if not (m1.shape[1] == m2.shape[0]) and not(m1.shape[0] == m2.shape[1]):
        return False

    # TODO: If you have not returned False, then calculate the matrix product
    #       of m1 and m2 and return it. Do not use a transpose,
    #       but you swap their order if necessary
    if m1.shape[1] == m2.shape[0]:
        return np.matmul(m1,m2)
    return np.matmul(m2,m1)
    

def find_mean(values):
    # TODO: Return the average of the values in the given Python list
    return np.mean(values)


input_array, inputs_minus_min, inputs_div_max = prepare_inputs([-1,2,7])
print("Input as Array: {}".format(input_array))
print("Input minus min: {}".format(inputs_minus_min))
print("Input  Array: {}".format(inputs_div_max))

input_matrix = np.array([[1,2,3],[4,5,6]])
result = multiply_inputs(input_matrix, np.array([[1],[2],[3],[4]]))
assert result is False
print("Multiply 1:\n{}\n".format(result))

result = multiply_inputs(input_matrix, np.array([[1],[2],[3]]))
assert np.all(result == np.array([[14],[32]])) == True
print("Multiply 2:\n{}\n".format(result))

result = multiply_inputs(input_matrix,  np.array([[1,2]]))
assert np.all(result == np.array([9,12,15])) == True
print("Multiply 3:\n{}\n".format(result))

res = find_mean([1,3,4])
assert res == 2.6666666666666665
print("Mean == {}".format(res))

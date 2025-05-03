
# add some numpy code here to practice numpy
import numpy as np
import matplotlib.pyplot as plt


# important installation: pip install numpy matplotlib
# if doesn't work double check: pip show matplotlib
# Then try: python -m pip install matplotlib



# Create a list

my_list = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

my_list = np.array(my_list) # convert the list to a numpy array
print("List converted to numpy array:\n", my_list) # print the numpy array

print(f"print the shape of the numpy array: {my_list.shape}") # print the shape of the numpy array
print(f"print the number of dimensions: {my_list.ndim}") # print the number of dimensions of the numpy array
print(f"print the size of the numpy array: {my_list.size}") # print the size of the numpy array
print(my_list[1,2]) # print the element at index [1,2] of the numpy array --> 23 


# Create a 1D array of integers from 0 to 9
array_1d = np.arange(10)
print("1D Array:", array_1d)
# Create a 2D array (matrix) of shape (3, 3) with random integers
array_2d = np.random.randint(1, 10, size=(3, 3)) # create a 3x3 matrix with random integers between 1 and 10
print("2D Array:\n", array_2d)



data_type = np.array([1,2,3,4,5])
print(type(data_type)) # <class 'numpy.ndarray'>
print(data_type.dtype) # int64
change_index_one_to_ten = data_type[1] = 10 # change the second element to 10
print(data_type) # [ 1 10 3 4 5]

# start at index 1 and end at length 4
slice_array = data_type[1:4] # slice the array from index 1 to 4
print(slice_array) # [10  3  4]

# Array addition
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 + array2
print(result)  # [5 7 9]

# Scalar multiplication
array = np.array([1, 2, 3])
result = array * 2 # each element of an array is multiplied by 2
print(result)  # [2 4 6]


# Element-wise multiplication (Hadamard product)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 * array2
print(result)  # [4 10 18]

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.dot(matrix1, matrix2)
print(result) 
# [[19 22]
#  [43 50]]


X=np.array([[1,0],[0,1]])

Y=np.array([[2,2],[2,2]]) 

Z=np.dot(X,Y) 
print(Z) # [[2 2]
#  [2 2]]


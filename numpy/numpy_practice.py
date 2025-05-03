
# add some numpy code here to practice numpy
import numpy as np
import matplotlib.pyplot as plt
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


# create a simple plot with numpy
x = np.arange(0, 10, 0.1) # create an array from 0 to 10 with a step of 0.1
y = np.sin(x) # create an array of sine values for each element in x
plt.plot(x, y) # plot the sine values against x
print("Plotting x and y diagram...")
plt.xlabel('x') # label the x-axis
plt.ylabel('y') # label the y-axis
plt.title('x and y plot') # title of the plot
plt.grid() # add a grid to the plot
plt.show() # show the plot


import numpy as np # import numpy for numerical operations
import matplotlib.pyplot as plt # import matplotlib for plotting




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
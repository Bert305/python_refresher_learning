# The clause try attempts to execute a block of code and except executes another block of code if try fails.


# The finally clause executes a block of code regardless of which clause, try or except, was executed. 

# The finally clause is useful in cases where both of your try and except might fail.



nums = [0, 1, 2, 3]
 
try:
   print(sum(nums))
 
except:
   print('Cannot print the sum! Your variables are not numbers.')
   
   
   
   
   
   
nums2 = ['x', 'y', 'z']
 
try:
   print(sum(nums2))
 
except:
   print('Cannot print the sum! Your variables are not numbers.')
   
   
   
   

nums3 = ['x', 'y', 'z']
 
try:
   print(sum(nums3))
 
except:
   print('Cannot print the sum! Your variables are not numbers.')
 
finally:
   print('Hope you got the result you want!')
   
   
   
# using Try- except 
try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
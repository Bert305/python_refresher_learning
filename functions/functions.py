



# return sorted list of numbers

def sort_numbers(numbers):

    return sorted(numbers)


print(sort_numbers([5, 2, 4, 1, 3])) # [1, 2, 3, 4, 5]



# return the sum of the numbers in the list
def sum_numbers(numbers):

    sum = 0

    for i in range(len(numbers)):

        sum += numbers[i]

    return sum

print(sum_numbers([1, 2, 3, 4, 5])) # 15



def two_sum(numbers, target):

    for i in range(len(numbers)):
        # Need a nested for loop to iterate through the array to find the second number
        # that will add up to the target number
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                 # find the indexes and compare to the target value
                return [numbers[i], numbers[j]]
                # return the two numbers that add up to the target value
    
print(two_sum([1, 2, 3, 4, 5], 6)) # [1, 5]


# return the sum of two numbers
def sum(a,b):

    return a + b

print(sum(1, 2)) # 3


def print_function(A):
    for a in A:
        print(a + '1')
print_function(['a', 'b', 'c']) # a1 b1 c1


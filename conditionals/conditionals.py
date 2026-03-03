

# conditionals


# odd or even

def odd_or_even(num):

    odd = []
    even = []
    
    for i in range(len(num)):
        if num[i] % 2 == 0:
            even.append(num[i])
        else:
            odd.append(num[i])
    
    return [odd, even]

print(odd_or_even([1,2,3,4,5,6,7,8,9,10])) # [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]


def loop_backwards(num):
    list = []
    for i in range(len(num)-1, -1, -1):
        list.append(num[i])
    
    return list

print(loop_backwards([1,2,3,4,5])) # [5,4,3,2,1]


def string_odd_or_even(string):

    odd_or_even = []
    
    for i in range(len(string)):
        if string[i] % 2 == 0:
            odd_or_even.append("even")
        else:
            odd_or_even.append("odd")
    
    return odd_or_even
    

print(string_odd_or_even([1,2,3,4,5,6,7,8,9,10])) # ["odd", "even", "odd", "even", "odd", "even", "odd", "even", "odd", "even"]


def find_target(num, target):
    # iterate through all pairs of numbers in the list
    for i in range(len(num)):
        # for each number, check if there is another number in the list that adds up to the target
        for j in range(i+1, len(num)):
        # check if the sum of the pair equals the target
            if num[i] + num[j] == target:
                # if it does, return the indices of the two numbers
                return [i, j]

print(find_target([2,1,7,8,9,5], 6)) # [1,5] index 1 and 5 add up to 6



def highest_and_lowest(num):

    highest = num[0]
    lowest = num[0]
    
    for i in range(len(num)):
        if num[i] > highest:
            highest = num[i]
        else:
            lowest = num[i]
    
    return [highest, lowest]

print(highest_and_lowest([1,2,3,4,5])) # [5,1]


def lower_and_upper(string):

    char = []
    
    for i in range(len(string)):
        if i % 2 == 0:
            char.append(string[i].lower())
        else:
            char.append(string[i].upper())
    
    return char

print(lower_and_upper(["h","e","l","l","o","w","o","r","l","d"])) # ["h", "E", "l", "L", "o", "W", "o", "R", "l", "D"]




#  Stack memory --> manages memory for function calls and local variables within the scope:
# Stores local variables and function call information.

def stack_example():
    # These integers are local variables stored in the stack memory
    x = 10
    y = 20
    print("Inside stack_example -> x:", x, "y:", y)
    



# Heap memory --> manages memory for objects, lists, dictionaries, class instances, etc.:

# Stores objects (lists, dictionaries, class instances, etc.).

# Managed by Python’s garbage collector.

def heap_example():
    # Stores objects (lists, dictionaries, class instances, etc.) in heap memory
    a = [1, 2, 3]
    b = a  # b points to the same heap object as a 
    b.append(4) # Modifying b also affects a
    print("Inside heap_example -> a:", a, "b:", b)





# Run functions
stack_example()
heap_example()




#--------------------------------------


# Stack LIFO Example --> manages memory for function calls and local variables

Stack = []

def add_to_stack(value):
    Stack.append(value)  # Push to stack

def remove_from_stack():
    if Stack:
        return Stack.pop()  # Pop from stack
    return None
# Example usage
add_to_stack(1)
add_to_stack(2)
add_to_stack(3)

print("Stack after pushes:", Stack)

print("Popped from stack:", remove_from_stack())
print("Popped from stack:", remove_from_stack())
print("Popped from stack:", remove_from_stack())
print("Popped from stack (empty):", remove_from_stack())




# Heap LIFO Example using heapq --> manages memory for objects, lists, dictionaries, class instances, etc.


import heapq

# Create an empty heap
heap = []

# Push items onto the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

print("Heap after pushes:", heap)

# Pop items from the heap (min comes out first)
print("Popped:", heapq.heappop(heap))  # removes 1
print("Popped:", heapq.heappop(heap))  # removes 3
print("Popped:", heapq.heappop(heap))  # removes 5

print("Heap after pops:", heap)

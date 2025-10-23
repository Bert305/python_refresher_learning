



# Python Memory Model:


# STACK------------
# Stack → managed automatically for function calls and local variables.
# When a function ends, its stack frame is destroyed.



# HEAP------------
# Heap → where all Python objects (lists, dicts, class instances, etc.) are stored.
# The lifetime of these objects is not tied to a function call.
# Managed by Python’s garbage collection system.








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




# Heap Example --> manages memory for objects, lists, dictionaries, class instances, etc.

# Heap (no LIFO rule)

# The heap doesn’t follow LIFO. Objects can live longer than the function that created them.

def make_list():
    a = [10, 20, 30]   # list stored in heap
    return a           # reference returned

def main():
    lst1 = make_list()   # lst1 points to heap object
    lst2 = make_list()   # lst2 points to another heap object
    lst1.append(40)
    print("lst1:", lst1) # lst1: [10, 20, 30, 40]
    print("lst2:", lst2) # lst2: [10, 20, 30]

main()


# Heap flow

# [10, 20, 30] is created in the heap twice (for lst1 and lst2).

# Even after make_list() ends, the lists remain in memory because lst1 and lst2 still reference them.

# Garbage collector only frees them when nothing points to them anymore



# Garbage Collection example

# When the data from the heap is no longer referenced, Python’s garbage collector frees that memory.

def garbage_collection_example():
    a = [1, 2, 3]
    b = a
    del a  # Remove reference to the list
    # At this point, the list [1, 2, 3] is still referenced by b
    print("returning no reference of a", b)
    del b  # Remove last reference
    # Now the list is no longer referenced and can be garbage collected
    print("Both a and b references deleted, list is garbage collected freeing memory.")
garbage_collection_example()
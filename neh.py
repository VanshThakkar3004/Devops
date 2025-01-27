# List operations
def list_operations():
    # Create a list
    my_list = [10, 20, 30, 40, 50]
    print("Initial List:", my_list)
    
    # Append operation
    my_list.append(60)
    print("After append(60):", my_list)
    
    # Remove operation
    my_list.remove(30)
    print("After remove(30):", my_list)
    
    # Reverse operation
    my_list.reverse()
    print("After reverse:", my_list)
    
    # Slicing operation
    sliced_list = my_list[1:4]  # Slice from index 1 to 3 (not inclusive of 4)
    print("Sliced List [1:4]:", sliced_list)

# Tuple operations
def tuple_operations():
    # Create a tuple
    my_tuple = (10, 20, 30, 40, 50)
    print("\nInitial Tuple:", my_tuple)
    
    # Accessing tuple elements
    print("Accessing element at index 2:", my_tuple[2])  # Access the element at index 2 (30)
    
    # Slicing operation
    sliced_tuple = my_tuple[1:4]  # Slice from index 1 to 3 (not inclusive of 4)
    print("Sliced Tuple [1:4]:", sliced_tuple)

# Main program
def main():
    list_operations()
    tuple_operations()

# Run the program
main()

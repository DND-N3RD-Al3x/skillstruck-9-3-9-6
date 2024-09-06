# Define the dictionary
dictionary = {7: "first", 3: "second", 4: "third", 8: "fourth", 9: "fifth"}

# Get the list of integers from the user input
num_list = [int(n) for n in input("Enter a list of integers separated by spaces: ").split()]

# Check if each integer is a key in the dictionary
for x in num_list:
    if x in dictionary:
        print("Yes")
    else:
        print("No")

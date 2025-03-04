#nterchange first and last elements in a list
input_string = input("Enter elements of the list separated by space: ")
input_list = input_string.split()
if len(input_list) > 1:
input_list[0], input_list[-1] = input_list[-1], input_list[0]
print("List after swapping first and last elements:", input_list)
else:
print("List should contain at least two elements to swap.")

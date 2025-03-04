#wap in python to remove multiple elements in a list
original_list = input("Enter the elements of the list: ").split()
elements_to_remove = input("Enter the elements to remove: ").split()
for element in elements_to_remove:
while element in original_list: 
original_list.remove(element)
print("Modified List:", original_list)

#wap in python to remove duplicates from a list
original_list = input("Enter the elements of the list: ").split()
unique_list = []
for item in original_list:
if item not in unique_list:
unique_list.append(item)
print("List without duplicates:", unique_list)

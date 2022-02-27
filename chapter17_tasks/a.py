# Declare a list of string with number values
n_list = ['11', '50', '5', '1', '37', '19']
# Sort the list using lambda and sorted function
sorted_list = sorted(n_list, key=lambda x: int(x[0:]))
# Print the sorted list
print("The list of the sorted values are:")
for value in sorted_list:
    print(value, end=' ')
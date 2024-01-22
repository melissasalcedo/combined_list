# Creating new list 

# Function
def new_list(list1, list2):
    final_list=[]
    # odd numbers from the first list
    final_list.extend([num for num in list1 if num % 2 !=0])
    # even numbers from the second list
    final_list.extend([num for num in list2 if num % 2 ==0])

    return(final_list)
# Print the final list
list1 = [1, 4, 6, 7, 8, 9, 13]
list2 = [2, 4, 6, 7, 9, 10]

combined_list = new_list(list1, list2)
print("The new merged list is", combined_list)
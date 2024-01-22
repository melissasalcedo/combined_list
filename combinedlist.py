# 

# Function
def new_list(list1, list2):
    final_list=[]



    # Add odd numbers from the first list
    final_list.extend([num for num in list1 if num % 2 != 0])

    # Add even numbers from the second list
    final_list.extend([num for num in list2 if num % 2 == 0])

    return final_list

# Example usage:
list1 = [1, 2, 5, 7, 9]
list2 = [2, 5, 6, 9, 10]

final_list = new_list(list1, list2)
print(final_list)
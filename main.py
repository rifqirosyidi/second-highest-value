# Search second largest number in alist

# List of numbers
raw_list = [12, 12, 11, 11, 10, 3, 5, 7, 7]
set_list = set(raw_list)  # remove distinct value by converting to sets
list_1 = list(set_list)  # List ready to be executed

max_list = max(list_1[0], list_1[1])
second_max = min(list_1[0], list_1[1])

for i in range(2, len(list_1)):
    if list_1[i] > max_list:
        second_max = max_list
        max_list = list_1[i]
    else:
        if list_1[i] > second_max:
            second_max = list_1[i]

print("Second Highest Num is : ", second_max)

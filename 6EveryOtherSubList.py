def sub_list_with_stride(lst, start_idx, end_idx):
    sub_lst = lst[start_idx:end_idx+1]
    return sub_lst[::2]

# Test the sub_list_with_stride function
original_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = sub_list_with_stride(original_list, start_index, end_index)
print(result)

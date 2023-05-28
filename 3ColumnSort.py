def sort_list_of_dicts(list_of_dicts, key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[key])
    return sorted_list

# Test the sort_list_of_dicts function
fruits = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_by_fruit = sort_list_of_dicts(fruits, "fruit")
print(sorted_by_fruit)

sorted_by_color = sort_list_of_dicts(fruits, "color")
print(sorted_by_color)

def switch_dict(dictionary):
    return {value: key for key, value in dictionary.items()}

# Test the switch_dict function
original_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

result_dict = switch_dict(original_dict)
print(result_dict)

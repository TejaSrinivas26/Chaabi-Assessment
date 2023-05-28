def file_types(types_str, filenames):
    file_types_dict = {}
    types_list = types_str.split(';')
    
    for filename in filenames:
        file_extension = filename.split('.')[-1].lower()
        found_type = False
        
        for file_type in types_list:
            extension, file_type = file_type.split(',')
            if file_extension == extension:
                file_types_dict[filename] = file_type
                found_type = True
                break
        
        if not found_type:
            file_types_dict[filename] = "unknown"
    
    return file_types_dict

# Test the file_types function
types_str = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]
result = file_types(types_str, filenames)
print(result)

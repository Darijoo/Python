def string_formatting(strings):
    my_list = strings
    string_1 = my_list.pop()
    string_2 = my_list.pop()
    new_element = string_2 + " en " + string_1
    my_list.append(new_element)
    return my_list


string_list = ["een", "twee", "drie"]
print(string_formatting(string_list))

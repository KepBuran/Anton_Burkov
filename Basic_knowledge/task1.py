def filter_list(list):
    new_list = []
    for i in list:
        if type(i) is int:
            new_list.append(i)
    return new_list

################
print(filter_list([1,2,'a','b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1,2,'assf','1','123', 123]))
def number_of_pairs(target, array):
    for i in array:
        if i > target:
            array.remove(i)
    
    result = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i]+array[j] == target:
                result+=1

    return(result)


########
print(number_of_pairs(5, [1, 3, 6, 2, 2, 0, 4, 5]))
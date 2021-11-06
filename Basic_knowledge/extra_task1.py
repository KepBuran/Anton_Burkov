def nextBigger(number):
    number = [int(i) for i in str(number)]
    length = len(number)
    
    if length == 1:
        return -1

    for i in range(length-1, 0, -1):
        if number[i] > number[i-1]:
            break

    if i == 1 and number[i] <= number[i-1]:
        return -1
         
    temp = number[i-1]
    smallest_digit = i
    for j in range(i+1,length):
        if number[j] > temp and number[j] < number[smallest_digit]:
            smallest_digit = j
         
    number[smallest_digit],number[i-1] = number[i-1], number[smallest_digit]

    result = 0
    for j in range(i):
        result = result * 10 + number[j]
     
    number = sorted(number[i:])
    for j in range(length-i):
        result = result * 10 + number[j]
     
    return result

####
print(nextBigger(12))
print(nextBigger(513))
print(nextBigger(2017))
print(nextBigger(9))
print(nextBigger(111))
print(nextBigger(531))
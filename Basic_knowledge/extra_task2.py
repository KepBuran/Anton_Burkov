def number_to_IPv4(number):
    binary_list = [0] * 32
    for i in range(31, -1, -1):
        pow_2_i = pow(2,i)
        if number >= pow_2_i:
            number -= pow_2_i
            binary_list[i] = 1

    result_list = [0, 0, 0, 0]
    for i in range(len(binary_list)):
        if binary_list[i] == 1:
            result_list[3-i//8] = result_list[3-i//8]+pow(2, i-i//8*8)


    return(str(result_list[0])+'.'+str(result_list[1])+'.'+str(result_list[2])+'.'+str(result_list[3]))


#####
print(number_to_IPv4(2149583361))
print(number_to_IPv4(32))
print(number_to_IPv4(0))
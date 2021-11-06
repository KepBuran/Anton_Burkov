def Digital_root(n):
    i = 1
    result = 0 
    while(True): 
        result += n%10
        n = n//10 
        if n == 0:
            break
    if result <= 9:
        return(result)
    else:
        return(Digital_root(result))



#######
print(Digital_root(16))
print(Digital_root(942))
print(Digital_root(132189))
print(Digital_root(493193))
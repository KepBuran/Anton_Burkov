def sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if arr[j][1] == arr[j + 1][1]:
                if arr[j][0] > arr[j + 1][0]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


def modify_list(input_string):
    input_string = input_string.upper()
    new_list = input_string.split(';')

    for i in range(len(new_list)):
        new_list[i] = new_list[i].split(':')
    
    sort(new_list)
    
    output_string = ''
    for i in range(len(new_list)):
        output_string += '('+new_list[i][1]+', '+new_list[i][0]+')'

    return output_string 


#########
print(modify_list("Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))
print(modify_list("Fred:Corwill;Fred:Corwill;Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))
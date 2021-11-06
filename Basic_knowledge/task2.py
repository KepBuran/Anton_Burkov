def change_letter_case(letter):
    if ord(letter) <= 122 and ord(letter) >= 97:
        return chr(ord(letter)-32)
    elif ord(letter) <= 90 and ord(letter) >= 65:
        return chr(ord(letter)+32)
    else:
        return letter

def first_non_repeating_letter(string):
    non_repeating_letters = []
    repeating_letters = []
    for i in string:
        if i in repeating_letters or change_letter_case(i) in repeating_letters:
            continue
        elif i in non_repeating_letters:
            repeating_letters.append(non_repeating_letters.remove(i))
        elif change_letter_case(i) in non_repeating_letters:
            repeating_letters.append(non_repeating_letters.remove(change_letter_case(i)))
        else: 
            non_repeating_letters.append(i)
    if len(non_repeating_letters) == 0:
        return ''
    else:
        return(non_repeating_letters[0])
        


##############
print(first_non_repeating_letter('string'))
print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('sTress'))
print(first_non_repeating_letter('sTretss'))
print(first_non_repeating_letter('sTrREtss'))
print(first_non_repeating_letter('streetrs'))
print(first_non_repeating_letter('s@treetrs'))
print(first_non_repeating_letter('s@treet@rs'))

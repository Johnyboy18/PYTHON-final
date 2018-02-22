num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def Converter(number):

    roman = ''

    while number > 0:
        for i, r in num_map:
            while number >= i:
                roman += r
                number -= i

    return roman

print("Give the integer you want to be converted into a Roman number")
print("If you want to end the program give as input the number zero")
number = int(input())

while number != 0:
    print(Converter(number))
    print("Give the integer you want to be converted into a Roman number")
    print("If you want to end the program give as input the number zero")
    number = int(input())
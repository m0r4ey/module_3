# Рекурсия.
def get_multiplied_digits (number):
    if number == 0:
        number = 1
    str_number = str(number)
    first = int(str_number[0:1])
    if not (len(str_number) > 1):
        return first
    return first * get_multiplied_digits(int(str_number[1:]))

result1 = get_multiplied_digits(40203)
result2 = get_multiplied_digits(4020)
print(result1)
print(result2)
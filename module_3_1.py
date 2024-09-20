# Пространство имён.

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    length_string = len(string)
    upper_string = string.upper()
    lower_string = string.lower()
    return length_string, upper_string, lower_string


def is_contains(string, list_to_search):
    count_calls()
    is_true = False
    string = string.upper()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()
        if string == list_to_search[i]:
            is_true = True
    return is_true


calls = 0
print(string_info('m0rfey'))
print(string_info('FlowerS'))
print(string_info('eLepHant'))
print(is_contains('m0rfey', ['lmYl', 'morfey', 'mor4ey']))
print(is_contains('sunshine', ['sun', 'shine', 'SUNSHINE']))
print(calls)

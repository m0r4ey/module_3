# Распаковка позиционных параметров.

def print_params(a = False, b = 'm0rfey', c = 23):
    print (a, b ,c)


print_params()
# №1
print_params(1, 2, 3)
print_params('a', 'b', 'c')
print_params(c = 30, a = 50, b = 20)
print_params(b = 25)
print_params(c = [1,2,3])
# №2
values_list = [True, 'GOAT', 3.14]
values_dict = {'a': 1488, 'b': 365, 'c': 'shark'}
print_params(*values_list)
print_params(**values_dict)
# №3
values_list_2 = ['Are_you_good_boy?', True]
print_params(*values_list_2, 42)
print()

#Из примера
def append_to_list(*item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)
    print(list_my)

append_to_list(3, 4, 5, 'HOROSHO')
print("Введите строку")
n = input()
for i in range(len(n)):
    if n[i] == 'я':
        print('а', end = '')
    elif n[i] == 'Я':
        print('А', end = '')
    elif n[i] == 'z':
        print('a', end = '')
    elif n[i] == 'Z':
        print('A', end = '')
    else:
        print(chr(ord(n[i])+1), end='')

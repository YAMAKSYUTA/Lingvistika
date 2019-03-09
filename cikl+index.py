1) print("Введите число")
n = int(input())
print("Вводите строки")
for i in range(n):
    s = input()
    if s == "":
        print("Введена пустая строка")
        
2) print("Введите строку")
n = input()
if n[1] == 'к' or n[1] == 'л' or n[1] == 'и':
    for i in range(1, len(n), 2):
        print(n[i], end=' ')
else:
    for i in range(0, len(n), 2):
        print(n[i], end=' ')
        
3) print("Введите строку")
n = input()
if n[0] == 'а' or n[0] == 'э' or n[0] == 'е' or n[0] == 'я':
    for i in range(len(n)):
        print(n[i], end='')
else:
    for i in range(len(n)-1, -1 ,-1):
        print(n[i], end='')
        
4) print("Введите число")
n = int(input())
k=1
while n >= k:
    print(k, end = ' ')
    k *= 2
    
5) print("Введите число")
n = int(input())
for i in range(1, 11):
    print(n * i)
    
6) print("Введите строку")
n = input()
if len(n) < 6:
    print(n)
else:
    for i in range(len(n)//2):
        print(n[i], end = '')
  
7) print("Введите строку")
n = input()
for i in range(1, len(n), 2):
    if n[i] != 'п' and n[i] != 'о' and n[i] != 'и':
        print(n[i], end=' ')
print()
for i in range(0, len(n), 2):
    if n[i] != 'п' and n[i] != 'о' and n[i] != 'и':
        print(n[i], end=' ')

with open("text.txt", "r") as text:
    a = text.read()
    b = []
    b = a.split()
    for i in range(len(b)):
        b[i] = b[i].lower()
    print("Введите текст")
    n = input()
    while(n[len(n)-1] != '?'):
        print("Введите текст")
        n = input()
    new_words = n.split()
    c = 0
    for i in range(len(new_words)):
        new_words[i] = new_words[i].lower()
    for i in new_words:
        if i in b:
            c += 1
        if c == 2:
            break
    if c == 0:
        print("нет")
    elif c == 1:
        print("может быть")
    else:
        print("да")
    flag = 0
    for i in range(len(b)-1, -1, -1):
        if b[i][0] == new_words[0][0]:
            flag = 1
            print(b[i])
            break
    if flag == 0:
        print(42)
    count_a = a.count("а")
    count_k = a.count("к")
    x = count_a * count_k
    if len(b)-x < 0:
        print(b[2])
    else :
        print(b[len(b)-x-1])
    k = 0;
    ans = []
    for i in range(1, len(b)):
        if b[i][0] == '"' and b[i-1][len(b[i-1]-1)]:
            ans.append(i)
            k += 1
    if k != 0:
        dif = len(new_words[-2])%k +1
        if dif < len(a):
            print(a[dif], end = ' ')
            dif += 1
            while a[dif].find('"') != -1:
                print(a[dif], end = ' ')
            dif += 1

def Fact(num):
    l = []
    for i in range (1, num):
        if num%i == 0:
            l.append(i)
        else:
            pass

    print(l)

Fact(6)

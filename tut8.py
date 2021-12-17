def fact(number):
    if number == 1:
        return 1
    elif number > 1:
        return number*fact(number-1)

a = fact(6)
print(a)
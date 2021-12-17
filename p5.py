def Perfect(num):
    sum = 0
    for n in range(1, num):
        if num%n == 0:
            sum = sum + n
        else:
            pass
    
    if num == sum:
        print(f"{num} is a perfect number.")



for i in range(1, 101):
    Perfect(i)
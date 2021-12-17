def table(num, qty):
    if qty == 1:
        print(f"{num}*{qty} = {num*qty}")
    elif qty>1:
        print(f"{num}*{qty} = {num*qty}")
        table(num, qty-1)


table(12, 10)
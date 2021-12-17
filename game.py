def game():
    return  631

m = game()
print(f"The score is {m}")

f = open("hs.txt", "r")
n = int(f.read())
if m>n:
    q = open("hs.txt", "w")
    q.write(str(m))

f.close()
q.close()
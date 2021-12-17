# l1 = []
# for r in range(7):
#     fruit = input("Enter a fruit name: ")
#     l1.append(fruit)
# print(l1)


# marks = []
# for i in range(6):
#     m = int(input("Enter the marks : "))
#     marks.append(m)
# marks.sort()
# print(marks)


# t1 = (3, )
# t1[0] = 9


# l1 = [1, 2, 3, 4]
# sum = 0
# for i in range(4):
#     sum = sum + l1[i]
# print(sum)



t = (2, 0 ,4, 5, 0, 4, 0)
# print(t.count(0))
coutn = 0
for i in range(7):
    if t[i] == 4 :
        coutn+=1

print(coutn)
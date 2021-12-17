# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# d = int(input("Enter a number: "))


# if a>b and a>c:
#     if a>d:
#         print("a is largest")
#     else: 
#         print("d is largest")

# elif b>a and b>c:
#     if b>d:
#         print("b is largest")
#     else: 
#         print("d is largest")

# elif c>a and c>b:
#     if c>d:
#         print("c is largest")
#     else: 
#         print("d is largest")

# elif d>a and d>b:
#     if d>c:
#         print("d is largest")
#     else: 
#         print("c is largest")





# a = int(input("Enter marks of 1st subject: "))
# b = int(input("Enter marks of 2nd subject: "))
# c = int(input("Enter marks of 3rd subject: "))
# count = 0
# total = a+b+c

# for i in range(1):
#     if a > 33:
#         count = 1
#     else :
#         count = -1
#         break

#     if b > 33:
#         count = 1
#     else :
#         count = -1
#         break

#     if c > 33:
#         count = 1
#     else :
#         count = -1
#         break

#     if total//3 > 40:
#         count = 1
#     else:
#         count = -1
#         break

# if count == 1:
#     print("You are pass.")
# elif count == -1:
#     print("You are fail.")




# s = "Hello i i free s"
# if s.find("subscibe ")>0 or s.find("free")>0:
#     print("Scam")
# else:
#     print("No scam")




# u = "Priyanshu"
# if len(u)>10:
#     print("It contains more than 10 letters")
# else:
#     print("It doesn't contain more than 10 letters")





# l = ["Priyanshu", "Jhansla", "Kalu", "Bandar"]
# name = input("Enter a name: ")
# count = 0
# for i in range(4):
#     if name == l[i]:
#         count = 1
#         break
#     else :
#         count = -1

# if count == 1:
#     print("It contains the name.")
# elif count == -1:
#     print("It does not contain the name.")




marks = int(input("Enter the percentage: "))
if marks>90 and marks<100:
    print("Ex")
elif marks in range(80, 90):
    print("Good")
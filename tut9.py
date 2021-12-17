# f = open("a.txt", "r")
# # t = f.read()
# # print(t)

# t = f.readline()
# print(t)
# f.close()



# f = open("b.txt", "w")
# f.write("Hello, this is another test file.")
# f.close()




# f = open("b.txt", "a")
# f.write("\nThis is appended text")
# f.close()




f = open("poem.txt", "r")
m = f.read()
print(m)

if "twinkle" in m:
    print("It is present.")
else:
    print("It is not present.")

f.close()
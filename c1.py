# import math
# class Circle:
#     # def __init__(self, radius):
#     #     self.radius = radius
#     def getArea(self):
#         print(f"Area = {math.pi*self.radius*self.radius}")
#     def getCircumference(self):
#         print(f"Circumference = {math.pi*2*self.radius}")


# c = Circle
# c.radius = 39
# # c.getArea()
# c.getCircumference()



import math as m

class Circle:

    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        print(f"The area of  given circle with radius {self.radius} is {m.pi*self.radius*self.radius}")


cir = Circle(4)
# cir.radius = 4
cir.getArea()






# class Temp():
#     def fe(temp):
#         return (temp*(9/5))+32
#     def cel(far):
#         return (far-32)*(5/9)

# t = Temp
# print(t.fe(32))



# class Point(object):
#     def __init__(self,x = 0,y = 0):
#         self.x = x
#         self.y = y

#     def distance(self):
#         """Find distance from origin"""
#         return (self.x**2 + self.y**2) ** 0.5


# p1 = Point(6,8)
# print(p1.distance())
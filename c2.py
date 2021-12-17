class Stud:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def dispaly(self):
        print(self.name)
        print(self.roll_no)
    def setMarks(self, marks):
        self.marks = marks
    def setAge(self, age):
        self.age = age


s = Stud("Priyanshu", 88008)
s.setAge(18)
s.setMarks(87)
s.dispaly()
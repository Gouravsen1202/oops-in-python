class Student:
    def sum(self,name,age):
        self.x=name
        self.y=age
        print(self.x,self.y)
        Student.surname='sen'
obj=Student()
obj.sum('gorav',33)
print(Student.surname)

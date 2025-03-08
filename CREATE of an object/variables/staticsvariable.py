# class Student:
#     school='vvv'
#     city='bhopal'#ese hi variable ko statiic variable bolte hai
#     def __init__(self,name,age):
#         self.x=name
#         self.y=age
#     def show(self):
#         print(self.x,self.y)
#         print(Student.school)#agar static variable ko prinet krna ho to class aur variable ka name likhna padta hia
#         print(Student.city)
# obj=Student('gourav',22)
# obj.show()
# obj2=Student('ajay',22)
# obj2.show()


# 2  all are the static variables

class Studet:
    school='vvv'# static variabel pure code me khi par bhi bna sakte hai
    def __init__(self,name,roll):
        self.x=name
        self.y=roll
        Studet.city='bhopal'# static variabel pure code me khi par bhi bna sakte hai
    def show(self):
        Studet.s_code=123# static variabel pure code me khi par bhi bna sakte hai
    def display(self):
        print(Studet.s_code)
        print(Studet.city)
        print(Studet.school)
        print(Studet.priencipal)
        # print(self.x,self.y)
Studet.priencipal='gourav'# static variabel pure code me khi par bhi bna sakte hai
obj=Studet('AJAY',22)
obj.show()
obj.display()
print(Studet.s_code)

    
    
    
    
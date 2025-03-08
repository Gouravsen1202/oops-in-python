# class Mobil:
#     def sum():
#         a=6
#         b=20
#         c=a+b
#         print("f")
# obj=Mobil
# obj.sum()
# print(obj)

# class Mobil:
#     def __init__(self):
#         self.model='realme'
#     def show_model(self):
#         print('model:',self.model)
# realme=Mobil()
# redmi=Mobil()

# class MYclass():
#     def show():
#         print("hi brp")
# a=MYclass
# a.show()

# class Myclass:
#     def sum():
#         a=int(input("enter np"))
#         b=int(input("enter 2no "))
#         c=a+b
#         print(c)
#     def sub():
#         a=20
#         b=10
#         c=a-b
#         print("2no func is",c)
#     def even():
#         pass
# obj=Myclass

# obj.sub()

# class Subject:
#     def __init__(self,name,no):
#         self.x=name
#         self.y=no
# object=Subject('goursv',89)
# print(object.x)
# print(object.y)


class Subject:
    def sum(self,name,age):
        self.x=name
        self.y=age
        print(self.x)
        print(self.y)
obj=Subject()
obj.sum('gourav',22) #ask sir normal function me nhi kr sakte hia kya
print(obj.sum('gourav',22))
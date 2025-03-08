#1.
#  class Student:
#     def __init__(self):
#         print("constructor caalled")

# obj=Student# yha par inbuild constructor call hota hai
# obj=Student()# ye parenthisi()responsibal hai apne constructor ko call krne ke liye
# obj.__init__()# yha bhi call ho jayega
# # consturctor 1 specisl type ka methord hai jo ki object bnate time autometicly cal ho jate hia



# 2.
class Student:
    def __init__(self):
        print("constructor caalled")
    def __init__(self):
        print("constructor  x caalled")
obj=Student()
# ye ho rha hai function overloading ho rha hia jo ki 2 same name ke function ko 
# banate hi aor fir call krte hai to wo function ko overload kr dete hia new value ayegi

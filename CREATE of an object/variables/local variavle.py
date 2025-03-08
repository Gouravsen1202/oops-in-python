# jis blaock me apan ne diclilar kra hia bus ushi me hi apan print hoga uske bahar use nhi kr sakte
# apne bloack je ander hi access karenge bus


class Studet:
    
    def __init__(self,name,roll):
        self.x=name
        self.y=roll
        Studet.city='bhopal'#
    def show(self):
        
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
class Human:
    class_name = "Human"
    
    def __init__(self):
        self.name = "大泉"
        
    def show(self):
        print(self.name)
    
print(Human.class_name)

class Hoge:
    class_call_count = 0
    
    def __init__(self):
        
        Hoge.class_call_count += 1
        
Hoge()
print(Hoge.class_call_count)

Hoge()
print(Hoge.class_call_count)

Hoge()
print(Hoge.class_call_count)

class Human1():
    def __init__(self):
        self.name = None
        self.address = None
        
    def show(self):
            print(self.name)
            print(self.address)
            
class Actor(Human1): pass

actor = Actor()

actor.name = "大泉"
actor.address = "北海道"

actor.show()


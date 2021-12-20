class Car:
    class_name = "Car"
    
    def __init__(self):
        self.name = None
        
        
    def show(self):
        print(self.name)
        
        
car = Car()

car.name = "セダン"

car.show()

print(Car.class_name)


class Hoge1:
   def hello(self):
       print("Hello Python!")
       
hoge = Hoge1()
hoge.hello()
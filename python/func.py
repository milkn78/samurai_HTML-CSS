def hello(str):
    print(str)
    
    
hello("Hello World!")


def calc(a,b):
    print(a * b)
    
calc(3,5)

def triangle_area(a,h):
    return a * h / 2

print(triangle_area(2,3))

file_list = []
def add_list(name):
    file_name = name + ".py"
    file_list.append(file_name)

add_list("function")
print(file_list)

add_list("hello")
print(file_list)
for num in range(0, 10, 1):
    print("Hello World!")
    
animals = ["dog", "cat", "bird"]
for animal in animals:
    print(animal)
    
for number in range(1, 31, 1):
    print(number)
    
for number in range(1, 31, 1):
    if number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
for number in range(1, 31, 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
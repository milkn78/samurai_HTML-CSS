
def check(num):
    if num == 42:
        print("Answer to the Ultimate Question of Life, the Universe, and Everything")
check(42)

even_num = []
odd_num = []

def soft_number(num):
    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)
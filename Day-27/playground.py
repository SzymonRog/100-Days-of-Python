def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(add(1,2,3,4,5))

def calculate(**kwargs):
    print(kwargs)


calculate(a=1, b=2, c=3)
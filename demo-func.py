apple = 100
a = 1
def fun():
    global a
    a = 20
    return a+100

print(apple)
print("past a is",a)
print(fun())
print("now a is",a)
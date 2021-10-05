x = 10

def f():
    # global x
    x = 12
    print(x)

f() # 12
print(x) # 10

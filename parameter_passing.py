def f_bad(p):
    p = 7 + p

def f_good(p=3):
    return 7 + p

def for_unpacking(x, y, z) -> int:
    return x + y + z

x = 10
f_bad(x)
print(x)
print(f_good(x))
print(f_good())

lst = [1, 2, 3]
print(for_unpacking(*lst)) # for_unpacking(lst[0], lst[1], lst[2])

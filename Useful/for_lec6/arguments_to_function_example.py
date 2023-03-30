def fun(a, b):  # a -> x, b -> y [     ,    ,    ]
    print(f"Before {id(a)=}")     #  1  ->2  ->3
    print(f"Before {id(b)=}")     #-> 1000
    a = 1000     # a -> 1000
    b[0] = 1000  # b[0] -> 1000
    print(f"After {id(a)=}")
    print(f"After {id(b)=}")
    return a, b


x = 100 # x -> 100
z = 500
y = [z, 2, 3] # y -> [1, 2, 3]
print(f"{id(x)=}")
print(f"{id(y)=}")
fun(x, y)
print(x)  # 100
print(y)  # [1, 2, 3, 1000]
print(z)  # 500
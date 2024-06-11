divide_give_int = lambda x,y : (x//y)
normal_divide = lambda x,y : (x/y)
print(divide_give_int(5,2))


def divide(fx):
    return fx(5,2)

print(divide(divide_give_int))
print(divide(normal_divide))

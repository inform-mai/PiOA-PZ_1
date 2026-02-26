x1 = -2
x2 = 4
dx = 1
a = 1
b = 1
c = 1


def F(x):
    if (a + b) / c > 0 and x != 0:
        return c * x / (a + b)
    if x == 0:
        return 0
    else:
        return a * x ** 2 - b * x + c


cnt = 1
for x in range(x1, x2 + 1, dx):
    result = F(x)
    print(f'{cnt}) x = {x} -> F(x) = {result}')
    cnt += 1

def fibonacci(n):
    n1 = 0
    n2 = 1

    for k in range(n):
        c = n1 + n2
        n1 = n2
        n2 = c
    return n1
print(fibonacci(8))
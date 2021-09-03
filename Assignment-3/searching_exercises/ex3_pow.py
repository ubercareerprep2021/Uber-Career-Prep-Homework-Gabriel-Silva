def power(x: int, n: int):
    if n == 0:
        return 1
    else:
        base = x
        for i in range(abs(n)-1):
            x *= base
        if n > 0:
            return x
        else:
            return 1/x

if __name__ == '__main__':
    x = 2
    n = 10
    print(power(x, n)) # result 1024
    n = -2
    print(power(x, n)) # result 0.25
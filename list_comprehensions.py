if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


summe = [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if x+y+z != n]
print(summe)
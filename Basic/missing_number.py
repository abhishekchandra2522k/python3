n = int(input())

a = list(map(int, input().strip().split(" ")))

asum = sum(a)

Sum = n * (n + 1) / 2

print(int(Sum - asum))
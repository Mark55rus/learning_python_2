n, m = map(int, input().split())
lst = []
while n <= m:
    lst.append(n ** 2)
    n += 1
print(*lst)
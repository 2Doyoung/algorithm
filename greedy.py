n, k = (map(int, input().split()))
result = 0

# 17 4
while True:
    target = (n // k) * k # 16, 4
    result += (n - target) # 1, 2 4
    n = target # 16, 4 0

    if n < k: # 16 4, 4 4
        break

    result += 1 # 2 3
    n //= k # 4 1

result += (n - 1)
print(result)
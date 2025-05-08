a = 1000
print(a)

a = -7
print(a)

a = 0
print(a)

a = 15.23
print(a)

a = 5.
print(a)

a = -.7
print(a)

a = 1e9
print(a)

a = int(1e9)
print(a)

a = 75.25e1
print(a)

a = 0.3 + 0.6
print(a)

if round(a, 4) == 0.9:
    print("TRUE")
else:
    print("FALSE")

a = round(123.456, 2)
print(a)

a = 10 % 3
print(a)

a = 10 / 3
print(a)

a = 10 // 3
print(a)

print(10 ** 2)
print(9 ** 0.5)

a = list()
print(a)

a.append(1)
a.append(2)
print(a)

a.pop(1)
print(a)

n = 10
a = [0] * n
print(a)

a = [1, 2, 3, 4, 5, 6]
print(a[1:5])

array = [i for i in range(10)]
print(array)

array = [i for i in range(20) if i % 2 == 1]
print(array)

array = [i * i for i in range(10)]
print(array)

n = 4
m = 3

array = [[0] * m for _ in range(n)]
print(array)

array = [i for i in range(10)]
print(array)
array.sort()

print(array)
array.sort(reverse=True)

data = list(map(int, input().split()))

data.sort()
print(data)
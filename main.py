# Test
print("Hello World")
print("Hello Python")

n = 10
m = 20
print(n)
print(n + m)
print(n * m)
print(n / m)
print(n % m)
print(m % n)
print(m - n)

"""
==	같다 포함
!=	같지 않다 제외
+=	더해서 저장	누적
%	나머지 배수 판별
"""

total = 0

for i in range(1, 7):
    if i % 4 != 0:
        total += i

total = 17
print(f"i = {total}")
# 3

i = 2
n = 600851475143

while n/i != 1:
    if n%i == 0:
        n = n/i
    else:
        i = i + 1

print(i)

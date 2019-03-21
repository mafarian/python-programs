# 2

s = 2
i0 = 1
i1 = 2
i2 = 3

while i2 <= 4000000:
    if i2%2 == 0:
        s = s + i2
    
    i0 = i1
    i1 = i2
    
    i2 = i1 + i0

print(s)

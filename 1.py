# 1

s = 0
maxn = 1000

for n in range(1,1000):
    if n%3 == 0:
        s = s + n
    elif n%5 == 0:
        s = s + n
        
print(s)

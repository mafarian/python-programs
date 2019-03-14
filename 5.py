# 5

s = 0
n = 2
m = 1

while s < 19:
    c = 0
    m = m*n
    
    for i in range(2,21):
        if m%i == 0:
            c = c + 1
    
    if c == s:
        m = m//n
        n = n + 1
    elif c > s:
        s = c

print(m)

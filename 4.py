# 4

grt = 0

for i in range(999,101,-1):
    for j in range(999,101,-1):
        n = str(i*j)
        m = n[::-1]
        
        if m == n:
            if int(m) > grt:
                grt = int(m)
                
print(grt)

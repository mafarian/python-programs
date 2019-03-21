# 9

k = 0

for a in range(0,1000):
    for b in range(a+1,1000):
        c = (a**2 + b**2)**0.5
        if c > b:
            if a + b + c == 1000:
                print(int(a*b*c))
                k = 1
        if k == 1:
            break
    if k == 1:
        break

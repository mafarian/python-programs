# 7 beta
# import time
# inicio = time.time()

k = 1
n = 1

while k < 10001:
    c = 0
    i = 1
    n = n + 2
    
    while c == 0:
        i = i + 2
        if n%i == 0:
            c = 1
            if n == i:
                k = k + 1
    
print(n)
# print("%s s" % (time.time() - inicio))

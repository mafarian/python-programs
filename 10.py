# 10

# import time
# inicio = time.time()

NUM = 2000000
n = [0]*NUM

for i in range(2,NUM):
    n[i] = i

k = 1
s = 0

while k < NUM-1:
    i = 1
    k = k + 1
    
    while n[k] != 0:
        i = i + 1
        if ((k%i == 0) and (k == i)) or (i >= sqrt(NUM)+1):
            s = s + n[k]
            j = i
            while (j+i) < NUM:
                j = j+i
                n[j] = 0
            break
    
print(s)
# print("%s s" % (time.time() - inicio))

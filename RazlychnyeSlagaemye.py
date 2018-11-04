n = 0
while n < 1 or n > 1e9 :
    n = int(input())

k=1
s=[]
while n>0:
    if n >= 2*k+1:
        n = n-k
        s.append(k)
        k = k+1
    else:
        s.append(n)
        n=0


print(k)
print(' '.join([str(i) for i in s]))




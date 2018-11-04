n = 0
while n < 1 or n > 100:
    n = int(input())

i = 0
A = []
while i < n:
    x1, x2 = map(int, input().split())
    if not ((x1 > 1e9) or (x2 > 1e9) or (x1 < 0) or (x2 < 0)):
        A.append([x1, x2])
        i = i+1

for i in range(n):
    if A[i][0] < A[i][1]:
        temp = A[i][0]
        A[i][0] = A[i][1]
        A[i][1] = temp

A.sort()

i = 0
j = 0
res = []
while i <= len(A) and (len(A) != 0):
    res.append(A[i][0])
    A.remove(A[i])
    while j < len(A) and (len(A) != 0):
        if (A[j][1] <= res[len(res)-1]) and (len(A) != 0):
            A.remove(A[j])
            j=j-1
        j = j+1
    j=0
print(len(res))
print(' '.join([str(i) for i in res]))
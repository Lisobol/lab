n = 0
while n < 1 or n > 1e3 or W < 0 or W > 2*1e6:
    n, W = map(int, input().split())
cw = []
w = []
i = 0

while i < n:
    ci, wi = map(int, input().split())
    if not (ci < 0 or ci > 2*1e6 or wi < 0 or wi > 2*1e6):
        x = ci / wi
        cw.append([x, ci, wi])
        i = i+1

cw.sort()
cw.reverse()

Sum = 0
for i in range(n):
    if cw[i][2] <= W and W > 0:
        Sum = Sum + cw[i][1]
        W = W - cw[i][2]
    elif W > 0:
        Sum = Sum + W*cw[i][0]
        W = 0
print('%.3f' % Sum)



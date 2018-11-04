w, e = -2*1e9, 2*1e9
while True:
    a, b =map(int, input().split())
    if not w < b < e or not w < a < e:
        break
    print(a+b)
    break


# ab,a,b = 0,0,0
# with open('input.txt','r') as f:
#     l = [line.strip() for line in f]
#     # print(l[0])
#     w, e = -2*1e9, 2*1e9
#     while True:
#         a, b = map(int, l[0].split())
#         if not w < b < e or not w < a < e:
#             break
#         ab = a+b
#         break
#
# with open('output.txt','w') as f:
#     if w < b < e and w < a < e:
#         f.write(str(ab)+'\n')

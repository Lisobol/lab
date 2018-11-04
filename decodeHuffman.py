

leng,strlen = map(int, input().split())
arr=[]
i=0
# print(i,leng)
while i<leng:
    a,b =map(str, input().split())
    arr.append([a,b])
    list(arr[i][0])
    # print(arr[i][0][0])
    arr[i][0]=arr[i][0][0]
    i = i + 1

g=''
s=str(input())

while len(s)>0:
    for i in range(len(arr)):
        if s.startswith(str(arr[i][1])):
            g=g+str(arr[i][0][0])
            s=list(s)
            for h in range(len(arr[i][1])):
                s.remove(s[0])
            s=''.join(s)


print(g)
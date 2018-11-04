import sys

str = str(input())
if (str==r'^[a-z]+$')or len(str) > 10000 :
    print('!')
    sys.exit()


class Tree():
    def __init__(self,n,l,r):
        self.left = l
        self.right = r
        self.node = n


list(str)

arr = []
for s in str:
    if [0,s,'','l'] not in arr:
        arr.append([0,s,'','l'])


if len(arr)==1:
    l=[1,len(str),arr[0][1],0]
    print('{0} {1}'.format(*l))
    print('{2}: {3}'.format(*l))
    # print('1 ',len(str))
    # print(arr[0][1],':','0')
    print('0'*len(str))
    exit()
for s in str:
    for i in range(len(arr)):
        if s == arr[i][1]:
            arr[i][0]=arr[i][0]+1

a=[]
arr1=list(arr)
len1=len(arr)
t=[]
while len(arr)>1:
    i0=list(min(arr))
    arr.remove(min(arr))
    j0=list(min(arr))
    arr.remove(min(arr))
    arr.append([i0[0]+j0[0],i0[1]+j0[1],'','n'])
    ij=[i0[0]+j0[0],i0[1]+j0[1],'','n']
    t.append(Tree(ij,i0,j0))
t.reverse()
for i in range(len(t)):
    t[i].left[2]=t[i].node[2]+'0'
    t[i].right[2] = t[i].node[2] + '1'
    l=t[i].left[1]
    r=t[i].right[1]
    l1 = t[i].left[2]
    r1 = t[i].right[2]

    for k in t:
        if k.node[1]==l:
            k.node[2]=l1
        if k.node[1] == r:
            k.node[2] = r1
    for a in arr1:
        if a[1]==t[i].left[1]:
            a[2]=t[i].left[2]
        if a[1]==t[i].right[1]:
            a[2]=t[i].right[2]

g=''
list(str)
for s in str:
    for a in arr1:
        if s==a[1]:
            g=g+a[2]


print(len(arr1), '',len(g))

for i in range(len(arr1)):
    l=[arr1[i][1],arr1[i][2]]
    # print(, ':', )
    print('{0}: {1}'.format(*l))

print(g)

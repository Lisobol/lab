
def inp():
    n=0
    a1=[]
    while n < 1 or n > 1e5 or len(a1) != n:
        a=[[int(i), x-1] for x,i in enumerate(input().split())]
        n=a[0][0]
        del a[0]
        a.sort()
        for ai in a:
            if ai[0] > 1e9:
                break
        return n,a


def inp1():
    k=0
    b=[]
    while k < 1 or k > 1e5 or len(b) != k:
        b = list(map(int,input().split()))
        k = b[0]
        del b[0]
        for bi in b:
            if bi > 1e9:
                break
        return k,b



def bin(a,b,k,n):
    res = ['-1' for i in range(k)]
    for i in range(k):
        for ki in range(k):
            l = 0
            r = n-1
            while l <= r:
                m = int((l+r)/2)
                if a[m][0] == b[ki]:
                    res[ki]=str(a[m][1]+1)
                    break
                elif a[m][0] > b[ki]:
                    r = m-1
                else:
                    l = m+1
        return res

def main():
    n,a=inp()
    k,b=inp1()


    print(' '.join(bin(a,b,k,n)))

if __name__ == '__main__':
    main()

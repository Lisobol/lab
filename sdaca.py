n = 0
while n < 1 or n > 1e3 :
    n = int(input())

n_25= int(n/25)
n = n - 25*n_25
n_10=int(n/10)
n = n - 10*n_10
n_5=int(n/5)
n = n - 5*n_5
n_1=int(n/1)
n = n - 1*n_1
k=n_25+n_10+n_5+n_1
print(k)
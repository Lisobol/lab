import sys
n = 0
while n < 1 or n > 1e5 :
    n = int(sys.stdin.read())
    print(n)
heap = []


def siftDown(i, heap):
    while 2 * i + 1 < len(heap):
        left = 2 * i + 1
        right = 2 * i + 2
        j = left
        if right < len(heap) and int(heap[right]) > int(heap[left]):
            j = right
        if int(heap[i]) >= int(heap[j]):
            break
        heap[i], heap[j] = heap[j],heap[i]
        i = j


def siftUp(i,heap):
    while int(heap[i]) > int(heap[int((i - 1) / 2)]):
        heap[i], heap[int((i - 1) / 2)]= heap[int((i - 1) / 2)], heap[i]
        i = int((i - 1) / 2)


def insert(heap,x):
    heap.append(x)
    if len(heap) > 1:
        siftUp(len(heap) - 1, heap)

def extractMax(heap):
    max = heap[0]
    heap[0] = heap[len(heap) - 1]
    heap.__delitem__(len(heap)-1)
    siftDown(0, heap)
    return max

x = 0
for i in range(n):
    # s = input()
    s=sys.stdin.read()
    if s.startswith('Insert'):
        oper, x = map(str, s.split(' '))
        int(x)
        if oper == 'Insert':
           insert(heap,int(x))
    else:
        if s == 'ExtractMax':
            print(extractMax(heap))



# T = []
#
#
# def t_insert(x):
#     T.append(x)
#
#
# def t_extract_max():
#     m = 0
#     for i in range(1, len(T)):
#         if T[i] > T[m]:
#             m = i
#     result = T[m]
#     del T[m]
#     return result
#
#
# n =10000
# for i in range(n):
#     insert(heap,i)
#     t_insert(i)
# for i in range(n):
#     a = extractMax(heap,n)
#     b = t_extract_max()
#     if a == b:
#         print(i, a)
#     else:
#         print(i, a, b, "ERROR")
#         break

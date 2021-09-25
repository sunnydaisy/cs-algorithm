# O(NlogN)의 시간복잡도 (퀵정렬, 병합정렬)
import sys
# 퀵정렬
def quick(n):
    if len(n) <= 1:
        return n
    pivot = n[len(n)//2]
    left, right, equal = [],[],[]
    left = [i for i in n if i<pivot]
    right = [i for i in n if i>pivot]
    equal = [i for i in n if i==pivot]
    return quick(left)+equal+quick(right)

# 병합정렬
def merge(left,right):
    v = []
    i=j=0
    while(i<len(left)&j<len(right)):
        if left[i]<rigth[j]:
            v.append(left[i])
            i+=1
        else:
            v.append(right[j])
            j+=1
    if i==len(left):
        v = v+right[j:]
    if j==len(right):
        v = v+left[i:]
def mergesort(n):
    if len(n)<=1:
        return n
    m = len(n)//2
    l = mergesort(n[:m])
    h = mergesort(n[m:])
    return merge(l,h)

num = int(sys.stdin.readline().strip())
n = [int(sys.stdin.readline().strip()) for i in range(num)]
answer = quick(n)

print(answer)
# for i in answer:
#     print(i)
import sys

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

def solution():
    n = int(sys.stdin.readline())
    array = []
    for _ in range(n):
        array.append(int(sys.stdin.readline()))
    array = quick_sort(array)
    for i in array:
        print(i)

solution()
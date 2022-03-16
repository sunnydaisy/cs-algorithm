

# 이진 탐색

# 재귀를 사용한 방법
def binary_search(array, target, start, end):
    if start > end:
        return
    mid = (end + start) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)



# 반복문 사용 방법
def binary_search(array, target, start, end):
    while start <= end:
        mid = (end + start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

array = [1, 3, 5, 9, 11, 13, 15, 17, 19]
print(binary_search(array, 11, 0, len(array) - 1))
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 1. 퀵정렬 파이썬 버전 (속도가 일반 퀵정렬보다는 조금 늦음)
# def quick_sort(array):
# 	if len(array) <= 1:
# 		return array

# 	pivot = array[0]
# 	tail = array[1:]

# 	front = [i for i in tail if i <= pivot]
# 	rear = [i for i in tail if i > pivot]

# 	return quick_sort(front) + [pivot] + quick_sort(rear)


# 2. 퀵정렬 일반 버전
def quick_sort(array, start, end):
	if start >= end:
		return

	pivot = start
	front = start + 1
	rear = end

	while front <= rear:
		while front <= end and array[front] <= array[pivot]:
			front += 1
		while rear > start and array[rear] >= array[pivot]:
			rear -= 1
		if front > rear:
			array[rear], array[pivot] = array[pivot], array[rear]
		else:
			array[front], array[rear] = array[rear], array[front]
	print(array)
	quick_sort(array, start, rear - 1)
	quick_sort(array, rear + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
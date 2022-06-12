def binary_search(array, target, start, end):
    while start <= end:
        mid = (end + start) // 2
        if array[mid][0] == target:
            return mid
        elif array[mid][0] > target:
            end = mid - 1
        else:
            start = mid + 1
    if array[mid][0] < target:
        return mid + 1
    return mid

def solution(n, plans, clients):
    answer = []
    service = []
    last_service = []

    for plan in plans:
        tmp = list(map(int, plan.split()))
        service.append((tmp[0], tmp[1:] + last_service))
        last_service += tmp[1:]
    
    for client in clients:
        tmp = list(map(int, client.split()))
        data = tmp[0]
        services = tmp[1:]
        # print(service)
        result = binary_search(service, data, 0, len(service))
        print(result)
    return answer

solution(5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"])

def solution(priorities, location):
    process = []
    before_max_num_index = 0

    for _ in range(len(priorities)):
        max_num = max(priorities)
        max_num_index = priorities.index(max_num)

        # 최대값이 두개 이상고 처음 실행하는게 아닐때
        if priorities.count(max_num) >= 1 or not process :
            # 이전 최대값 인덱스가 끝에 있지 않을 때
            if before_max_num_index != len(priorities):
                right_arr = priorities[before_max_num_index:]

                # 최대값이 이전 최대값 오른쪽에 있을 때
                if max(right_arr) == max_num:
                    max_num_index = right_arr.index(max_num) + before_max_num_index

                # 최대값이 이전 최대값 왼쪽에 있을 때
                else:
                    None
            # 이전 최대값이 끝에 있을 때
            else:
                None


        # 최대값 인덱스 넣기
        process.append(max_num_index)

        # 최대값 0으로 바꾸기
        priorities[max_num_index] = 0

        before_max_num_index = max_num_index









    return process.index(location) +1



priorities = [2, 1, 3, 2]
location = 2

print(solution(priorities, location))
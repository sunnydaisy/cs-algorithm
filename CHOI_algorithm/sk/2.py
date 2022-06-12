from sqlalchemy import true


def vip_ck(peridos, payments):
    result = False
    if payments >= 900000:
        if peridos >= 24:
            result = True
    elif payments >= 600000:
        if peridos >= 60:
            result = True
    return result

def solution(periods, payments, estimates):
    answer = [0, 0]
    n = len(periods) # 고객 수
    report = [[] for _ in range(n)]

    for i in range(n):
        y_payment = sum(payments[i])
        n_payment = sum(payments[i][1:]) + estimates[i]
        report[i] = [periods[i], y_payment, n_payment, vip_ck(periods[i], y_payment), vip_ck(periods[i], n_payment)]
    
    for custom in report:
        if custom[3] is False and custom[4] is True:
            answer[0] += 1
        elif custom[3] is True and custom[4] is False:
            answer[1] += 1
    return answer


solution()
# 프로그래머스 위클리 챌린지 4주차: 직업군 추천하기
'''개발자의 언어 선호도에 따른 직업군 언어 점수 계산, 가장 높은 점수이면서 사전순 1번째 직업군 출력'''
from collections import Counter
def solution(table, languages, preference):
    score={}
    for i in table:
        for lang,pref in zip(languages,preference):    
            if lang in i.split():
                score[i.split()[0]] = score.get(i.split()[0],0)+(6-i.split().index(lang)) * pref
                
    return sorted(score.items(), key=lambda item:[-item[1], item[0]])[0][0]
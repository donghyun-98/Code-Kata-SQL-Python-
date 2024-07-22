def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생이 도난당헀을 경우
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    #  reserve의 요소 i에 대해 for 문을 돌며 앞번호, 뒷번호가 있으면 lost 에서 제거.
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
                
    return n - len(set_lost)
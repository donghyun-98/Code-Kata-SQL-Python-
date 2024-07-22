def solution(X, Y):
    # 0~9 까지 각 숫자의 빈도 체크
    count_X = [0]*10
    count_Y = [0]*10
    
    for x in X:
        count_X[int(x)] += 1
    
    for y in Y:
        count_Y[int(y)] += 1
    
    # 공통으로 나타나는 숫자 k 찾기
    k  = []
    for i in range(9, -1, -1):
        common_count = min(count_X[i], count_Y[i])
        if common_count > 0:
            k.extend([str(i)] * common_count)
    
    answer = ''.join(k)
    
    # 조건에 따른 return
    if not answer:
        return '-1'
    elif answer == '0' * len(answer):
        return '0'
    else:
        return answer
def solution(n,a,b):
    answer = 0
    a_idx, b_idx = 0, 0
    
    # a, b가 같아질 때까지 반복
    while a != b:
        # a와 b에 각각 1씩 더한 후 2로 나눈 몫으로 업데이트 해주는데
        # 그 이유는 재배정되는 번호를 표현하기 위해.
        a, b = (a+1) // 2, (b+1) // 2
        answer += 1
        
    return answer
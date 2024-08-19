def solution(progresses, speeds):
    answer = []
    remain_days = []
    
    # 각 기능의 남은 일수 계산
    for i in range(len(progresses)):
        # divmod를 사용해 만약 나머지가 있다면 하루가 더 필요한 것이니 quotient + 1
        quotient, remainder = divmod((100 - progresses[i]), speeds[i]) 
        if remainder != 0:
            quotient += 1
        remain_days.append(quotient)

    # 배포 그룹 계산
    cnt = 1
    start = remain_days[0]
    for i in range(1, len(remain_days)):
        # 시작 작업 완료일보다 현재 작업 완료일이 작거나 같으면 같은 배포 그룹
        if start >= remain_days[i]:
            cnt += 1
        else:  # 현재 작업 완료일이 더 크다면 새로운 배포 그룹 시작 설정 및 cnt 초기화
            start = remain_days[i]
            answer.append(cnt)
            cnt = 1
    
    # 마지막 배포 그룹 추가
    answer.append(cnt)
    
    return answer
def solution(n, m, section):
    count = 0  # 페인트칠 횟수
    i = 0  # 현재 검사할 section 인덱스

    while i < len(section):
        count += 1  # 새로운 페인트칠 시작
        end = section[i] + m - 1  # 현재 롤러의 끝 위치 계산
        
        # 현재 롤러로 커버되는 구역의 다음 구역을 찾음
        while i < len(section) and section[i] <= end:
            i += 1

    return count
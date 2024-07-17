def solution(n, m, section):
    count = 0  # 페인트칠 횟수
    current_end = 0  # 현재 롤러로 커버할 수 있는 마지막 구역

    for start in section:
        if start > current_end:  # 현재 구역이 롤러로 커버되지 않으면
            count += 1  # 새로운 페인트칠 시작
            current_end = min(start + m - 1, n)  # 롤러의 끝 위치를 벽의 끝을 넘지 않도록 갱신

    return count
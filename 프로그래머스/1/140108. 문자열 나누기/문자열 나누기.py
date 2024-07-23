def solution(s):
    answer = 0
    i = 0  # 인덱스 시작 위치

    while i < len(s):
        x = s[i]
        x_count = 0
        other_count = 0

        for j in range(i, len(s)):
            if s[j] == x:  # x 와 같은 문자면 x_count 올리고
                x_count += 1
            else:  # 나머지 다른 문자면 other_count 를 올린다.
                other_count += 1

            if x_count == other_count:
                i = j + 1  # 분리된 문자열 다음 인덱스로 이동
                break
        else:
            i = len(s)  # 남은 부분이 더 이상 없을 때

        answer += 1

    return answer
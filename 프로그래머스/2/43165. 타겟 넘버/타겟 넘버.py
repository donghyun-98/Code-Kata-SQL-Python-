def dfs(numbers, target, idx, values, cnt):  # idx: 깊이, values: 현재까지의 합, cnt: 타겟 넘버를 만들 수 있는 방법의 수
    # 깊이가 끝까지 닿았고, 합이 타겟과 같으면 카운트를 증가
    if idx == len(numbers):
        if values == target:
            return cnt + 1
        return cnt

    # 재귀함수로 탐색을 진행 (카운트 값을 계속 넘겨줌)
    cnt = dfs(numbers, target, idx + 1, values + numbers[idx], cnt)
    cnt = dfs(numbers, target, idx + 1, values - numbers[idx], cnt)
    return cnt

def solution(numbers, target):
    cnt = dfs(numbers, target, 0, 0, 0)  # 초기 인덱스, 합, cnt는 0으로 시작
    return cnt
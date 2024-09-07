from collections import deque

def solution(x, y, n):
    # BFS를 위한 큐 초기화: (현재 숫자, 연산 횟수)
    queue = deque([(x, 0)])
    
    # 방문 여부를 체크하는 리스트 (중복 계산 방지)
    visited = [False] * (y + 1)
    visited[x] = True
    
    # BFS 시작
    while queue:
        current, operations = queue.popleft()
        
        # y에 도달하면 연산 횟수를 반환
        if current == y:
            return operations
        
        # 가능한 연산: n을 더하기, 2배 곱하기, 3배 곱하기
        for next_val in (current + n, current * 2, current * 3):
            # y를 넘지 않고 방문하지 않은 숫자만 큐에 추가
            if next_val <= y and not visited[next_val]:
                visited[next_val] = True
                queue.append((next_val, operations + 1))
    
    # y에 도달할 수 없으면 -1 반환
    return -1
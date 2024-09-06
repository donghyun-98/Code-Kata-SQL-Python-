def solution(topping):
    left_set = set()  # 철수의 토핑 가짓수
    right_count = {}  # 동생의 토핑 가짓수
    
    # 처음엔 모든 토핑이 동생에게 있다고 가정하고 카운트
    for t in topping:
        right_count[t] = right_count.get(t, 0) + 1
    
    ways_to_split = 0  # 공평하게 자를 수 있는 방법의 수
    
    # 하나씩 왼쪽에 추가하고 오른쪽에서 제거하는 과정
    for t in topping:
        left_set.add(t)  # 철수가 가지는 토핑 종류 추가
        
        # 동생 쪽에서 해당 토핑을 하나 제거
        right_count[t] -= 1
        if right_count[t] == 0:
            del right_count[t]  # 동생에게 남아있지 않으면 제거
        
        # 철수와 동생의 토핑 종류 가짓수가 같으면 공평하게 나눌 수 있음
        if len(left_set) == len(right_count):
            ways_to_split += 1
    
    return ways_to_split
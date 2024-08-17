def solution(clothes):
    clothes_dict = {}
    
    # 1. 의상 종류별로 그룹화
    for name, type in clothes:
        if type in clothes_dict:
            clothes_dict[type].append(name)
        else:
            clothes_dict[type] = [name]
    
    # 2. 조합의 수 계산
    answer = 1
    for type in clothes_dict:
        # 각 종류별로 (해당 종류의 의상 수 + 1)만큼의 선택지가 있음
        answer *= (len(clothes_dict[type]) + 1)
    
    # 3. 아무것도 입지 않는 경우를 제외하고 반환
    return answer - 1
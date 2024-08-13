def solution(citations):
    # 논문 내림차순 정렬해서 인용 횟수가 많은 것부터 확인
    citations = sorted(citations, reverse=True)
    h_idx = 0
    
    for i in range(len(citations)):
        # 인용 횟수가 해당 논문의 순서보다 크거나 같은면 h_idx를 i+1 로 업데이트
        if citations[i] >= i + 1:
            h_idx = i + 1
        # 조건이 만족되지 않는 순간 for문을 탈출하고
        else:
            break
    
    # h-index 반환
    return h_idx

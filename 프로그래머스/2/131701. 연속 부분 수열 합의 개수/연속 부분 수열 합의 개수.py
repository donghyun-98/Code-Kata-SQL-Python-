def solution(elements):
    # 원형 수열 구현하기 위해 수열 두 번 붙이기
    circle_elements = elements + elements
    answer = []
    
    # 부분수열의 길이를 1 ~ n 까지 증가시키는 반복문
    for i in range(1, len(elements)+1):
        # 0부터 n-1 까지 돌면서 원형수열에서 부분수열의 합을 구해 answer에 추가하기
        for j in range(len(elements)):
            total = sum(circle_elements[j:j+i])
            answer.append(total)
    
    # 마지막에 중복을 제거하며 가능한 합의 개수를 반환
    return len(set(answer))
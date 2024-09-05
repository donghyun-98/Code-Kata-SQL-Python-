def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    # 자리별로 가능한 경우의 수 계산을 위한 리스트
    place_value = [781, 156, 31, 6, 1]  # 5자리 이하 단어들의 경우의 수 (5^4, 5^3, 5^2, 5^1, 5^0)
    
    # 각 자리별로 가능한 경우의 수를 계산하며 위치를 구하기
    answer = 0
    for i, char in enumerate(word):
        index = vowels.index(char)  # 현재 글자가 사전에서 몇 번째인지 찾고
        answer += index * place_value[i] + 1  # 현재 글자가 차지하는 단어 순서를 더하기
    
    return answer
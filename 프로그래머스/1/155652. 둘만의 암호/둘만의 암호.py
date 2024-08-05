def solution(s, skip, index):
    answer = ''
    
    for char in s:  # s의 각 문자에 대해
        cnt = 0
        while cnt < index:  # index 보다 작을 때
            char = chr(ord(char) + 1)
            if ord(char) > 122:
                char = 'a'
            if char not in skip:
                cnt += 1
        
        answer += char

    return answer
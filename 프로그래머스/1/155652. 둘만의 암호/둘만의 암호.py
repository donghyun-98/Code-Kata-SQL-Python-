def solution(s, skip, index):
    answer = ''
    
    for char in s:  # s의 각 문자에 대해
        cnt = 0
        while cnt < index:  # index 보다 작을 때
            char = chr(ord(char) + 1)  # 문자를 다음 문자로 바꾸고
            if ord(char) > 122:  # 만약 바꿨을 때 z의 아스키코드를 넘어버린다면
                char = 'a'  # a로 바꾸기.
            if char not in skip:  # skip 리스트에 없으면 횟수 늘리고
                cnt += 1  
        
        answer += char  # while 문을 다 돌았다면 변환 완료된 문자열을 answer에 추가.

    return answer
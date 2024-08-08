def solution(s):
    answer = []
    # 단어를 각각 분리해서 리스트로 저장
    words = s.split(' ')

    for word in words:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:
            answer.append(word)
    
    return ' '.join(answer)
        

    
print(solution("for  the last week"))

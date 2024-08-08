def solution(s):
    answer = []
    # 띄어쓰기가 한 칸 이상인 경우를 고려하여 공백을 기준으로 분리해서 리스트로 저장
    words = s.split(' ')

    # words의 각 요소들에 for문을 돌면서
    for word in words:
        if word:  # 단어가 비어있지 않다면 첫 단어를 대문자로 바꾼 후 뒤에 단어들은 소문자로 바꿔 answer에 추가
            answer.append(word[0].upper() + word[1:].lower())
        else:  # 단어가 비어있다면 그대로 answer에 추가
            answer.append(word)
    
    # 마지막으로 모든 단어들을 공백을 사이에 두고 다시 결합하여 return
    return ' '.join(answer)
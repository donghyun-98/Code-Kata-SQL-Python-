def solution(babbling):
    answer = 0
    for i in babbling:  # babbling 의 각 단어 i 에 대해 for 문
        for j in ['aya','ye','woo','ma']:  # 주어진 발음 리스트의 각 발음 j 에 대해
            if j*2 not in i:  # i 에 연속되는 발음이 없다면?
                i = i.replace(j,' ')  # i 에서 j 부분을 공백으로 replace 해서 해당 발음을 제거
        if len(i.strip())==0:  # 모든 발음을 제거한 후 i 에 남은 부분이 없다면?
            answer +=1
    return answer
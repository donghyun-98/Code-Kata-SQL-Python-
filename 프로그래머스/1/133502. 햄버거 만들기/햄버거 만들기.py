def solution(ingredient):
    answer = 0
    stack = []  # ingredient 를 순차적으로 담을 리스트

    for item in ingredient:  # 각각의 요소를 stack 에 추가하고
        stack.append(item)
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:  # 스택의 마지막 4개 요소가 1, 2, 3, 1 패턴과 일치하면
            answer += 1
            del stack[-4:]  # 마지막 4개 요소를 제거

    return answer

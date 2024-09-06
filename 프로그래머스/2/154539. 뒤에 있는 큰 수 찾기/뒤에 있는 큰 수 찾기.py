def solution(numbers):
    answer = [-1] * len(numbers)
    
    # 스택은 인덱스를 저장
    stack = []
    for i in range(len(numbers)):
        # 스택에 값이 있고, 현재 숫자가 스택에 있는 숫자보다 큰 동안 반복
        while stack and numbers[stack[-1]] < numbers[i]:
            # 스택에서 값을 꺼내서 그 위치의 뒷 큰수로 현재 숫자를 설정
            idx = stack.pop()
            answer[idx] = numbers[i]
        
        # 현재 인덱스를 다음 숫자들과 비교하기 위해 스택에 넣는다
        stack.append(i)
        
    return answer
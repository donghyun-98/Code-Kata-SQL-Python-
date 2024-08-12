def solution(s):
    # 문자열이 올바른 괄호 문자열인지 확인
    def is_valid_paren(paren_string):
        stack = []  
        matching = {')': '(', ']': '[', '}': '{'}  # 닫는 괄호에 대한 짝이 되는 여는 괄호를 매핑

        for char in paren_string:
            if char in matching.values():  # 여는 괄호라면 스택에 추가
                stack.append(char)
            elif char in matching.keys():  # 닫는 괄호라면 스택에서 마지막 여는 괄호와 짝을 맞추고
                if stack and stack[-1] == matching[char]:  # 짝이 맞으면 스택에서 제거
                    stack.pop()
                else:
                    return False  # 짝이 맞지 않으면 올바른 괄호 문자열이 아님
            else:
                return False  # 예상치 못한 문자가 있으면 올바른 괄호 문자열이 아님

        return len(stack) == 0  # 스택이 비어있으면 모든 괄호가 짝이 맞은 것

    count = 0  # 올바른 괄호 문자열이 되는 회전의 개수를 카운트
    n = len(s)  # 문자열 s의 길이
    
    for i in range(n):
        rotated_s = s[i:] + s[:i]  # 문자열 s를 왼쪽으로 i만큼 회전
        if is_valid_paren(rotated_s):  # 회전된 문자열이 올바른 괄호 문자열인지 확인
            count += 1  # 올바른 경우 카운트 증가
    
    return count  # 최종적으로 올바른 괄호 문자열이 되는 회전의 개수를 반환
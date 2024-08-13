def solution(elements):
    circle_elements = elements+elements
    answer = []
    
    for i in range(1, len(elements)+1):
        for j in range(len(circle_elements)):
            if i == len(elements):
                answer.append(sum(elements))
                break
            else:
                total = sum(circle_elements[j:j+i])
                answer.append(total)
    
    return len(set(answer))
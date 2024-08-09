def solution(brown, yellow):
    answer = []
    carpet_size = brown + yellow
    
    for y in range(3, brown+ 1):  # 세로
        for x in range(y, brown+1):  # 가로
            if x*y == carpet_size:
                if ((x-2)*(y-2) == yellow) and (x*y - (x-2)*(y-2) == brown):
                    answer.append(x)
                    answer.append(y)
            
    return answer
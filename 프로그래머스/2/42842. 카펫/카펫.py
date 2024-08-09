def solution(brown, yellow):
    answer = []
    carpet_size = brown + yellow
    
    for y in range(3, brown+ 1):  # 세로
        for x in range(y, brown+1):  # 가로
            # x 곱하기 y 가 카펫의 전체 면적과 같고
            if x*y == carpet_size:
                # yellow의 면적과 brown의 면적을 동시에 만족하는 x, y 조합이라면 answer에 추가
                if ((x-2)*(y-2) == yellow) and (x*y - (x-2)*(y-2) == brown):
                    answer.append(x)
                    answer.append(y)
            
    return answer
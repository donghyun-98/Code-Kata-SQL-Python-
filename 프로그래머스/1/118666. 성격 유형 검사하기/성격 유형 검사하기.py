def solution(survey, choices):
    answer = ''
    # 성격 유형 점수
    score_placement = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 1,
        6: 2,
        7: 3
    }
    # 성격 유형 지표
    metric = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }

    for i in range(len(survey)):
        first, second = survey[i][0], survey[i][1]
        
        if choices[i] < 4:
            metric[first] += score_placement[choices[i]]
        elif choices[i] > 4:
            metric[second] += score_placement[choices[i]]
    
    answer += 'R' if metric['R'] >= metric['T'] else 'T'
    answer += 'C' if metric['C'] >= metric['F'] else 'F'
    answer += 'J' if metric['J'] >= metric['M'] else 'M'
    answer += 'A' if metric['A'] >= metric['N'] else 'N'
    
    return answer
def solution(lottos, win_nums):
    ranking_table = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    answer = []
    count = 0
    
    for num in lottos:
        if num in win_nums:
            count += 1
    answer.append(ranking_table[count])
    
    count += lottos.count(0)
    answer.append(ranking_table[count])
        
    return sorted(answer)
def solution(lottos, win_nums):
    ranking_table = {  # 로또의 순위를 정하는 방식을 {맞춘 갯수: 순위} 형태로 딕셔너리로 만들어 놓는다.
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    answer = []  # 최고 순위, 최저 순위를 담을 리스트
    count = 0
    
    for num in lottos:  # lottos의 각 요소에 대해 
        if num in win_nums:  # win_nums에 있다면 count를 1 올린다(이 때 count는 최저순위)
            count += 1
    answer.append(ranking_table[count])  # 딕셔너리에서 key가 count인 것의 값을 answer에 추가
    
    count += lottos.count(0)  # lottos에서 0 의 갯수를 찾아 count에 더한다(이 때 count는 최고순위)
    answer.append(ranking_table[count])  # 딕셔너리에서 key가 count인 것의 값을 answer에 추가
        
    return sorted(answer)  # 마지막으로 최고순위, 최저순위로 정렬해서 return
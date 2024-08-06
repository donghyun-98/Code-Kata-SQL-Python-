def solution(players, callings):
    rank_dict = {}
    
    # 선수: 등수 형태로 딕셔너리에 저장
    for idx, val in enumerate(players):
        rank_dict[val] = idx    

    # callings 리스트를 돌면서 호명된 선수와 그 앞의 선수의 값과 위치를 바꿔준다.
    for name in callings:
        current_position = rank_dict[name]
        
        rank_dict[name] -= 1
        rank_dict[players[current_position-1]] += 1
        
        players[current_position-1], players[current_position] = players[current_position], players[current_position-1]
        
    return players
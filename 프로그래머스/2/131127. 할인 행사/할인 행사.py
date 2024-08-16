def solution(want, number, discount):
    answer = 0
    want_dict = {}
    # 정현이가 원하는 물품과 그 수량을 맵핑
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    # discount의 길이만큼 for 문을 돌면서 10일간의 구간을 확인 
    for i in range(len(discount)):
        discount_dict = {}  # 각 구간마다 물품과 그 수량을 임시로 저장할 딕셔너리
        if len(discount[i:i+10]) == 10:  # 현재 구간의 길이가 10인지 확인(아니라면 for문 탈출)
            for j in discount[i:i+10]:  # 10일간의 품목과 그 수량을 딕셔너리에 저장
                if j not in discount_dict:  
                    discount_dict[j] = 1
                else:
                    discount_dict[j] += 1
        else:
            break
        
        if want_dict == discount_dict:  # 정현이가 원하는 것과 할인 품목이 정확히 일치하면 answer 1 올리기
            answer += 1
            
    return answer
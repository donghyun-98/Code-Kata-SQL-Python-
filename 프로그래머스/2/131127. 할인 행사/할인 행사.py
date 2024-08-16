def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
        
    for i in range(len(discount)):
        discount_dict = {}
        if len(discount[i:i+10]) == 10:
            for j in discount[i:i+10]:
                if j not in discount_dict:
                    discount_dict[j] = 1
                else:
                    discount_dict[j] += 1
        else: 
            break
        
        if want_dict == discount_dict:
            answer += 1
            
    return answer
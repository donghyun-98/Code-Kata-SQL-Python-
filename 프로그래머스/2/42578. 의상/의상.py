def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    for name, type in clothes:
        if type in clothes_dict:
            clothes_dict[type].append(name)
        else:
            clothes_dict[type] = [name]
    
    for type in clothes_dict:
        answer *= (len(clothes_dict[type]) + 1)

    return answer - 1
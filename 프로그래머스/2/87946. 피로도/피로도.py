from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0
        
        for min_required_stamina, stamina_cost in p:
            if tmp >= min_required_stamina:
                tmp -= stamina_cost
                cnt += 1
        answer = max(answer, cnt)
    
    return answer
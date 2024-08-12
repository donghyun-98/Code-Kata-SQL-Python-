def solution(k, tangerine):
    tangerine_count = {}
    
    # 귤의 갯수를 세서 딕셔너리 형태로 저장하고
    for i in tangerine:
        if i not in tangerine_count:
            tangerine_count[i] = 1
        else:
            tangerine_count[i] += 1
            
    # 내림차순으로 정렬해 갯수가 많은 귤부터 담을 수 있도록 한다.
    sorted_count = sorted(tangerine_count.values(), reverse=True)
    
    # 최소한의 종류로 k 개를 채우기
    cnt = 0
    for i in sorted_count:
        k -= i
        cnt += 1 
        
        if k <= 0:
            break
    
    return cnt
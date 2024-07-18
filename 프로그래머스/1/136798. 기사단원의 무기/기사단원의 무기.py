def solution(number, limit, power):
    answer = 0
    factors_list = []  # 1~number 까지의 기사들의 약수 갯수를 담을 리스트
    
    for i in range(1, number+1):  # 1~number 까지 for 문을 돌며
        factors = []  # 각 기사단원의 약수의 갯수를 담을 리스트
        for j in range(1, int(i**0.5)+1):  # 1~i의 제곱근까지만 확인
            if i % j == 0:  # i를 j 로 나눠 0이 나오면 약수니까
                factors.append(j)  # 약수에 추가
                if i//j not in factors:  # 제곱이 되는 수 중복 방지
                    factors.append(i//j)
        factors_list.append(len(factors)) # 안에 있는 for 문을 다 돌았으면 factors_list에 추가

    for iron_weight in factors_list: 
        if iron_weight > limit:  # 각 기사단원의 약수의 갯수가 제한 공격력을 넘으면
            answer += power  # power를 답에 더하고
        else:
            answer += iron_weight  # 아니라면 약수의 갯수를 그대로 답에 더한다.       
    
    return answer
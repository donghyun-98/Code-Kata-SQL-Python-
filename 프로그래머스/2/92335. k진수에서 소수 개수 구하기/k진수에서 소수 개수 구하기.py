def solution(n, k):
    # 1번. n을 k진수로 변환
    answer = ''
    
    while n > 0:
        # n을 k로 나눈 몫과 나머지를 구해 나머지를 answer에 추가.
        n, r = divmod(n, k)
        answer += str(r)
    
    answer = answer[::-1]
    
    # 2번. 소수 후보 구하기
    answer = answer.split('0')
    
    # 3번. 후보가 소수인지 아닌지 판별하기
    count = 0
    for candidate in answer:
        if candidate == '':  # 후보가 빈 문자열이거나
            continue
        if int(candidate) < 2:  # 2보다 작은 정수라면 다음 후보로 넘어가기
            continue
        
        is_prime = True  # 소수인지 아닌지 판별할 플래그
        for i in range(2, int(int(candidate)**0.5)+1):  # 제곱근까지만 탐색해 시간 복잡도 줄이기
            if int(candidate) % i == 0:  # i 로 나눠진다면 소수가 아니니 플래그를 False로 바꾸고 break
                is_prime = False
                break
        if is_prime:  # 전부 다 돌았는데 나눠지는 수가 없다면 소수
            count += 1
        
        
    return count
def solution(nums):
    answer = 0

    for i in range(len(nums)):  # 조합할 첫 번째 수
        for j in range(i+1, len(nums)):  # 조합할 두 번째 수
            for k in range(j+1, len(nums)):  # 조합할 세 번째 수
                is_prime = nums[i] + nums[j] + nums[k]  # 소수인지 확인할 수
                prime = True  
                for factor in range(2, int(is_prime**0.5)+1):  # 2부터 자기자신 - 1 까지의 숫자를 돌면서
                    if is_prime % factor == 0:  # 약수로 자기자신이 나눠지면 소수가 아니다.
                        prime = False
                if prime:  # prime이 True면 정답을 1 올림
                    answer += 1
                    

    return answer
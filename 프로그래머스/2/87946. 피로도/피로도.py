from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    # 모든 던전 탐험 순서를 permutations 함수를 이용해 생성
    for p in permutations(dungeons, len(dungeons)):
        tmp = k  # 남은 피로도
        cnt = 0  # # 현재 탐험한 던전 수
        
        # 생성된 순열 p에 대해 던전을 하나씩 탐험
        for min_required_stamina, stamina_cost in p:
            # 현재 남은 피로도가 던전의 최소 필요 피로도보다 크거나 같다면 던전을 탐험할 수 있는 것
            if tmp >= min_required_stamina:
                tmp -= stamina_cost  # 던전 탐험 후 소모된 피로도만큼 남은 피로도를 감소
                cnt += 1  #  탐험한 던전 수 증가
        
        # 현재 순열에서 탐험한 던전 수와 지금까지 계산된 최대 던전 수를 비교해 더 큰 값을 저장
        answer = max(answer, cnt)
    
    return answer
def solution(arr1, arr2):
    # arr2의 열의 개수만큼 0으로 채운 리스트를 arr1의 행의 개수만큼 만들기
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for col in range(len(arr1)):  # arr1의 각 행
        for row in range(len(arr2[0])):  # arr2의 각 열
            for k in range(len(arr2)):  # 내적 구하기
                answer[col][row] += arr1[col][k] * arr2[k][row]

    
    return answer
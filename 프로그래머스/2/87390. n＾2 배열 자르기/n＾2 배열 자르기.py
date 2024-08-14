def solution(n, left, right):
    answer = []
    
    # left ~ right까지 반복문을 돌면서 
    for i in range(left, right+1):
        row, col = divmod(i, n)  # i 를 n 으로 나눈 몫과 나머지를 각각 행과 열 변수에 저장하고
        answer.append(max(row+1, col+1))  # 행과 열에 1 씩 더한 값중 더 큰 수를 answer에 저장 
    
    return answer
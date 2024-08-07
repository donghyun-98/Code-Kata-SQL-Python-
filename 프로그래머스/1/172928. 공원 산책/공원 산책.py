def solution(park, routes):
    answer = []
    op = {"N": [-1, 0], "S": [1, 0], "E": [0, 1], "W": [0, -1]}
    
    # 시작점 찾기
    max_width = len(park[0])
    max_height = len(park)
    for i in range(max_height):
        for j in range(max_width):
            if park[i][j] == 'S':
                x, y = i, j

    # 명령을 돌면서 
    for i in routes:
        dx, dy = op[i.split()[0]]  # 가야하는 x 좌표(수평)와 y 좌표(수직)를 각각 저장
        n = int(i.split()[1])  # 몇 번 가야하는지 저장
        nx, ny = x, y  # 만약 명령을 수행하지 못하는 경우 다시 이전의 상태로 돌아가기 위한 좌표
        can_move = True
        
        for _ in range(n):
            nx += dx
            ny += dy
            # 만약 아래의 조건에 해당하면 다시 이전의 상태로 복귀
            if (nx < 0 or nx >= max_height) or (ny < 0 or ny >= max_width) or (park[nx][ny] == 'X'):
                can_move = False
                break
            
        # 위의 조건들에 해당하지 않으면 x, y 업데이트
        if can_move:
            x, y = nx, ny
    
    return [x, y]
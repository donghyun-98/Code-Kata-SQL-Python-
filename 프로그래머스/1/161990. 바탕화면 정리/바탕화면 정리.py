def solution(wallpaper):
    x_list = []
    y_list = []
    
    # '#'이 나타나는 좌표를 찾아서 각각 x 와 y 리스트에 추가
    for i in range(len(wallpaper)):  
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                x_list.append(i)
                y_list.append(j)
    
    # 마지막으로 x, y 의 최솟값 | x, y 의 최대값 + 1 을 return
    return [min(x_list), min(y_list), max(x_list)+1, max(y_list)+1]
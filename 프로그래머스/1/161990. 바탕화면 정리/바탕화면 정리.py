def solution(wallpaper):
    x_list = []
    y_list = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                x_list.append(i)
                y_list.append(j)
    
    return [min(x_list), min(y_list), max(x_list)+1, max(y_list)+1]
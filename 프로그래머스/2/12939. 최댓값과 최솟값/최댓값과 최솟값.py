def solution(s):
    s = list(map(int, s.rsplit()))
    
    return f'{min(s)} {max(s)}'
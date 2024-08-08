def solution(s):
    transform_count = 0  # 변환 횟수
    zero_count = 0  # 변환 과정에서 제거되는 0의 갯수
    
    # s 가 '1'이 될 때까지 
    while s != '1':
        zero_count += s.count('0')  # '0'의 갯수를 세서 zero_count에 더하고
        s = s.replace('0', '')  # 모든 '0'을 제거한 후
        s = bin(len(s))[2:]  # 이진수의 형태로 변환하면 0b접두사와 함께 반환되기에 그 뒤의 문자열만 가져간다
        
        transform_count += 1  # while 문을 한 번 돌면 transform_count 1회 올리기
    
    return [transform_count, zero_count]
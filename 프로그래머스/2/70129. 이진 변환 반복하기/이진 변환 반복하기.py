def solution(s):
    transform_count = 0
    zero_count = 0
    
    while int(s) != 1:
        zero_count += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s))[2:])
        
        transform_count += 1
    
    return [transform_count, zero_count]
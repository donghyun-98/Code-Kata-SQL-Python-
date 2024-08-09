def gcd(a, b):
    # 최대공약수 구하기
    while b > 0:
        a, b = b, a%b
    
    return a


def lcm(a, b):
    # 최소공배수 구하기 - a*b를 최대공약수로 나누면 최소공배수
    return a*b / gcd(a, b)


def solution(arr):
    # 주어진 배열의 첫 번째 요소를 시작으로, 나머지 요소들과 순차적으로 최소공배수를 구하기
    answer = arr[0]
    for num in arr[1:]:
        answer = lcm(answer, num)
    return int(answer)
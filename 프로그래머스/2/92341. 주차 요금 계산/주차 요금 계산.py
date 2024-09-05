def solution(fees, records):
    parking_times = {}  # 입차 시간 기록
    total_times = {}  # 차량별 누적 주차 시간 기록
    
    # 1. records의 시간, 차량번호, 내역을 분리
    for record in records:
        time, car_num, status = record.split()
        
        # 시간은 다시 ':'를 기준으로 분리해서 분 단위로 저장
        h, m = map(int, time.split(':'))
        time = h * 60 + m
        
        # 2. 내역에 따라서 입/출차 관리
        if status == 'IN':  # 들어온 차량이면 딕셔너리에 '차량번호:시간' 형태로 저장
            parking_times[car_num] = time
        elif status == 'OUT':  
            in_time = parking_times.pop(car_num)  # 출차 시 입차 시각 제거 및 주차 시간 계산
            parked_time = time - in_time
            total_times[car_num] = total_times.get(car_num, 0) + parked_time
    
    # 출차 기록이 없다면 23:59에 출차한 것으로 처리    
    for car_num, in_time in parking_times.items():
        parked_time = (23 * 60 + 59) - in_time
        total_times[car_num] = total_times.get(car_num, 0) + parked_time
    
    # 3. 요금 계산
    total_times = dict(sorted(total_times.items()))  # 차량번호 순으로 정렬
    
    answer = []
    for car_num, time in total_times.items():
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            extra_time = time - fees[0]
            extra_fee = (extra_time + fees[2] - 1) // fees[2] * fees[3]
            answer.append(fees[1] + extra_fee)
    
    return answer
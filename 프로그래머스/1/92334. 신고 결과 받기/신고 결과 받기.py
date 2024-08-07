def solution(id_list, report, k):
    # 유저가 신고한 유저 리스트 딕셔너리, 각 유저가 신고당한 횟수를 저장하는 딕셔너리
    reported_id_dict = {user: [] for user in id_list}
    report_count = {user: 0 for user in id_list}
    
    # 신고정보를 처리
    for i in report:
        user_id, reported_id = i.split()
        if reported_id not in reported_id_dict[user_id]:
            reported_id_dict[user_id].append(reported_id)
            report_count[reported_id] += 1
    
    answer = [0] * len(id_list)
    banned_id = []
    for key, value in report_count.items():
        if value >= k:
            banned_id.append(key)
    
    for key, values in reported_id_dict.items():
        for val in values:
            if val in banned_id:
                answer[id_list.index(key)] += 1
    
    return answer
def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    
    # 오늘 날짜를 정수 형태로 변환해서 각각 y, m, d에 할당하고 일수로 바꾼다
    y, m, d = map(int, today.split('.'))
    today_to_day = y*12*28 + m*28 + d
    
    # 약관 종류를 딕셔너리 형태로 저장 
    for term in terms:
        terms_dict[term[0]] = int(term[2:])
    
    # 개인정보 리스트에서 날짜와 약관종류를 분리하고, 날짜를 일수로 변환한 하며 약관종류에 해당하는 일수를 더해준다
    for i in range(len(privacies)):
        agreement_date, terms_type = privacies[i].split()
        p_year, p_month, p_date = map(int, agreement_date.split('.'))
        agreement_date_to_day = p_year*12*28 + p_month*28 + p_date-1
        
        # 현재 날짜보다 작으면 파기해야하므로 answer에 추가
        if agreement_date_to_day + terms_dict[terms_type]*28 < today_to_day:
            answer.append(i+1)
        
    return answer
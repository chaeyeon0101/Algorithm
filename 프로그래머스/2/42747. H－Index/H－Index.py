def solution(citations):
    answer = 0
    
    h = 1
    while True:
        cnt = 0
        for i in citations:
            if i >= h:
                cnt = cnt + 1
        if h > cnt:
            answer = h - 1
            break
        else:
            h = h + 1
    
    return answer
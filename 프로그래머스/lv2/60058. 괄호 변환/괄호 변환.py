def solution(p):
    # 빈 문자열인 경우, 반환
    if not p:
        return ''
    
    # u, v로 문자열 분리
    l_cnt, r_cnt = 0, 0
    for i in p:
        if i == "(":
            l_cnt += 1
        else:
            r_cnt += 1
        if l_cnt == r_cnt:
            break
    u = p[:l_cnt + r_cnt]
    v = p[l_cnt + r_cnt:]
    
    # u가 올바른 괄호 문자열인지 판단
    stack = []
    for i in u:
        if i == "(":
            stack.append(1)
        else:
            if not stack:
                stack.append(-1)
                break
            else:
                stack.pop()
                
    # 처리
    if not stack:
        return u + solution(v)
    else:
        tmp = "("
        tmp += solution(v)
        tmp += ")"
        for i in range(1, len(u) - 1):
            if u[i] == "(":
                tmp += ")"
            else:
                tmp += "("
        return tmp
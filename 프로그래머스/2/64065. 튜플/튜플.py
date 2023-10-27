def solution(s):
    numCnt = [0] * 100001
    num = ''
    for i in s:
        if i >= '0' and i <= '9':
            num = num + i
            continue
        if num != '':
            numCnt[int(num)] = numCnt[int(num)] + 1
            num = ''
    answer = []
    check = numCnt.index(max(numCnt))
    while check != 0:
        answer.append(check)
        numCnt[check] = 0
        check = numCnt.index(max(numCnt))
    
    return answer
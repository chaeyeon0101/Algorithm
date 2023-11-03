def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9):
        s = set(discount[i : i + 10])
        tmp = discount[i : i + 10]
        for i in range(len(want)):
                if number[i] != tmp.count(want[i]):
                    break
                if i == len(want) - 1:
                    answer = answer + 1
    
    return answer
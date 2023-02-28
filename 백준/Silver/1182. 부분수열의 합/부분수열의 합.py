n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

def f(num, start, level, result):
    global answer
    if num == level:
        if result == s:
            answer += 1
        return
    
    for i in range(start, n):
        tmp_result = result
        tmp_result += arr[i]
        f(num, i + 1, level + 1, tmp_result)

for i in range(1, n + 1):
    f(i, 0, 0, 0)

print(answer)
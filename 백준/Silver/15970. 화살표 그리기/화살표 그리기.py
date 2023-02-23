import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x : (x[1], x[0]))
answer = arr[1][0] - arr[0][0]
if len(arr) < 3:
    exit()
answer += (arr[-1][0] - arr[-2][0])

for i in range(1, n - 1):
    if arr[i][1] == arr[i - 1][1] and arr[i][1] == arr[i + 1][1]:
        answer += min(arr[i][0] - arr[i - 1][0], arr[i + 1][0] - arr[i][0])
    elif arr[i][1] == arr[i - 1][1] and arr[i][1] != arr[i + 1][1]:
        answer += arr[i][0] - arr[i - 1][0]
    elif arr[i][1] != arr[i - 1][1] and arr[i][1] == arr[i + 1][1]:
        answer += arr[i + 1][0] - arr[i][0]

print(answer)
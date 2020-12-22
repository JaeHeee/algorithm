# BAEKJOON 회의실 배정

N = int(input())
meetings = []
answer = 0

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort()
meetings.sort(key=lambda x: x[1])

start_time = 0
for m in meetings:
    if m[0] >= start_time:
        start_time = m[1]
        answer += 1

print(answer)

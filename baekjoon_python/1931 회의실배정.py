N = int(input())
meeting = []
for i in range(N):
    start, end = map(int, input().split())
    meeting.append([start, end])
meeting.sort()
meeting.sort(key=lambda x: x[1])

meeting_count = 0
start_time = 0

for m in meeting:
    if m[0] >= start_time:
        start_time = m[1]
        meeting_count += 1

print(meeting_count)

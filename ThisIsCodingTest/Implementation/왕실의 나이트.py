# 행복 왕의 왕실 정원은 체스판과 같은 8x8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서있다. 나이트는 매우 충성스러운 신하로서 매일 무슬을 연마한다.
# 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
# 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
#    1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
#    2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동

# 이처럼 8x8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성해라. 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다.


# 입력 조건 : 첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다. 입력 문자는 a1 처럼 열과 행으로 이뤄진다.
# 출력 조건 : 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력해라.


# 문제 해결 아이디어
#    나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인한다. 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의한다.


input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps  [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

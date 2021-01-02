# 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 '*' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하라. 단, +보다 *를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정한다.
# 예를 들어 02984라는 문자열이 주어지면, 만들어질 수 있는 가장 큰수는 ((((0+2)*9)*8)*4) = 576 이다.
# 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어진다.

# 입력 조건 : 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어지낟. (1 <= S의 길이 <= 20)
# 출력 조건 : 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력한다.

# 문제 해결 아이디어 : 대부분의 경우 '+'보다는 'x'가 더 값을 크게 만든다.
#    - 예를 들어 5 + 6 = 11이고, 5 x 6 = 30이다.
# 다만 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기를 수행하는 것이 효율적이다.
# 따라서 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 두 수가 모두 2 이상인 경우에는 곱한다.


data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
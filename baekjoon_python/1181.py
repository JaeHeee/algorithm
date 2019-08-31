#word sort

N = int(input())
word_list = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for i in range(N):
    str = input()
    length = len(str)
    if str not in word_list[length-1]:
        word_list[length-1].append(str)

for i in range(50):
    if word_list[i] != []:
        word_list[i].sort()
        for word in word_list[i]:
            print(word)

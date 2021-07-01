answer = 0
n, m, k = list(map(int, input().split()))
num_list = list(map(int, input().split()))

num_list.sort()
max_num = num_list.pop()
next_max = num_list.pop()

for i in range(m):
    if (i+1) % (k+1) == 0:
        answer += next_max
    else:
        answer += max_num

print(answer)
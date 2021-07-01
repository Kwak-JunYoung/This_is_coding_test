n = int(input())
total_secs = 59 + 59 * 60 + n * 3600
count = 0

for i in range(total_secs):
    second = str(i % 60)
    i //= 60
    minute = str(i % 60)
    i //= 60
    hour = str(i % 60)

    if '3' in (hour + minute + second):
        count += 1

print(count)
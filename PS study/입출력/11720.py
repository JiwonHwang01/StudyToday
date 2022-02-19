count = int(input())
line = input();
sum = 0

num = list(line)
for i in range(0,count):
    sum += int(num[i])

print(sum)
import sys

read = sys.stdin.readline
sum, pos = 0, 0

count = int(read())
num_list = [0] * (count+1)

for i in range(count):
    num_list[i] = int(read())

num_list.sort()
print(num_list)
for i in range(count):
    if num_list[i] > 1000:
        print(sum)
        continue
    
    if num_list[i] < 0 :
        if num_list[i+1] < 1:
            sum += num_list[i] * num_list[i+1]
            num_list[i+1] = 10000
            print(num_list)
            print(sum)
            continue
        else:
            sum += num_list[i]
            print(sum)
            continue
    
    elif num_list[i] < 2 :
        sum += num_list[i]
        print(sum)
        continue    
    else:
        if ( count - i ) % 2 == 1 :
            sum += num_list[i]
            continue
        sum += num_list[i] * num_list[i+1]
        num_list[i+1] = 10000
        print(sum)
        print(num_list)


print(sum)
import sys
import math

f = math.factorial
read = sys.stdin.readline

case =int(read())
nums = [0] * case

for i in range(case):
    nums[i] = int(read())

for num in nums:
    res = 1
    count_1, count_2, count_3 = 0, 0, 0

    count_3 = num // 3
    count_2 = (num % 3) // 2
    count_1 = (num % 3) % 2

    while count_3:
        res += f(count_3 + count_2 + count_1)/(f(count_3)*f(count_2)*f(count_1))

        if count_2:
            count_2 -= 1
            count_1 += 2

        else :
            count_3 -= 1
            count_2 = (num - (3*count_3)) // 2
            count_1 = (num - (3*count_3)) % 2
    
    count_2 = num // 2
    count_1 = num % 2

    while count_2:
        res += f(count_2 + count_1)/(f(count_2)*f(count_1))
        
        if count_2:
            count_2 -= 1
            count_1 += 2

    print(int(res))
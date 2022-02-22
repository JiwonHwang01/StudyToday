import sys

read = sys.stdin.readline
count = int(read())
nums = []
sum = 0

def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    
    return a

for i in range(count):
    nums = list(map(int,read().split()))
    cnt = nums[0]
    nums = nums[1:]
    
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            sum += gcd(nums[i],nums[i+j+1])
    print(sum)
    sum = 0



    

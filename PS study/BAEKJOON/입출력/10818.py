import sys

a = sys.stdin.readline
count = int(a())
numbers = list(map(int,a().split()))
    
numbers.sort()
print("{} {}".format(numbers[0], numbers[count-1]))

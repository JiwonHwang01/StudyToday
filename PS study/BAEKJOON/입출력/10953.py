count = int(input())
i = 0
for i in range(0,count):
    num1, num2 = map(int, input().split(","))
    print(num1+num2)

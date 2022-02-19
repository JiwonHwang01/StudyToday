a = int(input())
def func1():
    if a<1 or a>10000:
        return
    sum = 0

    for i in range(1,a+1):
        sum += i

    print(sum)
func1()
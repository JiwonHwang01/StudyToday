def func1():
    a = int(input())
    if a<1 or a>9:
        return

    for i in range(1,10):
        print("{} * {} = {}".format(a,i,a*i))

func1()
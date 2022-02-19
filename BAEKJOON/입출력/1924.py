a = {
    1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 
    9 : 30, 10 : 31, 11 : 30, 12 : 31
}
b = {
    1 : "MON", 2 : "TUE", 3 : "WED", 4 : "THU", 5 : "FRI", 6 : "SAT", 0 : "SUN"
}
def func1():
    mon, day = map(int,input().split(" "))
    if mon<1 or mon>12 or day<1 or day>31:
        return
    sum = day

    for i in range(1, mon):
        sum += a[i]
    

    print(b[sum%7])
func1()
n = input()
count = 99

if int(n) <= 99:
        count = n

else:
    for i in range(100,int(n)+1):
        nums = list(map(int,list(str(i))))

        if nums[0] + nums[2] == 2* nums[1]:
            count += 1
    
print(count)





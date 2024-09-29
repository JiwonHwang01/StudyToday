def solution(expressions):
    answer = []
    s, e = 2, 9
    tmp = []
    maxnum = 1
    for exp in expressions:
        spl = exp.split()
        
        if spl[-1] == 'X':
            tmp.append(spl)
            for i in range(0,3,2):
                for j in range(len(spl[i])):
                    maxnum = max(maxnum,int(spl[i][j]))
            s = max(s,maxnum + 1)
            #print('maxcut1','s:',s,'e:',e)
            continue
        possi = []
        for i in range(0,5,2):
            for j in range(len(spl[i])):
                maxnum = max(maxnum,int(spl[i][j]))
        s = max(s,maxnum + 1)
        #print('maxcut','s:',s,'e:',e)
        if spl[1] == '+':

            for i in range(s,e+1):
                num1, num2, num3 = 0, 0, 0
                for j in range(len(spl[0])):
                    num1 += int(spl[0][len(spl[0])-j-1]) * (i**j)
                for j in range(len(spl[2])):
                    num2 += int(spl[2][len(spl[2])-j-1]) * (i**j)
                for j in range(len(spl[4])):
                    num3 += int(spl[4][len(spl[4])-j-1]) * (i**j)
                if num1 + num2 == num3:
                    possi.append(i)
            #print('plus poss', possi)
            s,e = min(possi), max(possi)
                    
                        
                    
        else:

            for i in range(s,e+1):
                num1, num2, num3 = 0, 0, 0
                for j in range(len(spl[0])):
                    num1 += int(spl[0][len(spl[0])-j-1]) * (i**j)
                for j in range(len(spl[2])):
                    num2 += int(spl[2][len(spl[2])-j-1]) * (i**j)
                for j in range(len(spl[4])):
                    num3 += int(spl[4][len(spl[4])-j-1]) * (i**j)
                if num1 - num2 == num3:
                    possi.append(i)
            #print('minus', possi)
            s,e = min(possi), max(possi)
        #print('s:',s,'e:',e)

    for res in tmp:
        ress = []
        for i in range(s,e+1):
            num1, num2, num3 = 0, 0, 0
            for j in range(len(res[0])):
                num1 += int(res[0][len(res[0])-j-1]) * (i**j)
            for j in range(len(res[2])):
                num2 += int(res[2][len(res[2])-j-1]) * (i**j)
            if res[1] == '+':
                num3 = num1 + num2
            else:
                num3 = num1 - num2
            remain = ""
            print(num1,num2,num3)
            while True:
                if num3 == 0:
                    break
                remain = str(num3 % i) + remain
                num3 //= i
            print(res, i, remain)
            if remain == "":
                remain ='0'
            ress.append(int(remain))
        print(ress)
        if min(ress)==max(ress):
            res[4] = str(min(ress))
        else:
            res[4] = '?'
        answer.append(" ".join(res))
                
    #print('tmp', tmp)
    
    return answer
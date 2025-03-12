# -> 숫자나 알파벳만 있는 경우는 절대 없다
k = 0
for i in range(3):
    buf = input()
    if buf == 'Fizz' or buf == 'Buzz' or buf == 'FizzBuzz':
        continue
    k = int(buf) + (3-i)

if k % 15 == 0:
    print('FizzBuzz')
elif k % 5 == 0:
    print('Buzz')
elif k % 3 == 0:
    print('Fizz')
else:
    print(k)

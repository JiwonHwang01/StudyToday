word = input()
count = []
for alpha in range (ord('a'),ord('z')+1):
    count.append(0)
for char in word:
    count[ord(char)-97] += 1
print(*count, sep = " ")
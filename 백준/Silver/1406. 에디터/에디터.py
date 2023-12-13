import sys

read = sys.stdin.readline

stack_a = list(read().strip())
stack_b = []
count = int(read())

for _ in range(count):
    command = list(read().split())

    if command[0] == "L" and stack_a:
        stack_b.append(stack_a.pop())
    elif command[0] == "D" and stack_b:
        stack_a.append(stack_b.pop())
    elif command[0] == "B" and stack_a:
        stack_a.pop()
    elif command[0] == "P":
        stack_a.append(command[1])

print("".join(stack_a + list(reversed(stack_b))))
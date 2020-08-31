n = input()
steps = 0
while len(n) > 1:
    step_sum = 0
    for i in n:
        step_sum += (ord(i) - ord('0'))
    steps += 1
    n = str(step_sum)
print(steps)


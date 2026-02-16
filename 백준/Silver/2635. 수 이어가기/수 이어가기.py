n = int(input())

max_len = 0
best_seq = []

for i in range(1, n + 1):
    temp_seq = [n, i]

    while True:
        next_val = temp_seq[-2] - temp_seq[-1]

        if next_val < 0:
            break

        temp_seq.append(next_val)

    if len(temp_seq) > max_len:
        max_len = len(temp_seq)
        best_seq = temp_seq

print(max_len)
print(*best_seq)
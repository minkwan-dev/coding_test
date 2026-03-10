N = int(input())

durations = list(map(int, input().split()))
durations.sort()

result = 0

for idx in range(len(durations)):
    result += (N - idx) * durations[idx]
    

print(result)
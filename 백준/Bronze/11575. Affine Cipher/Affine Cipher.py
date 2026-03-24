import sys

input = sys.stdin.readline

def solve():
    line = input().strip()
    if not line:
        return
    T = int(line)

    for _ in range(T):
        params = input().split()
        if not params: continue
        a, b = map(int, params)
        
        sentence = input().strip()
        if not sentence:
            sys.stdout.write('\n')
            continue
        
        memo = [chr(((a * x + b) % 26) + 65) for x in range(26)]
        
        result = "".join(memo[ord(char) - 65] for char in sentence)
        
        sys.stdout.write(result + '\n')

if __name__ == "__main__":
    solve()
ampere = int(input())

watt, volt = map(int, input().split())

if watt >= ampere * volt:
    print(1)
else:
    print(0)
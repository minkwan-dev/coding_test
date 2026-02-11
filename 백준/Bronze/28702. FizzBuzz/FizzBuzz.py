# 세 줄의 입력을 리스트에 담습니다.
strings = [input() for _ in range(3)]

for i in range(3):
    # 입력값이 숫자인 경우 (문자열이 Fizz, Buzz, FizzBuzz가 아닐 때)
    if strings[i].isdigit():
        # i가 0이면 +3, i가 1이면 +2, i가 2이면 +1을 하여 다음 숫자를 구합니다.
        next_num = int(strings[i]) + (3 - i)
        break

# 구한 다음 숫자에 FizzBuzz 규칙 적용
if next_num % 15 == 0:
    print("FizzBuzz")
elif next_num % 3 == 0:
    print("Fizz")
elif next_num % 5 == 0:
    print("Buzz")
else:
    print(next_num)
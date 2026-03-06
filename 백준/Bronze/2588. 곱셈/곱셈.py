num1 = int(input())
num2_str = input()  

for i in range(2, -1, -1):
    print(num1 * int(num2_str[i]))

print(num1 * int(num2_str))
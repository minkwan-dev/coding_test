n, k = map(int, input().split())

def factorial(n):
	if n <= 1:
		return 1
	return n*factorial(n-1)

top = factorial(n)
bottom_1 = factorial(k)
bottom_2 = factorial(n-k)

result =  top // (bottom_1*bottom_2)

print(result)
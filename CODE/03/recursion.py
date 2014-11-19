def factorial(n):
	if n<=1: 
		return 1
	
	return n * factorial(n - 1)


# print factorial (12)


def factorialWhile(x):

	if x==0:
		return 1

	res = x
	while(x > 1):
		x = x-1
		res=res * x
	return res





#print factorialWhile (4)
def countdown(n):
	if n == 0:
		print "Blasstoff!"
	elif n < 0:
		print "Invalid negative number"

	else:
		print n
		countdown (n-1)



countdown(-5)

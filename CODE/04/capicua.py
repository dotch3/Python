def calculate_capicua(my_string):
	is_capicua = True
	previous_char =None
	# size = len(my_string)
	# if size % 2 ==0:
	# 	print 'even'
	# else:
	# 	print 'not even'

	index = 0
	second_string =''

	for  ch in my_string:
		second_string = ch + second_string 
	return second_string == my_string # returns a true or a false value
	# while index < size / 2:
	# 	is_capicua = my_string[index] == my_string[-(index+1)]
	# 	if is_capicua is False:
	# 		break
	# 	index += 1	
	# return is_capicua


#calculate_capicua('holas')
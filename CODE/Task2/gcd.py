import math
# def calculate_gcd(a, b):

#     if a == 0 or b == 0:
#     	return 0

#     else :
#     	if a > b:
#        		 r = a%b
#         if r == 0:
#             return b
#         else:
#             return gcd(b, r)
#     if a < b:
#         a = b
#         b = a
#         return gcd(a, b)

def create_matrix(n):
	x = 1
	number_of_rows = n
	
	my_list_values =[]
	my_list_columns =[]
	if n == 0:
		
		return n
	else:
		for index in range (1, int (n ** 2 + 1)):
			#print 'entered FOR' , index_column, len(my_column)
			my_column = []
			my_list_values.append(index)
			while x <= n:
				new_value = index
			 	for index_second in range (0 , int(x)):
			 	 	my_column.append(new_value)
			 	 	print new_value , x , new_value + x
			 	 	new_value = new_value + 1 
				number_of_rows = number_of_rows + 1
				
				x = x +1

	print my_list_values
	x = x + 1
	#print my_list_values		
	
create_matrix(3)




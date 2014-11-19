def calculate_day(month, day, year):
	print 'Calculating the day for the date entered: ' + str(month)+  '/' + str(day) +  '/' + str(year)
	#print("Calculating new month value")
	if(month > 2):
		month = month - 2
		#print 'New Month:', month
	else:
		month = month + 10
		year = year - 1
		#print ('new month, year:',month, year)


	my_year = year%100
	my_century = year/100
	w = (13 * month - 1)/ 5
	x = my_year/4
	y = my_century/4
	z = w + x + y + day + my_year - 2 * my_century
	r= z%7
	#print r
	#print month,day,year,my_year,my_century
	#print w,x,y,z
	my_text= 'The day in the date entered was/will be on:  '
	if r == 0:
		print my_text + 'Sunday'
	elif r == 1:
		print my_text + 'Monday'
	elif r == 2:
	    	print my_text + 'Tuesday'
	elif r == 3:
	   	print my_text + 'Wednesday'
	elif r == 4:
	    	print my_text + 'Thursday'
	elif r == 5:
	    	print my_text + 'Friday'
	elif r == 6:
	    	print my_text + 'Saturday'

	return r



# Future/Near Date:
##calculate_day(10,28,2014)

#Birthday Date:
#calculate_day(5,14,2014)

if __name__ == '__main__':
	calculate_day(10,27,2014)

  
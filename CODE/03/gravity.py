import math 
def calculate_y_position (initial_y,initial_speed,time):
	return   (initial_y + initial_speed * time - (9.8/2) * (math.pow(time,2)))
	


def print_y_position(y0, v):
	y = y0
	time = 0
	while(y > 0):
		print time, "\t", y
		time = time + 0.01
		y = calculate_y_position(y0, v, time)
		if (y < 0):
			print "entered to the break"
			break
	else:
		print "end"


if __name__ == '__main__':
	print_y_position(2, 4)

#print calculate_y_position(1,2,0)
#print calculate_y_position(2,4,6)


def matrix_2(number_rows):

    for index in range(0, number_rows):
        my_res = []
        
        number_to_print = 1
        for index_column in range(0, number_rows):
            my_res.append(number_to_print)
            if (index_column < index):
                number_to_print = number_to_print +  1
            else:
                number_to_print = 0
        print (my_res)

matrix_2(3)
#matrix_2(4)


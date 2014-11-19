#!/usr/bin/env python

def first_matrix(n):
    for i in range(0, n):
        printable = ""
        print ('\n')
        value = 1
        for j in range(0, n):
            printable += str(value) + '\t'
            if (j < i):
                value += 1
            else:
                value = 0
        print (printable)

def second_matrix(n):
    last_row = n - 1
    column = 1
    constant = 2
    for i in range(0, n):
        p = ""
        print ('\n')
        column = column + i
        row = column
        incremental = 0
        for j in range(0, n):
            p = p + str(row) + '\t'
            if (j < last_row):
                incremental = j
            else:
                if(j == last_row):
                    incremental = incremental
                else:
                    incremental = incremental - 1
            row = row + constant + incremental
        print (p)
        if (i < (n - 2)):
            constant = constant + 1
        last_row = last_row - 1

if __name__ == '__main__':
    #first_matrix(5)
    second_matrix(4)
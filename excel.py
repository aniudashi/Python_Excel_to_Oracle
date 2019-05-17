#! /usr/bin/env python
#coding=utf-8
# -*- coding: utf-8 -*-
 
 
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#print "argv[0]=", sys.argv[0]
#for i in range(1, len(sys.argv)):
#    print "argv ", i, sys.argv[i]
 
def read_xls_file():
    data = xlrd.open_workbook(sys.argv[1])
    sheet0 = data.sheet_by_index(0)
    sys.stdout.write("create table ")
    sys.stdout.write(sheet0.name)
    sys.stdout.write("\n(\n")
    for rown in range(1,sheet0.nrows):
        sys.stdout.write("  ")
        sys.stdout.write(sheet0.cell_value(rown,0)),
        sys.stdout.write(" "),
        sys.stdout.write(sheet0.cell_value(rown,1)),
        sys.stdout.write(" ")
        sys.stdout.write(sheet0.cell_value(rown,3)),
        if(rown!=sheet0.nrows-1):
            sys.stdout.write(",\n")
        else:
            sys.stdout.write("\n")
    sys.stdout.write(");\n")

    for rown in range(1,sheet0.nrows):
        if(sheet0.cell_value(rown,4).strip()):
            sys.stdout.write("create index ")
            sys.stdout.write(sheet0.cell_value(rown,4))
            sys.stdout.write(" on ")
            sys.stdout.write( sheet0.name )
            sys.stdout.write(" (")
            sys.stdout.write(sheet0.cell_value(rown,0))
            sys.stdout.write(");\n")

    for rown in range(1,sheet0.nrows):
        if(sheet0.cell_value(rown,2).strip()):
            sys.stdout.write("comment on column ")
            sys.stdout.write( sheet0.name )
            sys.stdout.write( "." )
            sys.stdout.write( sheet0.cell_value(rown,0) )
            sys.stdout.write( " is '" )
            sys.stdout.write( sheet0.cell_value(rown,2))
            sys.stdout.write("';\n")
            

if __name__ == '__main__':
    read_xls_file()

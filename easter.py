#!/usr/bin/python
def main():
    
    n=year("Please Enter a year: ")
    na = n%19
    nb = n%4
    nc = n%7
    nd = ((19*na)+24)%30
    ne = ((2*nb)+(4*nc)+(6*nd)+5)%7
    easter = 22+nd+ne
    print "In The Year of the Lord",year,", Easter is on",
    if days <= 31:
        print"March " ,str(easter)
    else:
        print"April " , str(easter)
 
main()
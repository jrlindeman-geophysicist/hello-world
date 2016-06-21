#!/usr/bin/python
def listbound( first, last, space, seq, newlist ):
	print("Here is a list starting with %s, ending in %s, with spacing of %s.\nHere is the original list: %s \nand here is the new list from the first and last elements of the previous list: %s \n") % (first, last, space, seq, newlist)
	return;
first = int(raw_input("Please enter the first number of your list: "))
last = int(raw_input("Please enter the last number of your list: "))
space = int(raw_input("Please enter the spacing of your list: "))
seq = range(first,last+1,space)
length = len(seq)
newlist = [seq[0],seq[length-1]]
listbound(first,last,space,seq,newlist)

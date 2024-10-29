import argparse
import tkinter
from enum import Enum
if __name__=='__main__':
	parser=argparse.ArgumentParser(description="""
		Alternate in adding a course description and a colour
	""")
	parser.add_argument('file',)
	file=parser.parse_args().file
	hour=[]
	for i in range(2):
		if(i==0)
			h[i]=input("""
				enter earliest hour:
			""")
		else:
			h[i]=input("""
				enter latest hour:
			""")
	try:
		if int(h[i]) not in range(24):
			print("""
				not a hour
			""")
			quit()
	except ValueError:
		print("""
			wrong value
		""")
		quit()
	print("""
		enter the course description, press enter, enter the color, press enter. Now you can repeat everything for the next course. If you are ready, left the next line blank and press enter
	""")
	with open(file,'w')as r:
		d=input('course description')
		

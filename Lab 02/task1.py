from PIL import Image 
import os, sys


"""
Converting and Writing Image to .jpg
"""

for infile in sys.argv[1:]:
	f, e = os.path.splitext(infile)
	print(f,e)
	print(infile)
	outfile = f + ".jpg"
	if infile != outfile:
		try:
			Image.open(infile).save(outfile)
		except IOError:
	 		print("cannot convert", infile)
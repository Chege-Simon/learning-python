#! /usr/bin/python3

#Program that add bullet points to what is copies to the clipboard

import pyperclip,sys

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):	# loop through all indexes in the "lines" list
	lines[i] = '* ' + lines[i]	# add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)






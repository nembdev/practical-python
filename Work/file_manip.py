"""
Working with files
'r'     open for reading (default)
'w'     open for writing, truncating the file first
'x'     open for exclusive creation, failing if the file already exists
'a'     open for writing, appending to the end of the file if it exists
'b'     binary mode
't'     text mode (default)
'+'     open a disk file for updating (reading and writing)
'U'     universal newlines mode (deprecated)
https://docs.python.org/3/library/functions.html#open 
"""
"""
# opening, reading,writing, 1.0

f = open('test_file.txt', 'r')
contents = f.read()
print(contents)
f.close()

f = open('test_file2', 'w')
f.write('This file was written to')
f.close

f = open('test_file2', 'r')
contents = f.read()
f.close()
print(contents)
"""

# reading
with open('test_file.txt', 'r') as read_file:
	for line in read_file:
		print(line)
# writing
with open('test_file2.txt', 'w') as write_file:
	lines_to_write = 5
	for i in range(0, lines_to_write):
		write_file.write("This is line " + str(i) + "\n")

# print redirect
with open('test_file3.txt', 'w') as print_file:
	print("The print function wrote this", file=print_file)


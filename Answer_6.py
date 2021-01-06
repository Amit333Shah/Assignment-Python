'''6: Write a Python program to convert an array to an array of machine values and
return the bytes representation.
Expected Output:
Original array:
A1: array('i', [1, 2, 3, 4, 5, 6])
Array of bytes: b'010000000200000003000000040000000500000006000000'''

from array import*
A1= array('i', [1, 2, 3, 4, 5, 6])
print(A1.tobytes())

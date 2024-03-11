"""
A
BC
DEF
GHIJ
KLMNO  
...
"""
a=0
b=int(input())
for i in range(b+1):
	for j in range(i):
		a+=1
		print(i+j,end='\t')
	print()
width = 1
center = 25
for height in range(1, 21):
	 for space in range(center):
		  print('  ', end='')
	 for symbol in range(width):
		  print(' *', end='')
	 print()
	 if height % 5 == 0:
		  center += 2
		  width -= 4
	 else:
		  center -= 1
		  width += 2
	 height += 1

for symbol in range(5):
	 for space in range(center + 7):
		  print(' ', end='')
	 print("|#|")

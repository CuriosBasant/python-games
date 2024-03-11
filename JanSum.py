import random as r

"""while True:
	a=r.randint(r.randint(100,999), r.randint(1000,9999))
	b=r.randint(2,9)
	print('\nMultiply: %d X %d'%(a,b))
	while True:
		c=int(input())
		if c == a*b:
			print('Well Done, Janishi! Your answer is Correct.')
			break
		else:
			print('Oops! Try Again.')
	if input('Want to Play Again! ')=='n': break
"""
while True:
        c=0
        w=[]
        for i in range(10):
                a=r.randint(2,9)
                b=r.randint(2,9)
                print('\n%d.  %d X %d = '%(i+1, a, b), end='')
                ans=int(input())
                if ans==a*b: c=c+1
                else: w.append(i+1)

        print('\nYour score is : %d/10'%c)
        print('\nWrong Answers :', w)
        if input('Want to Play Again! ')=='n': break

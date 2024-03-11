# ab+c-de-*fg-h+/

postfix = 'ab+c-de-*fg-h+/'
stack = infix = ''

for i, ch in enumerate( postfix ) :
	if ch.isalpha() :
		infix += ch + ','
	else :
		infix = 

"""
# A + (B * C - (D / E ^ F) * G) * H
# A + B * C ^ D
# A+(B*C-(D/E^F)*G)*H
# A*(B+D)/E-F*(G+H/I)
infix = '(a+b-c)*(d-e)/(f-g+h)'
#infix = input("Enter an Infix Expression : ")
stack = postfix = ''
isPrefix = False

infix = '(' + infix.replace(' ', '') + ')'

if isPrefix :
	infix = infix[ : : -1]
	infix = infix.replace('(', '?').replace(')', '(').replace('?', ')')
	# print(infix)
	# infix = infix.replace(')', '(')
	# infix = infix.replace('?', ')')

precedence = { '(' : 0, '+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3 }

for i, ch in enumerate( infix ) :
	if ch.isalpha() :
		postfix += ch
	elif ch == ')' :
		postfix += stack[stack.rfind('(') + 1 : i][ : : -1]
		stack = stack[ : stack.rfind('(')]
	elif ch == '(' or precedence[ch] > precedence[stack[-1]] :
		stack += ch
	else :
		postfix += stack[-1]
		stack = stack[ : -1] + ch

if isPrefix :
	postfix = postfix[ : : -1]

print('The conversion of Infix Expression to Postfix Expression is : \n' + postfix + '\n')
"""
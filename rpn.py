#!/usr/bin/env python3
import readline
import operator
from clint.textui import colored
import sys
OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}


def calculate(arg):
	stack = list()
	op = ''
	for operand in arg.split():
	
		try:	
			operand = float(operand)
			stack.append(operand)

		except:
			arg2 = stack.pop()
			arg1 = stack.pop()

			operator_fn = OPERATORS[operand]
			op = operand
			result = operator_fn(arg1, arg2)

			stack.append(result)
			sys.stdout.write(colored.blue(arg1)+ ' ' + str(colored.blue(op)) + ' ' + colored.blue(arg2))
	return stack.pop()

def main():
	while True:
		result = calculate(input("rpn calc>"))
		print(colored.green(' = '+ str(result)))
def random_func():
	for i in range(20):
		print('hi')
#this has been called directly from the terminal (not from an impot
if __name__ == '__main__':
	main()

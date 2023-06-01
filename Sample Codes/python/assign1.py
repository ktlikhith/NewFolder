# Exchange the Values of Two Numbers Without Using a Temporary Variable
def swap_values(val1, val2):
	val2, val1 = val1, val2
	return (val1, val2)

#Check Whether a Number is Positive or Negative
def isPositive(num):
	return num >= 0

# Divisible numbers in the given range
def divisibleNumbers(start, end, num):
	out = []
	for ele in range(start, end+1):
		if ele % num == 0:
			out.append(ele)
	return out

def divNums(start, end, num):
	out = [ ele for ele in range(start, end+1) if ele % num == 0]
	return out

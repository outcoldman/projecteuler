# coding=utf8
#
# http://projecteuler.net/problem=4
#
# Largest palindrome product
#
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. 
# Find the largest palindrome made from the product of two 3-digit numbers.
#

def isPalindromic(n):
	nstr = str(n)

	for i in xrange(0, len(nstr) / 2):
		if nstr[i] != nstr[len(nstr) - 1 - i]:
			return False

	return True

def getPalindromic(maxN) :
	maxPalindromic = 0;

	for x in xrange(maxN, maxN / 10, -1):
		for y in xrange(maxN, x - 1, -1):
			n = x * y
			if isPalindromic(n):
				maxPalindromic = max(maxPalindromic, n)

	return maxPalindromic

print("For 2-digit number answer is " + str(getPalindromic(99)))
print("For 3-digit number answer is " + str(getPalindromic(999)))


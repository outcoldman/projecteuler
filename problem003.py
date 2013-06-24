# coding=utf8
#
# http://projecteuler.net/problem=3
#
# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#

def addIfNotIn(a, n):
	if (n not in a):
		a.append(n)

def addNewPrimes(primes, n):
	primeFactors = getPrimeFactors(n)

	if len(primeFactors) == 0:
		addIfNotIn(primes, n)
	else:
		for ip in primeFactors:
			addIfNotIn(primes, ip)


def getPrimeFactors(n):
	if (n == 0):
		return [1]

	if (n <= 3):
		return [n]

	primeFactors = []

	for i in xrange(2, (n + 1) / 2):
		if n % i == 0:
			d = n / i

			addNewPrimes(primeFactors, i)
			addNewPrimes(primeFactors, d)

			break

	if len(primeFactors) == 0:
		primeFactors.append(n)

	return primeFactors


print(max(getPrimeFactors(600851475143)))
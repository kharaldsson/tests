#basic function for finding the probability that a coin side with probability p will fall k times, over n flips
def coinflip(n, k, p):
	return (math.factorial(n)/(math.factorial(n - k) * math.factorial(k))) * (p ** k) * ((1 - p) ** (n - k))

#basic function for finding the probability that a coin side with probability p will fall k times, over n flips
def coinflip(n, k, p):
	return (math.factorial(n)/(math.factorial(n - k) * math.factorial(k))) * (p ** k) * ((1 - p) ** (n - k))


#basic function for chosing coin then flipping where Coin1 probability of Heads is p0
def coinsflip(p0,p1,p2):
    return (p0 * p1) + ((1-p0) * p2)

#Calculate the probability of a positive result--P(Positive)--given that
#p0=P(C)
#p1=P(Positive|C)
#p2=P(Negative|Not C)

def pos_result(p0,p1,p2):
    return (p0 * p1) + ((1 - p0) * (1 - p2))

#bayes law where:
#p0 = P(A) = Prior Probability (e.g. - Probability that you have cancer)
#p1 = P(B|A) = Specificity (e.g. - Probability a positive test for cancer if you have cancer) 
#p2 = P(Not B|Not A) = Sensitivity (e.g. - Probabilty of a negative test for cancer if you don't have cancer)
#Return the probability of A conditioned on B, or, P(A|B) (e.g. - Probability that you have cancer given a positive test)
def bayes1(p0,p1,p2):
	return (p0 * p1) / (p0 * p1 + (1 - p0) * (1 - p2))

print bayes1(0.1, 0.9, 0.8) 

#Return the probability of A conditioned on Not B given that 
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2 
def bayes2(p0,p1,p2):
	return (p0 * (1 - p1)) / (p0 * (1 - p1) + (1 - p0) * (p2))

print bayes2(0.1, 0.9, 0.8) 

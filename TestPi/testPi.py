import Gnuplot
import piRead
import math
from scipy.stats import chi2, norm, chisquare
from scipy.stats import f as f2
import numpy as np
pi = piRead.get_decimal()
should_LaTeX = False
should_plot = True

def chi2():
	print "\n"  + "Test du Chi2" +"\n"
	observed = np.array([99959, 99758, 100026, 100229, 100230, 100359, 99548, 99800, 99985, 100106])
	expected = np.array([.10, .10, .10, .10, .10, .10, .10, .10, .10, .10]) * np.sum(observed)
	result = chisquare(observed, expected)
	(kn, maxalpha) = result
	print kn #5.50908
	print maxalpha #0.7878
	
	
def gap_count(digit,gapLen):
	pi = piRead.get_decimal()
	counter = []
	max_gap = 1
	for i in range(gapLen):
		counter.append(0)

	in_digit = False

	gap_length = 1
	for i in pi:
		if(in_digit):
			if(i == str(digit)):
				gap_length = 1
				counter[gap_length-1] += 1
			else:
				gap_length +=1
				if(gap_length <= gapLen):
					counter[gap_length-1] += 1
				if(gap_length >max_gap):
					max_gap += 1

		else:
			if(i == str(digit)):
					in_digit = True
					counter[gap_length-1] += 1
	print "Digit ", digit," : max gap : ", max_gap
	return counter	
		

				
def gap(nb_class=60):
	print "\n" + "Test du Gap" +"\n"
	p_i = [] #avec nb de classe = longueur de chaine
	results = []
	l = 1
	for j in range(0, nb_class):
		value = 1/10.
		value = value * math.pow(9/10., l-1)
		l += 1
		p_i.append(value)
	print p_i
	for i in range(0, 10):
		counter = gap_count(i, nb_class)
		observed = np.array(counter)
		expected = np.array(p_i) * np.sum(observed)
		result = chisquare(observed, expected)
		(kn, maxalpha) = result
		print " ---   ---"
		print "-- Digit : ", i , " --"
#		print "Expected   Observed"
#		for j in range(len(counter)):
#			print p_i[j]*counter[0]*10,"  ",counter[j]
		print "Kn : ", kn, " Max alpha : ", maxalpha

def different_numbers(list):
	counters = [0,0,0,0,0,0,0,0,0,0]
	for elem in list:
		counters[int(elem)]+=1
	diff_elem=0
	for elem in counters:
		if elem >0:
			diff_elem +=1
	return diff_elem

def poker_theoritical_probability(sequence_length = 5, number_of_digits = 10):
	p_i = []
	for i in range(1, sequence_length+1):
		p = float(stirling_rec(sequence_length, i))
		stop = 0
		while(stop != -i):
			p = p*(number_of_digits+stop)
			stop = stop - 1
		p = p / (math.pow(float(number_of_digits), sequence_length))
		p_i.append(p)
	return p_i

stirling_rec_known = []

def stirling_rec(k, r):
	try:
		stirling_rec_known[k]
	except IndexError:
		for i in range(k-len(stirling_rec_known)+1):
			stirling_rec_known.append([])
	try:
		stirling_rec_known[k][r]
	except IndexError:
		for i in range(r-len(stirling_rec_known[k])+1):
			stirling_rec_known[k].append(None)

	if(k == r or r == 1):
		return 1
	else:
		if(stirling_rec_known[k][r] == None):
			stirling_rec_known[k][r] = stirling_rec(k-1, r-1) + r*stirling_rec(k-1, r)
		return stirling_rec_known[k][r]
	
def poker(k=5):
	print "\n" + " --- Test du poker ---" + "\n"
	hand = []
	counter = []
	for i in range(0,k):
		counter.append(0)
	for number in pi:
		hand.append(number)
		if len(hand)==k:
			diff_elem = different_numbers(hand)
			counter[diff_elem-1] +=1
			hand = []
	print "Resultat experimentaux", counter
	theory = poker_theoritical_probability()
	observed = np.array(counter)
	expected = np.array(theory) * np.sum(observed)
	result = chisquare(observed, expected)
	(kn, maxalpha) = result
	print kn #Dans la table des fractiles prendre 4 deg de liberte
	print maxalpha #
	for i in range(0,k):
		theory[i] = theory[i] *200000
	print "Resultat theorique", theory
def full_true(tab):
	for elem in tab:
		if elem == False:
			return False
	return True

def coupon_theoProb(length, d = 10):
	p_i = []
	for i in range(length):
		p_i.append(0.0)

	for r in range(10, length):
		p = float(math.factorial(d))/math.pow(d, r)
		p = p * stirling_rec(r-1, d-1)
		p_i[r] = p

	return p_i
	
def coupon(Max_coupon_size = 100):
	bool_tab = [False,False,False,False,False,False,False,False,False,False]
	len_coupon = 0
	counter = [] #0 a 9 devrait etre = 0 
	draw = 0
	for i in range(0,Max_coupon_size):
		counter.append(0)
	for decimal in pi:
		len_coupon +=1
		bool_tab[int(decimal)] = True
		if full_true(bool_tab):
			if len_coupon < Max_coupon_size-1:
				counter[len_coupon] +=1
			else:
				counter[Max_coupon_size-1] +=1
			len_coupon = 0
			bool_tab = [False,False,False,False,False,False,False,False,False,False]
			draw +=1
	print "draw : " , draw
	theory = coupon_theoProb(len(counter))
	print " i & experimental & theory \\\\"
	for i in range(0,Max_coupon_size):
		print i , " & ", counter[i], "  &  ", theory[i]*draw , "\\\\"

	observed = np.array(counter[10:99])
	expected = np.array(theory[10:99]) * draw
	result = chisquare(observed, expected)
	(kn, maxalpha) = result
	print "Kn :",kn 
	print "Alpha Max" ,maxalpha 

#chi2()
#gap()
#poker()
coupon()

from numpy import *

pi_file = open("pi6.txt", "r")
pi = ""

for line in pi_file:
	pi += line.rstrip('\n\r.') #retire les \n , \r et la virgule. on n'a que des nbrs

pi_decimals = pi[1:]

def get_decimal():
	return pi_decimals

def get_pi():
	return pi

def get_decimal_number(i):
	if(i< len(pi_decimals) ):
		return pi_decimals[i]
	else:
		return False
def getPiDecimalsBound(start, finish):
	return pi_decimals[start:finish+1]

def getNumberDecimalsOfPi():
	return len(pi_decimals)

print "Il y a " + str(getNumberDecimalsOfPi()) + " decimales de pi"
def count_digit_of_pi():
	zeros = 0
	un = 0
	deux = 0
	trois = 0
	quatre = 0
	cinq = 0
	six= 0
	sept = 0
	huit = 0
	neuf = 0
	for digit in pi_decimals:
		digit = int(digit)
		if digit == 1:
			un +=1
		elif digit == 2:
			deux +=1
		elif digit == 3:
			trois +=1
		elif digit == 4:
			quatre +=1
		elif digit ==5:
			cinq +=1
		elif digit ==6:
			six +=1
		elif digit ==7:
			sept +=1
		elif digit ==8:
			huit +=1
		elif digit ==9:
			neuf +=1
		else:
			zeros +=1
	real_repartition = [zeros,un,deux,trois,quatre,cinq,six,sept,huit,neuf]
	return real_repartition

real_repartition = count_digit_of_pi()
print real_repartition
index1 =  [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
index2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
theo_repartition = [100000, 100000, 100000, 100000, 100000,
						   100000, 100000, 100000, 100000, 100000]
for i in range(0,10):
	print str(i) +" & 100.000 &" + str(real_repartition[i]) +" & "+ str((100000.0/real_repartition[i] -1 )*100)
	
theo_fctrepart = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
for i in range(0,10):
	theo_fctrepart[i] = float(theo_fctrepart[i])/1000000
print theo_fctrepart
havetoplot = False
if havetoplot == True:
		import Gnuplot, Gnuplot.funcutils
		g = Gnuplot.Gnuplot()
		g.xlabel("Digits des decimales de pi")
		g.ylabel("Nombre d'occurrence")
		g.title("Histogramme des occurrences des decimales de pi")
		g('set yrange [0:130000]')
		g('set xtics ("0" 0, "" 1, "1" 2, "" 3, "2" 4, "" 5,"3" 6, "" 7, "4" 8, "" 9, "5" 10, "" 11, "6" 12, "" 13, "7" 14, "" 15, "8" 16, "" 17, "9" 18, "" 19)')
		g('set auto x')
		d = Gnuplot.Data(index1, real_repartition, with_='boxes lc rgb"red"', title='Resultats experimentaux')
		d2 = Gnuplot.Data(index1, theo_repartition, with_='boxes lc rgb"blue"', title='Resultats theoriques')
		g('set term pngcairo')
		g('set output "naive.png"')
		g.plot(d, d2)
		g('set yrange [99000:101000]')
		g('set term pngcairo')
		g('set output "naive2.png"')
		g.plot(d, d2)
		g('reset')
		g('set style histogram rowstacked gap 1 ')
		g('set style fill transparent solid 1 noborder')
		g.xlabel("Digits des decimales de pi")
		g.ylabel("Probabilite d'obtenir ce digit ou un digit inferieur")
		g.title("Fonction de repartition theorique des digits des decimales de pi")
		g('set yrange [0:1]')
		g('set xtics ("" 0, "0" 1, "1" 2, "2" 3, "3" 4, "4" 5, "5" 6, "6" 7, "7" 8, "8" 9, "9" 10, "" 11)')
		g('set auto x')
		d = Gnuplot.Data(range(1,11), theo_fctrepart, with_='boxes lc rgb"red"')
		g('set term pngcairo')
		g('set output "repartition.png"')
		g.plot(d)


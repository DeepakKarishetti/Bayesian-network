# Executable (bnet) file to compute and output
# the probability of any combination of events
# given any combination of events.

# Importing the implemented Bayesian Network class
from BayesianNetwork import BayesianNetwork
from sys import argv

given = False
observations = []
query = []

for _arg in argv:
        if _arg == "given":
                given = True
        query.append(_arg)
        if given:
                observations.append(_arg)

# Initializing class object
bnet = BayesianNetwork()

if query:
	x = bnet.check(bnet.get_values(query))
	if observations:
		y = bnet.check(bnet.get_values(observations))
	else:
		y = 1
	print "The probability is : %.9f" % (x/y)
else:
	print "Invalid query string"

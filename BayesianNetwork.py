'''
CSCI-404
Deepak Rajasekhar Karishetti
CSM
'''

# Bayesian network class:
class BayesianNetwork(object):
        def compute_probability(self, values):
                return  (self.get_defaults("B",values[0],None,None) * \
		self.get_defaults("E",values[1],None,None) * \
		self.get_defaults("A|B,E",values[2],values[0],values[1]) * \
		self.get_defaults("J|A",values[3],values[2],None) * \
		self.get_defaults("M|A",values[4],values[2],None))

	def get_defaults(self, check, prob_1, prob_2, prob_3):
		if check == "B":
			if prob_1:
				return 0.001
			else:
				return 0.999
		if check == "E":
			if prob_1:
				return 0.002
			else:
				return 0.998
		if check == "A|B,E":
			if prob_2 and prob_3:
				p_2 = 0.95
			if prob_2 and not prob_3:
				p_2 = 0.94
			if not prob_2 and prob_3:
				p_2 = 0.29
			if not prob_2 and not prob_3:
				p_2 = 0.001
			if prob_1:
				return p_2
			else:
				return (1-p_2)
		if check == "J|A":
			if prob_2:
				p_2 = 0.9
			else:
				p_2 = 0.05
			if prob_1:
				return p_2
			else:
				return (1-p_2)
		if check == "M|A":
			if prob_2:
				p_2 = 0.7
			else:
				p_2 = 0.01
			if prob_1:
				return p_2
			else:
				return (1-p_2)

	def check(self,values):
		if not None in values:
			return self.compute_probability(values)
		else:
			i = values.index(None)
			next_items = list(values)
			next_items[i] = True
			val_1 = self.check(next_items)
			next_items[i] = False
			val_2 = self.check(next_items)
			return val_1 + val_2

	def get_values(self,values):
		result = []
		if "Bt"	in values:
			result.append(True)
		elif "Bf" in values:
			result.append(False)
		else:
			result.append(None)
		if "Et"	in values:
			result.append(True)
		elif "Ef" in values:
			result.append(False)
		else:
			result.append(None)
		if "At"	in values:
			result.append(True)
		elif "Af" in values:
			result.append(False)
		else:
			result.append(None)
		if "Jt"	in values:
			result.append(True)
		elif "Jf" in values:
			result.append(False)
		else:
			result.append(None)
		if "Mt"	in values:
			result.append(True)
		elif "Mf" in values:
			result.append(False)
		else:
			result.append(None)
		return result

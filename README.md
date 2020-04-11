## Bayesian networks

**Name and CSM ID of the student**

	Name: Deepak Rajasekhar Karishetti
	CSM ID: 

**What programming language is being used**

	Python3

**How the code is structured**

	- The Bayesian Network class is structured in a seperate file and is imported in the bnet executable file to
	compute the probability of given events.
	- The probaility values from the table are hard-coded for each individual moves.
	- The class contains a function compute_probability that computes and returns the joint probability of the five events.
	- The probability for each condition is checked and their resulting probability is computed and returned based 
	on the given input.

**How to run the code**

	```To run the code on linux terminal:```
		- open a terminal at the file destination and type the following example implementation command:

		$ python bnet.py Bt Af Mf Jt Et

	```To run the code on Windows:```
		- Open a terminal at the file location and type the following example implementation:

		$ python bnet.py Bt Af Mf Jt Et 
		or
		$ bnet.py Bt Af Mf Jt Et

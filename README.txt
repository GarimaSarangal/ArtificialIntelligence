To load database on MAC: 
['filelocation/Question1.pl']. 
Do not put extra space between '' and filelocation

Question 1.2
Test Facts : 
 	edge(object, rel, category).

objects: louis, albert, frank
rel: isa, ako
category: creature, human, bird, man, turkey

Test Rules: 
	rel(louis, isa, What).
	rel(albert, isa, What).
	rel(frank, isa, What).
Corresponding answere for louis, albert and frank will appear.
example: louis is a man, louis is a human , louis is a creature


Question 1.4
Test Property Facts:
	property(object, propertytype, What).
object: human, bird, man, turkey, louis, albert, frank
propertytype: legs, fly

Test Property Rules: 
	hasProperty(frank, fly, no).
	hasProperty(albert, legs, two).
	hasProperty(louis, legs, one).






	








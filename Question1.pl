edge(human, ako, creature).
edge(bird, ako, creature).
edge(man, ako, human).
edge(turkey, ako, bird).
edge(louis, isa, man).
edge(albert, isa, man).
edge(frank, isa, turkey).

property(human, legs, two).
property(bird, fly, yes).
property(louis, legs, one).
property(turkey, fly, no).


rel(A, Reltype, B):- edge(A, Reltype, B).

rel(A, Reltype, B):- edge(A, Reltype, C), 
					 	rel(C, isa, B).
rel(A, Reltype, B):- edge(A, Reltype, C), 
						rel(C, ako, B).


hasProperty(A, Ppt, Val):- property(A, Ppt, Val).
hasProperty(A, Ppt, Val):- edge(A, isa, Z), hasProperty(Z, Ppt, Val), \+ property(A, Ppt, _). 
hasProperty(A, Ppt, Val):- edge(A, ako, Z), hasProperty(Z, Ppt, Val), \+ property(A, Ppt, _). 
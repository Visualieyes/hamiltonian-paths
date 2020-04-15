import pyquil
import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np


#data:graph, nodes, adjacencies, path

#quantum components: qubits, states, superposition, oracle, projector, groves search, measurement, wave function, collapse, interference, amplitude 



#Helper Function
#Returns Random Boolean Value
def randBool():
 bool_val = False
	val = random.randint(0,1)
	if val == 1:
	 bool_val = True
 return bool_val

#return random graph of 'N' vertices with at least degree 1, as a matrix in numpy.
def generateRandomGraph(N):
	G = nx.gnp_random_graph(random.randint(N, N+10), 1, seed=None, directed=randBool())
	matrix = nx.numpy_to_matrix(G)



#generate qubits for all possible states
def qubies(graph_g):
	



#Groves search or linear algebra on matrix
def quSolve():
	return None



def main():
	

	#connect to QVM
	
	#construct and inilialize graph
	
	#...function calls

	#measure and project the state of the qubit
	
	#display graph

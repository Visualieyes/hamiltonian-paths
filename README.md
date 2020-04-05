# Hamiltonian-search


#Problem:
 Represent a random graph with n vertices of at least degree one (n is at least 100). 
 This graph might be undirected or directed. It could have cycles or no cycles. 
 Randomly select two vertices (x,y) from the graph, and find all of the possible hamiltonian paths in the graph.
 

#Notes:
- Hamiltonian Path: a path which visits every vertex in a graph exactly once.
- A cycle could lead to infinite searches in the graph. Nodes visited must be stored.
- This problem is NP Complete
- Using Classical Computing algorithms this problem can, at best, be solved in polynomial time.
  Recursive algs will only scale to so many nodes until an iterable solution must be used. Worst-case, every node is redudantly interconnected and N! paths will be stord. Consider a graph of the human population where N is 7 billion. 
  Say we want to simulate the ways a virus could traverse through each person in the population individually. The number of different 'paths' would be 7billion! which is a very large number. As a result a quicker method should be used to solve the search problem.
- Quantum search algorithms could speed up the time of the search. 
- Depending on the goal of the search, it might not necessarily always be that more efficient, especially givent the learning curve for unversed and inexperienced developers. If we want to find all possible paths, they will nonetheless need to be stored. If quantum circuits can also optimize storage and memory access then the potential would surely supersede that of classical computing algorithms. More research is indeed needed, a 'path' I'm certainly interested in pursuing. 

#Implementation:
  1. 
  1. Use Depth-First Search (DFS) to traverse graph and check hamiltonian paths.
  2. Use Matrix-adjacency to iterate through paths.
  3. Use Grovers algorithm to quantum mechanically search for hamiltonian paths in the graph. 



#Libraries + Frameworks
- Networkx to construct a visual representation of the graph
- Random

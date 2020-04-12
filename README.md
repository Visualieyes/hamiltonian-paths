# Find Hamiltonian Paths


# Problem:
 Represent a random graph with n vertices of at least degree one (n is at least 100). 
 This graph might be undirected or directed. It could have cycles or no cycles. 
 Randomly select two vertices (x,y) from the graph, and find all of the possible hamiltonian paths in the graph.
 

# Solutions:
1. Recursive Depth First Search
2. Iterate Permutations
3. Groves Quantum Search

# Notes
- Hamiltonian Path: a path which visits every vertex in a graph exactly once.
- This problem is NP Complete/
- A cycle could lead to infinite searches in the graph. Nodes visited must be stored.
- Using Classical Computing algorithms this problem can, at best, be solved in polynomial time.
  Recursive algs will only scale to so many nodes until an iterable solution must be used. Worst-case, every node is redudantly interconnected and N! paths will be stored. * Example: Consider a graph of the human population where N is 7 billion. Say we want to simulate the ways a virus could traverse through each person in the population individually (not expontially). The number of different 'paths' would be 7billion! which is a very large number. Too large for a classical computer. As a result a quicker method is needed in order to solve the path finding problem. *
- Quantum search algorithms could speed up the time of the search. 
- *Important* Depending on the goal of the search, a quantum approach might not necessarily always be optimal, especially considering the learning curve for unversed and inexperienced developers. If we want to find all possible paths, then they will all need to be stored. The worst-case space complexity would still be (N-1)! *since we start from a given vertex*. A quantum search might provide a quick speed up to search and find a particular path, or any hamiltonian path. Moreoeover, if quantum circuits can optimize storage or memory access then the potential improvement of quantum algorithms would surely supersede that of classical computing algorithms. This research 'path' is certainly something I'm interested in pursuing. 

# Implementation
  1. Depth-First Search (DFS): Traverse graph and check hamiltonian paths. Since the problem is NP complete and specifies at least a 100 nodes, this is perfectly sufficient because at worst case you'll need to check every permutation anyways. TIncase a user does need to analyze more than 990
  2. Iterate Permutations: Instead of recursive calls which can lead to stackoverflow passed 990 nodes, store all levels and adjencies into a tree and then iteratively print all permutations of possible ham paths. This implmentation leverages the multiplication rule, since building a path is a step by step tree of potential node adjacencies. 
  3. Use Grovers algorithm to quantum mechanically search for hamiltonian paths in the graph. Theoretically, this solution promises to provide a quadratic speed up to that of a classical computing algorithm.  *NOTE* Due to quantum noise the optimization may be reduced.  



# Languages + Modules
- Python Programming Lanugage (3.7): Python is widely used, well supported, and extremely readable. When dealing with complex problems that involve multiple pieces to solve, a readable language will reduce the cognitive resources needed to focus on syntax and code and more on implementation and documentation. 
- Networkx: Objects and Methods for construction, initalizing, and accessing a random graph.
- MatPlotLib: Methods to display a visual representation of the graph.
- Pyquil: A well supported, open-source framework for quantum computing that allows you to leverage a QVM (quantum virtual machine) in order to run quantum code on a classical computer. It's recommended to pip install this moduke into a virtual environment.



# Sources
- https://awesomeopensource.com/project/rigetti/pyquil
- http://docs.rigetti.com/en/stable/start.html

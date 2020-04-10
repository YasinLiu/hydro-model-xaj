from platypus.algorithms import NSGAII
from platypus.core import Problem
from platypus.types import Real
import matplotlib.pyplot as plt
import seaborn 
import numpy as np 


seaborn.set()
 
# class allocation(Problem):
 
#     def __init__(self):
#         super(allocation, self).__init__(3, 3, 1)
#         self.types[:] = [Real(-10, 10), Real(-10, 10), Real(-10,10)]
#         self.constraints[:] = "<=0"
    
#     def evaluate(self, solution):
#         x = solution.variables[0]
#         y = solution.variables[1]
#         z = solution.variables[2]
#         solution.objectives[:] = [6*x/(1+x), 7*y/(1+1.5*y), 8*z/(1+0.5*z)]
#         solution.constraints[:] = [x+y+z-6]

# def schaffer(x):
#     return [x[0]**2, (x[0]-2)**2]
# schaffer_problem = Problem(1, 2)
# schaffer_problem.types[:] = Real(-10, 10)
# schaffer_problem.function = schaffer

class Belegundu(Problem):
    def __init__(self):
        super(Belegundu, self).__init__(2, 2, 2)
        self.types[:] = [Real(0, 5), Real(0, 3)]
        self.constraints[:] = "!=0"
    def evaluate(self, solution):
        x = solution.variables[0]
        y = solution.variables[1]
        solution.objectives[:] = [-2*x + y, 2*x + y]
        solution.constraints[:] = [-x + y - 1, x + y - 7]
    
algorithm = NSGAII(Belegundu())
# algorithm = NSGAII(schaffer_problem)
algorithm.run(10000)

for solution in algorithm.result:
    print(solution.objectives)
    
x = np.linspace(-50, 50, 1000)
p1 = plt.plot(x, -2*x+x)
# p2 = plt.plot(x, 2*x+x)
# p3 = plt.plot(x, x+1+x)
# p4 = plt.plot(x, 2*x+7)
plt.scatter([s.objectives[0] for s in algorithm.result],
            [s.objectives[1] for s in algorithm.result])
plt.legend()
plt.show()
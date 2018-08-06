def q2():
    from gurobipy import GRB, Model, quicksum
    import pandas as pd
    import numpy
 
    # You can either extract A,B,c from q1 if you want
    from q1 import q1
    A, b, c = q1()
 
    # Creation of the model
    m = Model('Dual')

    # Your code goes here
 
    # The following example is here to help you build the model (you must adapt it !!!) 
    # Define decision variables
    lamb = []
    for i in range(N):
        lamb.append(m.addVar(lb = 0, vtype=GRB.CONTINUOUS, name = 'lamb_{}'.format(i), obj = 1))
    m.update()

    # Define constraints:
    for i in range(len(x)):
        m.addConstr(y[i] - z[i] , "<=" , rhs=0)  
        m.update()
 
    # Define objective function:
    m.setObjective(objexpr, GRB.MINIMIZE)
 
    m.update()
 
    # z = optimal objective value (float)
    # lamb = coefficient for each covariate, starting with the covariates associated with the capacity constraints (list or numpy array)
    return([z, lamb])
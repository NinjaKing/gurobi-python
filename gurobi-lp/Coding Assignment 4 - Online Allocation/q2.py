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
    N = len(c)    
    
    # The following example is here to help you build the model (you must adapt it !!!) 
    # Define decision variables
    lamb = []
    for i in range(len(A)):
        lamb.append(m.addVar(lb = 0, vtype=GRB.CONTINUOUS, name = 'lamb_{}'.format(i), obj = 1))
    m.update()

    # Define constraints:
    for i in range(len(c)):
        lhs = LinExpr()
        for j in range(len(A)):
            expr.add(lamb[j], A[j][i])
        m.addConstr(lhs, ">=" , rhs=c[i])  
        m.update()
 
    # Define objective function:
    objexpr = LinExpr()
    for i in range(len(b)):
        objexpr.add(lamb[i], b[i])
    m.setObjective(objexpr, GRB.MINIMIZE)
    m.update()
    
    m.optimize()
 
    z = m.objVal
    lamb = [v.x for v in lamb[:4]]
    return ([z, lamb])
################ Open the data ###################################### 
def open_data(file = 'data.txt'):
    import numpy as np

    f = open(file, 'r')
    x = np.array([[0 for j in range(10)] for i in range(10000)])
    y = np.array([0 for i in range(10000)])

    # Loop over lines and extract variables of interest
    i = 0
    for line in f:
        columns = line.strip().split(',')
        y[i] = float(columns[0])
        for j in range(0,10):
            x[i, j] = float(columns[j+1])
        i += 1
            
    # x, y are numpy arrays 
    return(x, y)

################ Function to construct an LP Model ##################
def construct_lp_model(c, A, d):
    from gurobipy import Model, LinExpr, GRB

    # A = numpy.array (matrix)
    # c = numpy.array (vector)
    # d = numpy.array (vector)

    k, n = A.shape

    # Creation of the gurobi model
    m = Model("sp")

    # Variables 
    x = list()
    for i in range(n):
        x.append(m.addVar(lb = -GRB.INFINITY, ub = GRB.INFINITY, name = 'x_%d' % i))

    # Objective Function
    objExpr = LinExpr()
    for i in range(n):
        objExpr.add(x[i], c[i])
    m.setObjective(objExpr, GRB.MAXIMIZE)

    # Constraints 
    expr={}
    for j in range(k):
        expr = LinExpr()
        for i in range(n):
            expr.add(x[i], A[j, i])
        m.addConstr(expr, GRB.LESS_EQUAL, d[j])

    # Update the model to add new entries
    m.update()
    return m
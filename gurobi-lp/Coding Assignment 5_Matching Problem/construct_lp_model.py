def construct_lp_model(c, A, b, B, d):	
    from gurobipy import Model, LinExpr, GRB

    # A = numpy.array (matrix)
    # B = numpy.array (matrix)
    # c = numpy.array (vector)
    # d = numpy.array (vector)
    # b = numpy.array (vector)

    k, n = A.shape
    k2, n = B.shape
 
    # Creation of the gurobi model
    m = Model("sp")

    # Variables 
    x = list()
    for i in range(n):
        x.append(m.addVar(lb = 0, name = 'x_%d' % i))
 
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
        m.addConstr(expr, GRB.EQUAL, b[j])

    for j in range(k2):
        expr = LinExpr()
        for i in range(n):
            expr.add(x[i], B[j, i])
        m.addConstr(expr, GRB.LESS_EQUAL, d[j])
   
    # Update the model to add new entries
    m.update()
    return m
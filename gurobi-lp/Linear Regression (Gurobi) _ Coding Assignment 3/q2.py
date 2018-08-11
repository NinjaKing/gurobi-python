def q2():
    from gurobipy import Model, GRB, quicksum, LinExpr
    import numpy
    from functions import open_data

    # Creation of the model
    m = Model('LR')

    # Your code goes here
    x, y = open_data()
    N, n = len(x), len(x[0])

    # The following example is here to help you build the model (you must adapt it !!!) 
    # Define decision variables
    var = [] # w, b, z
    for i in range(n):
        var.append(m.addVar(lb = -GRB.INFINITY, vtype=GRB.CONTINUOUS, name = 'w_{}'.format(i), obj = 1))
    var.append(m.addVar(lb = -GRB.INFINITY, vtype=GRB.CONTINUOUS, name = 'b'.format(i), obj = 1))
    for i in range(N):
        var.append(m.addVar(lb = 0, vtype=GRB.CONTINUOUS, name = 'z_{}'.format(i), obj = 1))
    #m.update()

    # Constraints 
    expr={}
    for j in range(N):
        expr = LinExpr()
        for i in range(n):
            expr += -var[i]*x[j][i]
        expr += -var[n]
        expr += -var[n+1+j]
        m.addConstr(expr, GRB.LESS_EQUAL, -y[j])

        expr = LinExpr()
        for i in range(n):
            expr.add(var[i], x[j][i])
        expr += var[n]
        expr += -var[n+1+j]
        m.addConstr(expr, GRB.LESS_EQUAL, y[j])

    # Define objective function:
    obj=LinExpr()
    for i in range(N):
        obj += var[n+1+i]
    m.setObjective(obj, GRB.MINIMIZE)

    m.update()
    m.optimize()
    m.write('q2.lp')

    # Your code goes here

    #if m.status == GRB.Status.OPTIMAL:
    z = m.objVal
    b = var[n].x
    w = [v.x for v in var[:n]]
    
    #print([v.x for v in var[n+1:]])
    return ([z, b, w])

#if __name__ == '__main__':
#    q2()

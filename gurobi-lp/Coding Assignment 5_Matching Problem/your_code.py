def compute_optimal_allocation():
    from gurobipy import GRB, Model, quicksum, LinExpr
    import numpy
    from construct_lp_model import construct_lp_model
 
 
    cost = numpy.array([[17.8, 16.96, 13.56, 12.22, 15.88, 17.59], 
                        [13.11, 7.14,  8.57, 8.67,  7.23, 14.49],
                        [12.62, 9.1 ,  8.97, 7.75, 16.71, 16.59],
                        [12.87, 7.14,  9.75, 13.87, 13.59, 12.37],
                        [17.92, 14.5 , 14.91, 10.0 , 13.67, 12.56], 
                        [9.9 , 15.7 , 15.32, 16.8 , 17.34, 18.21]])
 
 
    # Your code goes here
    m = Model('matching')

    # Your code goes here
    n_jobs = cost.shape[0]
    n_servers = cost.shape[1]
    
    # The following example is here to help you build the model (you must adapt it !!!) 
    # Define decision variables
    x = []
    for i in range(n_jobs):
        x_i = []
        for j in range(n_servers):
            x_i.append(m.addVar(vtype=GRB.BINARY, name = 'var_{}_{}'.format(i, j)))
        x.append(x_i)

    # Define constraints:
    # each job only assigned to 1 server
    for i in range(n_jobs):
        lhs = LinExpr()
        for j in range(n_servers):
            lhs.add(x[i][j], 1)
        m.addConstr(lhs, GRB.EQUAL, rhs=1)  
    
    # each server can do at most 2 jobs
    for j in range(n_servers):
        lhs = LinExpr()
        for i in range(n_jobs):
            lhs.add(x[i][j], 1)
        m.addConstr(lhs, '<=', rhs=2)  
 
    # Define objective function:
    objexpr = LinExpr()
    for i in range(n_jobs):
        for j in range(n_servers):
            objexpr.add(x[i][j], cost[i, j])
    m.setObjective(objexpr, GRB.MINIMIZE)
    
    m.update()
    m.write('matching.lp')
    m.optimize()
 
    total_cost = m.objVal
    optimal_allocation = []
    for i in range(n_jobs):
        for j in range(n_servers):
            if x[i][j].x == 1:
                optimal_allocation.append((i + 1, j + 1))
    model = m

    # Your code goes here
 
    # optimal_cost = optimal total cost for the company
    # optimal_allocation = see instructions provided in the problem description on edX
    # model = gurobi model returned by the lp_standard_form function
    return ([total_cost, optimal_allocation, model])
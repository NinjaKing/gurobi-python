def compute_optimal_allocation():
    import gurobipy
    import numpy
    from construct_lp_model import construct_lp_model
 
 
    cost = numpy.array([[17.8, 16.96, 13.56, 12.22, 15.88, 17.59], 
                        [13.11, 7.14,  8.57, 8.67,  7.23, 14.49],
                        [12.62, 9.1 ,  8.97, 7.75, 16.71, 16.59],
                        [12.87, 7.14,  9.75, 13.87, 13.59, 12.37],
                        [17.92, 14.5 , 14.91, 10.0 , 13.67, 12.56], 
                        [9.9 , 15.7 , 15.32, 16.8 , 17.34, 18.21]])
 
 
    # Your code goes here

    model = construct_lp_model(c, A, b, B, d)
    model.optimize()

    # Your code goes here
 
 



 cost = np.array([[17.8, 16.96, 13.56, 12.22, 15.88, 17.59], 
                 [13.11, 7.14,  8.57, 8.67,  7.23, 14.49],
                 [12.62, 9.1 ,  8.97, 7.75, 16.71, 16.59],
                 [12.87, 7.14,  9.75, 13.87, 13.59, 12.37],
                 [17.92, 14.5 , 14.91, 10.0 , 13.67, 12.56], 
                 [9.9 , 15.7 , 15.32, 16.8 , 17.34, 18.21]])
 c = - cost.flatten()
 b = np.array([1 for _ in range(6)])
 d = np.array([2 for _ in range(6)])

 # Construction of the matrix A by blocks
 A = [[0 for _ in range(6 * i)] + [1 for _ in range(6)] + [0 for _ in range(6*(i+1), 6 * 6)] for i in range(6)]
 A = np.array(A)
 print(A, b, c, d)
 
 # optimal_cost = optimal total cost for the company
 # optimal_allocation = see instructions provided in the problem description on edX
 # model = gurobi model returned by the lp_standard_form function
 return([total_cost, optimal_allocation, model])
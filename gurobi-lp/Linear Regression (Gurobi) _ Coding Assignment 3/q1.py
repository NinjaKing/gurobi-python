def q1():
    import gurobipy
    import numpy
    from functions import construct_lp_model, open_data

    x, y = open_data()
    N, n = len(x), len(x[0])

    # Your code goes here
    
    nb_var = N + n + 1 + 1
    # c
    c = np.zeros(nb_var) # w, b, a_i, z
    c[-1] = 1

    # A
    A = np.zeros((3*N, nb_var))
    d = np.zeros(3*N)
    for i in range(N):
        # constraint 1
        A[i,:n] = -x[i]
        A[i,n] = -1
        A[i,n+1+i] = -1
        A[i,-1] = 0

        d[i] = -y[i]

        # constraint 2
        A[N+i,:n] = x[i]
        A[N+i,n] = 1
        A[N+i,n+1+i] = -1
        A[N+i,-1] = 0

        d[N+i] = y[i]

        # constraint 3
        A[2*N+i,:n+1] = 0
        A[2*N+i,n+1+i] = 1
        A[2*N+i,-1] = -1

        d[2*N+i] = 0
        
    # You can use either one of the following two approaches
    # Approach 1: construct matrices and vectors, and use the construct_lp_model function
    m = construct_lp_model(c, A, d)
    m.optimize()

    # Approach 2: create loops to create decision variables and constraints (see sample example in q2.py)


    var = m.getVars()
    
    z = m.objVal
    b = var[n].x
    w = [v.x for v in var[:n]]
    return([z, b, w])

if __name__ == '__main__':
    q1()

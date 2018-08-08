def q1():
    import pandas as pd
    data = pd.read_csv("data_online_allocation.csv")
    #Your code goes here
    
    m = 4
    N = 100
    b0, b1, b2, b3 = 125, 130, 118, 137

    #Construct A (has to be lists within a list)
    A = []
    for i in range(m):
        A.append(data.iloc[:, i].values.tolist())

    for i in range(N):
        A.append([0] * i + [1] + [0] * (N - i - 1))
    
    #Construct b (this will be the upper bound limit for your x1,..,x100
    b = [b0, b1, b2, b3]
    b.extend([1]*N)
    
    #Construct c (this goes into calculating the objective of the LP)
    c = data.iloc[:, 4].values.tolist()

    #Be careful, you have to return lists and not numpy arrays
    return ([A, b, c])
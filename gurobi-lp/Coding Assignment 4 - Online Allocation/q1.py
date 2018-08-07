def q1():
    import pandas as pd
    data = pd.read_csv("data_online_allocation.csv")
    #Your code goes here
    
    m = 4
    N = 100
    
    #Construct A (has to be lists within a list)
    A = []
    A.append([1, 0, 0, 0])
    A.append([0, 1, 0, 0])
    A.append([0, 0, 1, 0])
    A.append([0, 0, 0, 1])
    
    #Construct b (this will be the upper bound limit for your x1,..,x100
    
    
    #Construct c (this goes into calculating the objective of the LP)
 

    #Be careful, you have to return lists and not numpy arrays
    return ([A, b, c])
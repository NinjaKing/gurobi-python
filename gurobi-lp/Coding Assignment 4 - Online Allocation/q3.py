def q3():
    import pandas as pd
    from q2 import q2
    
    optimal = q2()
    lamda = optimal[1]
    
    data = pd.read_csv("new_data.csv")
    A = data.iloc[:, :].values
    
    reject_list = []
    for i in range(data.shape[0]):
        p = A[i, 4]
        for j in range(4):
            p -= lamda[j]*A[i, j]
        if p < 0:
            reject_list.append(i)
    
    return(reject_list)
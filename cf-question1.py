import numpy as np

stock = [[12, 23, 14],
     [10, 30, 15],
     [16, 22, 35],
     [14, 24, 20]]

stock = np.asarray(stock)

stock[1][1]

def floor_paint_eval(stock, A):
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    
    all_comb = np.zeros((3,3,3,3), dtype=int)
    
    #print(all_comb)
    
    while(p1 < 3):
        p2 = 0
        while(p2 < 3):
            p3 = 0
            while(p3 < 3):
                p4 = 0
                while(p4 < 3):
                    all_comb[p1,p2,p3,p4] = stock[0,p1] + stock[1,p2] + stock[2,p3] + stock[3,p4]
                    p4 = p4 + 1
                p3 = p3 + 1
            p2 = p2 + 1
        p1 = p1 + 1
            
    
    """
    print(np.where((all_comb > 100) == True, all_comb, np.zeros((3,3,3,3), dtype=int)))
    np.where((all_comb>=90))
    print(all_comb.shape)
    """
    
    output = (all_comb>=A).nonzero()
    
    total_usage = np.sum(np.where((all_comb >= A) == True, all_comb, np.zeros((3,3,3,3), dtype=int)))
    
    wastage = total_usage - A*len(output[0])
    
    final_output = []
    
    for i in range(len(output[0])): 
        final_output.append([(0,output[0][i]), (0,output[1][i]), (0,output[2][i]), (0,output[3][i])])
    
    return final_output, wastage

# Question 1 and 2
f_o, waste = floor_paint_eval(stock, 100)
print(f_o)
print(waste)

# Question 3
f_o, waste = floor_paint_eval(stock, 90)
print(f_o)
print(waste)

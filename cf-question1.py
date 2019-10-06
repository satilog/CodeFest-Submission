import numpy as np

stock = [[12, 23, 14],
     [10, 30, 15],
     [16, 22, 35],
     [14, 24, 20]]

stock = np.asarray(stock)

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
    
    output = (all_comb>=A).nonzero()
    #print(output)
    
    final_output = []
    
    min_usage_ind = 10e10
    for i in range(len(output[0])): 
        if all_comb[output[0][i], output[1][i], output[2][i], output[3][i]] < min_usage_ind:
            min_usage_ind = all_comb[output[0][i], output[1][i], output[2][i], output[3][i]]    
            final_output = [(0,output[0][i]), (0,output[1][i]), (0,output[2][i]), (0,output[3][i])]
    
    print(min_usage_ind)
    wastage = min_usage_ind - A
    
    return final_output, wastage, min_usage_ind

# Question 1 and 2
f_o, waste, usage = floor_paint_eval(stock, 100)
print(f_o)
print(waste)
print(usage)

# Question 3
f_o, waste, usage = floor_paint_eval(stock, 90)
print(f_o)
print(waste)
print(usage)

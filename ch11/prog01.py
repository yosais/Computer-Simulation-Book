def main():
    Num_Repl = 50    # Number of replications (repetitions)
    d = [] # Data set
    for i in range(Num_Repl):
        sim(state_var, out_var, param)
        a = list(map(lambda x,y: x-y, 
                        out_var['deps'], out_var['arrs']))
        d.append(stat.mean(a))
    
    # Estimate of performance measure
    print('Average Delay = ' , stat.mean(d))
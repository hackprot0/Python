def get_max_len(n, sticks, face=0):
    f = [[None]*n for k in range(1 << n)]
    
    out = 1
    
    for k in range(1 << n):
        for i in range(n):
            if (k & (1 << i)) != 0:
                if k & (k-1) == 0:
                    f[k][i] = [1, sticks[i][face]]
                else:
                    max_len = -1
                    max_len_end = None

                    for j in range(n):
                        if i != j and (k & (1 << j)) != 0:
                            p, q = f[k & ~(1 << i)][j]

                            if sticks[i][0] == q or sticks[i][1] == q:
                                if p+1 > max_len:
                                    max_len = p+1
                                    max_len_end = sticks[i][1] if sticks[i][0] == q else sticks[i][0]

                    f[k][i] = [max_len, max_len_end]
                    
                out = max(out, f[k][i][0])
                
    return out
                            
                            
def join_sticks(sticks):
    n = len(sticks)
    
    a = get_max_len(n, sticks, 0)
    b = get_max_len(n, sticks, 1)
    
    return max(a, b)

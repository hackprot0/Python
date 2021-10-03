def count_set_bits(n):
    count = 0
    
    while (n): 
        n &= (n-1)  
        count += 1
      
    return count 
            
def assignment(cost):
    f = [float("Inf")]*(1<<len(cost))
    f[0] = 0
    
    for k in range(1, 1<<len(cost)):
        i = count_set_bits(k)
        
        for j in range(len(cost)):
            if (k & 1 << j) != 0:
                f[k] = min(f[k], f[k & ~(1 << j)] + cost[i-1][j])
    
    return f[-1]
    
if __name__ == "__main__":
  print(assignment([[1, 5,], [2, -1]))

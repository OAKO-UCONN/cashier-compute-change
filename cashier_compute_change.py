def give_change(total, cost,d):
    
    c = total-cost
    sortedkeys=storted(d.keys(),reverse=True)
    print(sortedkeys)
    for i in sortedkeys:
        n = c//i
        c %= i
        d[i]=n
        
        print(d)
    return d


d = {10:0,20:0,5:0,1:0}
print(give_change(100, 55,d))
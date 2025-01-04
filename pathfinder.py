def pathfinder(m, n):
    if m==0 or n==0:
        return []
    if m==1 and n==1:
        return []
    ways = []
    if m==1 and n!=m:
        return ["D"*(n-1)]
    if n==1 and n!=m:
        return ["R"*(m-1)]
    if m>1:
        turnright=pathfinder(m-1,n)
        for i in turnright:
            ways.append("R"+i)
    if n>1:
        godown=pathfinder(m,n-1)
        for i in godown:
            ways.append("D"+i)
    return ways
    
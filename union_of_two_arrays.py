# gfg
# union of two arrays


def doUnion(self,a,n,b,m):
        
    u1 = set(a)
    u2 = set(b)
        
    u3 = u1.union(u2)
        
    return len(u3)
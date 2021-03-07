#13:05 18/01/20

def list_terms(F,list_t): return [F(i) for i in list_t]
def list_maker(F,init,end,N): return [F(i) for i in [init+(end-init)/(N-u) for u in range(N)]]

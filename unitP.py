

Dict ={}

def UnitPropagate(S):
    LetrasProposicionales = ['p','q','r','s']
    i=0
    if S==[]:
        return("satisfacible")
    while i<len(S):
        for i in range(0,len(S)):
            if S[i] == '':
                return("insatisfacible")
            else:
                i+=1
    for i in S:
        if i in LetrasProposicionales:
            Dict[i]='1'
            L=i
            S.remove(i)
            for l in S:
                for k in range(0,len(l)):
                    if l[k] ==i:
                        if l[k-1] =='-':
                            m =l[:k-1]+l[k+1:]
                            S.remove(l)
            S.append(m)
            return S,Dict
        else:
            continue


Clausula = ['s','pr','r-s']
print(UnitPropagate(Clausula))

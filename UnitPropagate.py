#Codigo UnitPropagate
#Input: S, conjunto de clausulas
#       I, interpretacion parcial
#Output: S, conjunto de clausulas
#       I, interpretacion parcial

def UnitPropagate(S,I):
    LetrasProposicionales = ['p','q','r','s']
    Dict ={}
    for i in [0,1, len(S)]:
        if S[i] == None:
            print("No se puede hacer unit propagate")

        elif S[i] == LetrasProposicionales[i]:
            S.pop(i)
            Dict[S[i]]='1'

    return Dict


Clausula = ['p','-qp','qr-s']
interpretacion = {}

UnitPropagate(Clausula, interpretacion)

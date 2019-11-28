# -*- coding: utf-8 -*-

# Subrutinas para la transformacion de una
# formula a su forma clausal

# Subrutina de Tseitin para encontrar la FNC de
# la formula en la pila
# Input: A (cadena) de la forma
#                   p=-q
#                   p=(qYr)
#                   p=(qOr)
#                   p=(q>r)
# Output: B (cadena), equivalente en FNC
def enFNC(A):
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256, 300)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB)))
    L = []
    Pila = [] # Inicializamos pila
    i = -1 # Inicializamos contador de variables nuevas
    s = A[0] # Inicializamos sımbolo de trabajo
    while (len(A) > 0):
        if s in letrasProposicionalesA and Pila[-1] =='-':
            i += 1
            atomo = LetrasProposicionalesB[i]
            Pila = Pila[:-1]
            Pila.append(atomo)
            L.append(atomo + '=' + '-' + s)
            A = A[0]
            if len(A) > 0:
                s = A[0]
        elif s == ')':
            w = Pila[-1]
            O = Pila[-2]
            v = Pila[-3]
            Pila = Pila[:len(Pila)-4]
            i += 1
            atomo = letrasProposicionalesB[i]
            L.append(atomo +"="+"(" + v + O + w + ")")
            s = atomo
        else:
            Pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]

    B = ""
    if i < 0:
        atomo = Pila[-1]
    else:
        atomo = letrasProposicionalesB[i]
    for x in L:
        y = enFNC(x)
        B += "Y" + y

    B = atomo + B
    return B

# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula
# Output: L (lista), lista de literales
def Clausula(C):
    L=[]
    while len(C) > 0:
        s = C[0]
        if s == 'O':
            C=C[1:]
        elif s == '-':
            literal = s+C[1]
            L.append(literal)
            C=C[2:]
        else:
            L.append(s)
            C=C[1:]
    return L

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC
# Output: L (lista), lista de listas de literales
def formaClausal(A):
    L=[]
    i=0
    while len(A)>0:
        if i >= len(A):
            L.append(Clausula(A))
            A=[]
        else:
            if A[i] == 'Y':
                L.append(Clausula(A[:i]))
                A=A[i+1:]
                i=0
            else:
                i+=1



    return L


def claUnitaria(U):
    point =False
    pos =-1
    for i in range (len(U)):
        if len(U[i]) == 0:
            return (True, False, pos)
        elif len(U[i]) == 1:
            point = True
            pos = i
            break
    return(False, point, pos)

def claUnit(S):
    for i in S:
        if(len(i) == 1):
            return True
    return False

def Compl(l):
    if l[0] == '-':
        return l.replace('-', '')
    else:
        return '-' + l

def removeCl(S, l):
    S.remove(l)
    if(len(l) >= 1):
        if(l[0] == '-'):
            L = l.replace('-', '')
        else:
            L = l[0]
        for i in S:
            if L in i:
                S.remove(i)
    return S

def removeCompl(S, l):
    if(len(l) >= 1):
        L = l[0]
        L = Compl(L)
        for i in S:
            if L in i:
                i.remove(L)
    return S

def unitPropagate(S, I):
    vacia, unitaria, posicion = claUnitaria(S)
    while(vacia == False and claUnit(S)):
        for i in S:
            S = removeCl(S, i)
            S = removeCompl(S, i)
            if(len(i) == 0):
                return 'Insatisfacible', I
            if(i[0] == '-'):
                I[Compl(i[0])] = 0
            else:
                I[i[0]] = 1
    return S, I

def lDicc(D):
    I = D.copy()
    for i in I:
        if(i[0] == '-'):
            I.pop(i)
            i = Compl(i)
            if(I.get(i) == 0):
                I[i[0]] = 1
            else:
                I[i[0]] = 0
    return I

def DPLL(S, I):
    S, I = unitPropagate(S, I)
    if(S == "Insatisfacible"):
        return 'Insatisfacible', "{}"
    if(len(S) == 0):
        return 'Satisfacible', lDicc(I)
    for i in S:
        if(len(i) == 0):
            return 'Insatisfacible', "{}"
    L = S[0]
    L = Compl(Compl(L[0]))
    Ip = I.copy()
    if(L[0] == '-'):
        Ip[Compl(L[0])] = 0
    else:
        Ip[L[0]] = 1

    Sp = S.copy()
    Sp.append(L[0])

    aux1, aux2 = DPLL(Sp, Ip)
    if(aux1 == 'Satisfacible'):
        return 'Satisfacible', lDicc(Ip)
    else:
        Spp = S.copy()
        Spp.append(Compl(L[0]))
        Ipp = I.copy()
        if(L[0] == '-'):
            Ipp[Compl(L[0])] = 1
        else:
            Ipp[L[0]] = 0
    return DPLL(Spp, Ipp)

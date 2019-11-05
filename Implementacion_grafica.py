print("importando paquetes")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib.figure import Figure

fig, ax = plt.subplots()

circle1 = plt.Circle((0.8, 0.89), 0.07, color='gainsboro')
circle2 = plt.Circle((0.8, 0.69), 0.07, color='gainsboro')
circle3 = plt.Circle((0.8, 0.49), 0.07, color='gainsboro')
circle4 = plt.Circle((0.8, 0.29), 0.07, color='gainsboro')
circle5 = plt.Circle((0.8, 0.09), 0.07, color='gainsboro')

circle6 = plt.Circle((0.63, 0.69), 0.07, color='gainsboro')
circle7 = plt.Circle((0.63, 0.49), 0.07, color='gainsboro')
circle8 = plt.Circle((0.63, 0.29), 0.07, color='gainsboro')
circle9 = plt.Circle((0.63, 0.09), 0.07, color='gainsboro')

circle10 = plt.Circle((0.46, 0.49), 0.07, color='gainsboro')
circle11 = plt.Circle((0.46, 0.29), 0.07, color='gainsboro')
circle12 = plt.Circle((0.46, 0.09), 0.07, color='gainsboro')

circle13 = plt.Circle((0.29, 0.29), 0.07, color='gainsboro')
circle14 = plt.Circle((0.29, 0.09), 0.07, color='gainsboro')

circle15 = plt.Circle((0.12, 0.09), 0.07, color='gainsboro')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

ax.add_artist(circle1)
label = ax.annotate("a", xy=(0.8, 0.86), fontsize=25, ha = "center")
ax.add_artist(circle2)
label = ax.annotate("b", xy=(0.8, 0.66), fontsize=25, ha = "center")
ax.add_artist(circle3)
label = ax.annotate("d", xy=(0.8, 0.46), fontsize=25, ha = "center")
ax.add_artist(circle4)
label = ax.annotate("g", xy=(0.8, 0.26), fontsize=25, ha = "center")
ax.add_artist(circle5)
label = ax.annotate("k", xy=(0.8, 0.06), fontsize=25, ha = "center")
ax.add_artist(circle6)
label = ax.annotate("c", xy=(0.63, 0.66), fontsize=25, ha = "center")
ax.add_artist(circle7)
label = ax.annotate("e", xy=(0.63, 0.46), fontsize=25, ha = "center")
ax.add_artist(circle8)
label = ax.annotate("h", xy=(0.63, 0.26), fontsize=25, ha = "center")
ax.add_artist(circle9)
label = ax.annotate("l", xy=(0.63, 0.06), fontsize=25, ha = "center")
ax.add_artist(circle10)
label = ax.annotate("f", xy=(0.46, 0.46), fontsize=25, ha = "center")
ax.add_artist(circle11)
label = ax.annotate("i", xy=(0.46, 0.26), fontsize=25, ha = "center")
ax.add_artist(circle12)
label = ax.annotate("m", xy=(0.46, 0.06), fontsize=25, ha = "center")
ax.add_artist(circle13)
label = ax.annotate("j", xy=(0.29, 0.26), fontsize=25, ha = "center")
ax.add_artist(circle14)
label = ax.annotate("n", xy=(0.29, 0.06), fontsize=25, ha = "center")
ax.add_artist(circle15)
label = ax.annotate("o", xy=(0.12, 0.06), fontsize=25, ha = "center")

#SITUACION INICIAL
#letras posicion
#numeros fichas

dict ={'a':0,'b':0,'c':0,'d':1,'e':1,'f':0,'g':1,'h':1,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0}

    #creacion de el ejemplo para la representacion grafica
a = dict.get('a')
b = dict.get('b')
c = dict.get('c')
d = dict.get('d')
e = dict.get('e')
f = dict.get('f')
g = dict.get('g')
h = dict.get('h')
i = dict.get('i')
j = dict.get('j')
k = dict.get('k')
l = dict.get('l')
m = dict.get('m')
n = dict.get('n')
o = dict.get('o')

#DIBUJA LA EL EJEMPLO QUE CONDICIONAMOS EN EL tablero
if a == 1:
    circlea = plt.Circle((0.8, 0.89), 0.07, color='k')
    ax.add_artist(circlea)
    label = ax.annotate("1", xy=(0.8, 0.86), fontsize=25, ha = "center",color='w')
if b == 1:
    circleb = plt.Circle((0.8, 0.69), 0.07, color='k')
    ax.add_artist(circleb)
    label = ax.annotate("2", xy=(0.8, 0.66), fontsize=25, ha = "center",color='w')
if d == 1:
    circled = plt.Circle((0.8, 0.49), 0.07, color='k')
    ax.add_artist(circled)
    label = ax.annotate("4", xy=(0.8, 0.46), fontsize=25, ha = "center",color='w')
if g == 1:
    circleg = plt.Circle((0.8, 0.29), 0.07, color='k')
    ax.add_artist(circleg)
    label = ax.annotate("7", xy=(0.8, 0.26), fontsize=25, ha = "center",color='w')
if k == 1:
    circlek = plt.Circle((0.8, 0.09), 0.07, color='k')
    ax.add_artist(circlek)
    label = ax.annotate("11", xy=(0.8, 0.06), fontsize=25, ha = "center",color='w')


if c == 1:
    circlec = plt.Circle((0.63, 0.69), 0.07, color='k')
    ax.add_artist(circlec)
    label = ax.annotate("3", xy=(0.63, 0.66), fontsize=25, ha = "center",color='w')
if e == 1:
    circlee = plt.Circle((0.63, 0.49), 0.07, color='k')
    ax.add_artist(circlee)
    label = ax.annotate("5", xy=(0.63, 0.46), fontsize=25, ha = "center",color='w')
if h == 1:
    circleh = plt.Circle((0.63, 0.29), 0.07, color='k')
    ax.add_artist(circleh)
    label = ax.annotate("8", xy=(0.63, 0.26), fontsize=25, ha = "center",color='w')
if l == 1:
    circlel = plt.Circle((0.63, 0.09), 0.07, color='k')
    ax.add_artist(circlel)
    label = ax.annotate("12", xy=(0.63, 0.06), fontsize=25, ha = "center",color='w')


if f == 1:
    circlef = plt.Circle((0.46, 0.49), 0.07, color='k')
    ax.add_artist(circlef)
    label = ax.annotate("6", xy=(0.46, 0.46), fontsize=25, ha = "center",color='w')
if i == 1:
    circlei = plt.Circle((0.46, 0.29), 0.07, color='k')
    ax.add_artist(circlei)
    label = ax.annotate("9", xy=(0.46, 0.26), fontsize=25, ha = "center",color='w')
if m == 1:
    circlem = plt.Circle((0.46, 0.09), 0.07, color='k')
    ax.add_artist(circlem)
    label = ax.annotate("13", xy=(0.46, 0.06), fontsize=25, ha = "center",color='w')


if j == 1:
    circlemj = plt.Circle((0.29, 0.29), 0.07, color='k')
    ax.add_artist(circlej)
    label = ax.annotate("10", xy=(0.29, 0.26), fontsize=25, ha = "center",color='w')
if n == 1:
    circlen = plt.Circle((0.29, 0.09), 0.07, color='k')
    ax.add_artist(circlen)
    label = ax.annotate("14", xy=(0.29, 0.06), fontsize=25, ha = "center",color='w')


if o == 1:
    circleo = plt.Circle((0.12, 0.09), 0.07, color='k')
    ax.add_artist(circleo)
    label = ax.annotate("15", xy=(0.12, 0.06), fontsize=25, ha = "center",color='w')

fig.savefig('Senku.png') #la parte grafica se guarda en una imagen llamada asi

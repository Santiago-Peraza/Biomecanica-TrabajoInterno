import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from energia_rot import energia_rot
import pickle as pk

file = 'totalWork.pkl'
#cargo archivo de datos
data = np.load(file)

#creo dataframe  con los promedios de trabajo por marcha
totalWork = data[['Nombre', 'Masa','Marcha','Velocidad','Paso', 'Trabajo']].groupby(['Nombre','Marcha']).mean()
#reindexo
totalWork.reset_index(inplace =True)

#declaracion de velocidad y filtro marcha w
velocidadW = [3.0,4.0,5.0,6.5]
filtroMarcha = totalWork.Marcha == 'w'

#creo dataframe vacio de marchas
marcha = pd.DataFrame(columns = ['Marcha','Velocidad', 'Promedio','Desv'])
#iteracion para calculo de promedio y desv estandar de velocidad W
for vel in velocidadW:
    filtroVelocidad = totalWork.Velocidad == vel
    #filtro datos necesarios para calculo de desv y prom
    marcha1 = totalWork.where(filtroVelocidad & filtroMarcha).dropna()
    #promedio por velocidad
    mean = marcha1.Trabajo.mean()
    #desv estandar por velocidad
    std = np.std(marcha1.Trabajo)
    #creo dataframe
    insert = pd.DataFrame(data=[('w',vel,mean,std)],columns= marcha.columns)
    #agrego fila de calculos
    marcha = marcha.append(insert,ignore_index=True)

#velocidades de marcha S
velocidadS = [5.0,6.5,9.0]
#filtro de marcha s
filtroMarcha = totalWork.Marcha == 's'
for vel in velocidadS:
    filtroVelocidad = totalWork.Velocidad == vel
    
    marcha1 = totalWork.where(filtroVelocidad & filtroMarcha).dropna()
    mean = marcha1.Trabajo.mean()
    std = np.std(marcha1.Trabajo)
    insert = pd.DataFrame(data=[('s',vel,mean,std)],columns= marcha.columns)
    marcha = marcha.append(insert,ignore_index=True)

#velocidad marcha R
velocidadR = [6.5,9.0,11.0]
#filtro marcha R
filtroMarcha = totalWork.Marcha == 'r'
for vel in velocidadR:
    filtroVelocidad = totalWork.Velocidad == vel
    
    marcha1 = totalWork.where(filtroVelocidad & filtroMarcha).dropna()
    mean = marcha1.Trabajo.mean()
    std = np.std(marcha1.Trabajo)
    insert = pd.DataFrame(data=[('r',vel,mean,std)],columns= marcha.columns)
    marcha = marcha.append(insert,ignore_index=True)

#defino tamaño figura
figsize = (10,6)
#gra#grafico marcha Sfico marcha S
plt.figure(figsize=figsize)
plt.title('Marcha S')
plt.errorbar(velocidadS,marcha.Promedio.where(marcha.Marcha == 's').dropna(),marcha.Desv.where(marcha.Marcha == 's').dropna(),linestyle = 'None',marker = '^', ecolor='g')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Trabajo')
plt.savefig('Trabajo_s.png')

#grafico marcha W
plt.figure(figsize=figsize)
plt.title('Marcha W')
plt.errorbar(velocidadW,marcha.Promedio.where(marcha.Marcha == 'w').dropna(),marcha.Desv.where(marcha.Marcha == 'w').dropna(),linestyle = 'None',marker = '^', ecolor='g')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Trabajo')
plt.savefig('Trabajo_w.png')

#grafico marcha R
plt.figure(figsize=(figsize))
plt.title('Marcha R')
plt.errorbar(velocidadR,marcha.Promedio.where(marcha.Marcha == 'r').dropna(),marcha.Desv.where(marcha.Marcha == 'r').dropna(),linestyle = 'None',marker = '^', ecolor='g')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Trabajo')
plt.savefig('Trabajo_R.png')


#grafico marchas conjuntas
plt.figure(figsize=(figsize))
plt.title('Marchas')
plt.errorbar(velocidadR,marcha.Promedio.where(marcha.Marcha == 'r').dropna(),marcha.Desv.where(marcha.Marcha == 'r').dropna(),linestyle = 'None',marker = '^', ecolor='g')
plt.errorbar(velocidadS,marcha.Promedio.where(marcha.Marcha == 's').dropna(),marcha.Desv.where(marcha.Marcha == 's').dropna(),linestyle = 'None',marker = '^', ecolor='r')
plt.errorbar(velocidadW,marcha.Promedio.where(marcha.Marcha == 'w').dropna(),marcha.Desv.where(marcha.Marcha == 'w').dropna(),linestyle = 'None',marker = '^', ecolor='b')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Trabajo')
plt.savefig('Trabajo_totaldemarchas.png')

plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from energia_rot import energia_rot
import pickle as pk

file = 'totalWork.pkl'
#cargo archivo de datos
data = np.load(file)


totalWork = data[['Nombre', 'Masa','Marcha','Velocidad','Paso', 'Trabajo']].groupby(['Nombre','Marcha']).mean()
totalWork.reset_index(inplace =True)


velocidadW = [3.0,4.0,5.0,6.5]

filtroMarcha = totalWork.Marcha == 'w'


marcha = pd.DataFrame(columns = ['Marcha','Velocidad', 'Promedio','Desv'])
for vel in velocidadW:
    filtroVelocidad = totalWork.Velocidad == vel
    
    marcha1 = totalWork.where(filtroVelocidad & filtroMarcha).dropna()
    mean = marcha1.Trabajo.mean()
    std = np.std(marcha1.Trabajo)
    insert = pd.DataFrame(data=[('w',vel,mean,std)],columns= marcha.columns)
    marcha = marcha.append(insert,ignore_index=True)


velocidadS = [5.0,6.5,9.0]
filtroMarcha = totalWork.Marcha == 's'
for vel in velocidadS:
    filtroVelocidad = totalWork.Velocidad == vel
    
    marcha1 = totalWork.where(filtroVelocidad & filtroMarcha).dropna()
    mean = marcha1.Trabajo.mean()
    std = np.std(marcha1.Trabajo)
    insert = pd.DataFrame(data=[('s',vel,mean,std)],columns= marcha.columns)
    marcha = marcha.append(insert,ignore_index=True)

velocidadR = [6.5,9.0,11.0]
filtroMarcha = totalWork.Marcha == 'r'
for vel in velocidadR:
    filtroVelocidad = totalWork.Velocidad == vel
    
    marcha1 = totalWork.where(filtroVelocidad & filtroMarcha).dropna()
    mean = marcha1.Trabajo.mean()
    std = np.std(marcha1.Trabajo)
    insert = pd.DataFrame(data=[('r',vel,mean,std)],columns= marcha.columns)
    marcha = marcha.append(insert,ignore_index=True)

figsize = (10,6)
plt.figure(figsize=figsize)
plt.title('Marcha S')
plt.errorbar(velocidadS,marcha.Promedio.where(marcha.Marcha == 's').dropna(),marcha.Desv.where(marcha.Marcha == 's').dropna(),linestyle = 'None',marker = '^', ecolor='g')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Trabajo')
plt.savefig('Trabajo_s.png')

plt.figure(figsize=figsize)
plt.title('Marcha W')
plt.errorbar(velocidadW,marcha.Promedio.where(marcha.Marcha == 'w').dropna(),marcha.Desv.where(marcha.Marcha == 'w').dropna(),linestyle = 'None',marker = '^', ecolor='g')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Trabajo')
plt.savefig('Trabajo_w.png')

plt.figure(figsize=(figsize))
plt.title('Marcha R')
plt.errorbar(velocidadR,marcha.Promedio.where(marcha.Marcha == 'r').dropna(),marcha.Desv.where(marcha.Marcha == 'r').dropna(),linestyle = 'None',marker = '^', ecolor='g')
plt.xlabel('Velocidad (km/h)')
plt.ylabel('Trabajo')
plt.savefig('Trabajo_R.png')
plt.show()

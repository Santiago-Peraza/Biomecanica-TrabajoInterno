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
# Biomecanica trabajo final


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig


file = 'data_proyecto_biomec2020.npy'
#cargo archivo de datos
data = np.load(file).item()


masa=data['MP_W_065']['info']['mass (kg)'][0]
# K: 
    # k_ua : brazo
    # k_fa :antebrazo
    # k_t : muslo
    # k_s : pierna
    # k_f :pie
    
k=pd.DataFrame(data = {'k_ua':[0.322],'k_fa':[0.303],'k_t':[0.323],'k_s':[0.302],'k_f':[0.475]})
# masas relativas: 
    #m_ua : brazo
    #m_fa :antebrazo
    # m_t : muslo
    # m_s : pierna
    # m_f :pie

m_s=pd.DataFrame(data={'m_ua':[masa*0.028],'m_fa':[masa*0.022],'m_t':[masa*0.100],'m_s':[masa*0.0465],'m_f':[masa*0.0145]})

# recorro los multiples registros de marchas (AUN NO FUNCIONA)
for reg in data:
    # Guardo informacion del registro
    info = pd.DataFrame(data['MP_W_065']['info'])
    
    # Defino dt y ventana de convolucion
    dt = 1/info['fs_kin (Hz)'].item()
    win = np.array([1/(2*dt),0,-1/(2*dt)])

    # for paso in reg['model_output_l']:
    paso = data['MP_W_065']['model_output_l'][0]

    # diccionario de centros de masa relativos al CM total 
    relativeCm = {
    'pierna_der_x': paso['cm_pierna_der_x'] - paso['cm_x'],
    'pierna_der_y': paso['cm_pierna_der_y'] - paso['cm_y'],
    'pierna_der_z': paso['cm_pierna_der_z'] - paso['cm_z'],
    
    'pierna_izq_x': paso['cm_pierna_izq_x'] - paso['cm_x'],
    'pierna_izq_y': paso['cm_pierna_izq_y'] - paso['cm_y'],
    'pierna_izq_z': paso['cm_pierna_izq_z'] - paso['cm_z'],

    'muslo_der_x': paso['cm_muslo_der_x'] - paso['cm_x'],
    'muslo_der_y': paso['cm_muslo_der_y'] - paso['cm_y'],
    'muslo_der_z': paso['cm_muslo_der_z'] - paso['cm_z'],

    'muslo_izq_x': paso['cm_muslo_izq_x'] - paso['cm_x'],
    'muslo_izq_y': paso['cm_muslo_izq_y'] - paso['cm_y'],
    'muslo_izq_z': paso['cm_muslo_izq_z'] - paso['cm_z'],
    
    'pie_der_x': paso['cm_pie_der_x'] - paso['cm_x'],
    'pie_der_y': paso['cm_pie_der_y'] - paso['cm_y'],
    'pie_der_z': paso['cm_pie_der_z'] - paso['cm_z'],

    'pie_izq_x': paso['cm_pie_izq_x'] - paso['cm_x'],
    'pie_izq_y': paso['cm_pie_izq_y'] - paso['cm_y'],
    'pie_izq_z': paso['cm_pie_izq_z'] - paso['cm_z'],

    'brazo_der_x': paso['cm_brazo_der_x'] - paso['cm_x'],
    'brazo_der_y': paso['cm_brazo_der_y'] - paso['cm_y'],
    'brazo_der_z': paso['cm_brazo_der_z'] - paso['cm_z'],

    'brazo_izq_x': paso['cm_brazo_izq_x'] - paso['cm_x'],
    'brazo_izq_y': paso['cm_brazo_izq_y'] - paso['cm_y'],
    'brazo_izq_z': paso['cm_brazo_izq_z'] - paso['cm_z'],

    'antbrazo_der_x': paso['cm_antbrazo_der_x'] - paso['cm_x'],
    'antbrazo_der_y': paso['cm_antbrazo_der_y'] - paso['cm_y'],
    'antbrazo_der_z': paso['cm_antbrazo_der_z'] - paso['cm_z'],

    'antbrazo_izq_x': paso['cm_antbrazo_izq_x'] - paso['cm_x'],
    'antbrazo_izq_y': paso['cm_antbrazo_izq_y'] - paso['cm_y'],
    'antbrazo_izq_z': paso['cm_antbrazo_izq_z'] - paso['cm_z'],

    'tronco_der_x': paso['cm_tronco_der_x'] - paso['cm_x'],
    'tronco_der_y': paso['cm_tronco_der_y'] - paso['cm_y'],
    'tronco_der_z': paso['cm_tronco_der_z'] - paso['cm_z'], 

    'tronco_izq_x': paso['cm_tronco_izq_x'] - paso['cm_x'],
    'tronco_izq_y': paso['cm_tronco_izq_y'] - paso['cm_y'],
    'tronco_izq_z': paso['cm_tronco_izq_z'] - paso['cm_z'], 

    'cm_x': paso['cm_x'],
    'cm_y': paso['cm_y'],
    'cm_z': paso['cm_z'],
    }
    
    #Creo dataframe de posiciones relativas 
    relativeCm = pd.DataFrame(data = relativeCm)
    #creo dataframe vacio para velocidades relativas
    relativeVelocity = pd.DataFrame()
    #realizo convolucion para crear dataframe de velocidades relativas
    relativeVelocity = relativeCm.transform(lambda x: sig.convolve(x,win,'same'))


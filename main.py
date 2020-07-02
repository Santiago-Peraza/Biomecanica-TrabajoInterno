# Biomecanica trabajo final


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file = 'data_proyecto_biomec2020.npy'
data = np.load(file).item()


for reg in data:
    info = pd.DataFrame(data['MP_W_065']['info'])
    # for paso in reg['model_output_l']:
    paso = data['MP_W_065']['model_output_l'][0]

    # centro de masa relativos
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
    relativeCm = pd.DataFrame(data = relativeCm)
# data['MP_W_065']['model_output_l'][0].keys() 
# Biomecanica trabajo final


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from energia_rot import energia_rot

file = 'data_proyecto_biomec2020.npy'
#cargo archivo de datos

data = np.load(file).item()
#declaro un dataframe vacio para el trabajo total
totalWork = pd.DataFrame(columns=['Nombre','Masa','Marcha', 'Velocidad', 'Paso', 'Trabajo'])

k=pd.DataFrame(data = {'k_ua':[0.322],'k_fa':[0.303],'k_t':[0.323],'k_s':[0.302],'k_f':[0.475]})
  # K:
            # k_ua : brazo
            # k_fa :antebrazo
            # k_t : muslo
            # k_s : pierna
            # k_f :pie
            



#recorro todos los registros de marcha
for reg in list(data.keys()):
    #evaluo si el registro de marcha tiene los resultados de cm de extremidades (hay registros que les falta)
    if 'cm_pierna_der_x' in data[reg]['model_output_l'][1]:
        # almaceno la masa del sujeto
        masa=data[reg]['info']['mass (kg)'][0]
        # masas relativas: 
            #m_ua : brazo
            #m_fa :antebrazo
            # m_t : muslo
            # m_s : pierna
            # m_f :pie

        
        m_s=pd.DataFrame(data={'m_ua':[masa*0.028],'m_fa':[masa*0.022],'m_t':[masa*0.100],'m_s':[masa*0.0465],'m_f':[masa*0.0145]})

        # recorro los multiples registros de marchas (AUN NO FUNCIONA)
        # for reg in data:
        # Guardo informacion del registro
        info = pd.DataFrame(data[reg]['info'])
        print(info)
        # Defino dt y ventana de convolucion
        dt = 1/info['fs_kin (Hz)'].item()
        win = np.array([1/(2*dt),0,-1/(2*dt)])

        

        for i in range(0,15):
            # guardo un paso 
            paso = data[reg]['model_output_l'][i]
            # guardo el total de marcadores
            marcadores =data[reg]['kinematic_l']

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
            relativeCm = relativeCm/1000
            #creo dataframe vacio para velocidades relativas
            relativeVelocity = pd.DataFrame()
            #realizo convolucion para crear dataframe de velocidades relativas
            relativeVelocity = relativeCm.transform(lambda x: sig.convolve(x,win,'same'))
            relativeVelocity.iloc[0] = relativeVelocity.iloc[1]
            relativeVelocity.iloc[-1] = relativeVelocity.iloc[-2]
            #creo dataframe de energia cinetica lineal
            linealKinetic= pd.DataFrame(columns=['brazo_der', 'brazo_izq', 'antebrazo_der','antebrazo_izq', 'muslo_der','muslo_izq','pierna_der','pierna_izq', 'pie_der','pie_izq'])
            #obtengo energiaC de brazo
            linealKinetic['brazo_der'] = ((relativeVelocity[['brazo_der_x', 'brazo_der_y', 'brazo_der_z']]**2 * m_s.m_ua.item())/2).sum(axis =1)
            linealKinetic['brazo_izq'] = ((relativeVelocity[['brazo_izq_x', 'brazo_izq_y', 'brazo_izq_z']]**2 * m_s.m_ua.item())/2).sum(axis =1)
            #obtengo energiaC de antebrazo
            linealKinetic['antebrazo_der'] = ((relativeVelocity[['antbrazo_der_x', 'antbrazo_der_y', 'antbrazo_der_z']]**2 * m_s.m_fa.item())/2).sum(axis =1)
            linealKinetic['antebrazo_izq'] = ((relativeVelocity[['antbrazo_izq_x', 'antbrazo_izq_y', 'antbrazo_izq_z']]**2 * m_s.m_fa.item())/2).sum(axis =1)
            #obtengo energiaC de muslo
            linealKinetic['muslo_der'] = ((relativeVelocity[['muslo_der_x', 'muslo_der_y', 'muslo_der_z']]**2 * m_s.m_t.item())/2).sum(axis =1)
            linealKinetic['muslo_izq'] = ((relativeVelocity[['muslo_izq_x', 'muslo_izq_y', 'muslo_izq_z']]**2 * m_s.m_t.item())/2).sum(axis =1)
            #obtengo energiaC de pierna
            linealKinetic['pierna_der'] = ((relativeVelocity[['pierna_der_x', 'pierna_der_y', 'pierna_der_z']]**2 * m_s.m_s.item())/2).sum(axis =1)
            linealKinetic['pierna_izq'] = ((relativeVelocity[['pierna_izq_x', 'pierna_izq_y', 'pierna_izq_z']]**2 * m_s.m_s.item())/2).sum(axis =1)
            #obtengo energiaC de pie
            linealKinetic['pie_der'] = ((relativeVelocity[['pie_der_x', 'pie_der_y', 'pie_der_z']]**2 * m_s.m_f.item())/2).sum(axis =1)
            linealKinetic['pie_izq'] = ((relativeVelocity[['pie_izq_x', 'pie_izq_y', 'pie_izq_z']]**2 * m_s.m_f.item())/2).sum(axis =1)

            #reseté indice de dataframe
            linealKinetic.reset_index(inplace = True)
            #externo a for de pasos
            e_rot = energia_rot(marcadores, info['mass (kg)'].item(), 0)
            #reseté indice de dataframe
            e_rot.reset_index(inplace = True)


            # se crea dataframe de energia de segmentos
            energiaTotalSegmento = pd.DataFrame(columns=list(linealKinetic.columns))
            energiaTotalSegmento['brazo_der'] =  linealKinetic['brazo_der']+ e_rot['E_b_r']
            energiaTotalSegmento['antebrazo_der'] =  linealKinetic['antebrazo_der']+ e_rot['E_a_r']
            energiaTotalSegmento['muslo_der'] =  linealKinetic['muslo_der']+ e_rot['E_g_r']
            energiaTotalSegmento['pierna_der'] =  linealKinetic['pierna_der']+ e_rot['E_p_r']
            energiaTotalSegmento['pie_der'] =  linealKinetic['pie_der']+ e_rot['E_pie_r']

            energiaTotalSegmento['brazo_izq'] =  linealKinetic['brazo_izq']+ e_rot['E_b_l']
            energiaTotalSegmento['antebrazo_izq'] =  linealKinetic['antebrazo_izq']+ e_rot['E_a_l']
            energiaTotalSegmento['muslo_izq'] =  linealKinetic['muslo_izq']+ e_rot['E_g_l']
            energiaTotalSegmento['pierna_izq'] =  linealKinetic['pierna_izq']+ e_rot['E_p_l']
            energiaTotalSegmento['pie_izq'] =  linealKinetic['pie_izq']+ e_rot['E_pie_l']


            #dataframe de energias totales por miembrp
            energia =pd.DataFrame()

            energia['superior_derecho'] = energiaTotalSegmento['brazo_der'] + energiaTotalSegmento['antebrazo_der']
            energia['superior_izquierdo'] = energiaTotalSegmento['brazo_izq'] + energiaTotalSegmento['antebrazo_izq']
            energia['inferior_derecho'] = energiaTotalSegmento['muslo_der'] + energiaTotalSegmento['pierna_der']+ energiaTotalSegmento['pie_der']
            energia['inferior_izquierdo'] = energiaTotalSegmento['muslo_izq'] + energiaTotalSegmento['pierna_izq']+ energiaTotalSegmento['pie_izq']


            # realizado diff para calcular incrementos positivos
            difEnergia = energia.diff()
            difEnergia.iloc[0] = difEnergia.iloc[1]
            #v=f*l   l=v/f  f=1/periodo

            #frecuencia de paso
            f = 1/(difEnergia.shape[0]*dt)
            #largo de paso
            l =(info['vel (km/h)'].item()/3.6)/f
            #trabajo interno por segmento 
            trabajoInternoSegmento= difEnergia.where(difEnergia>0).sum()
            #trabajo interno total
            wInt = trabajoInternoSegmento.sum()/(masa*l)
            # se frea dataframe de fila de datos
            t= pd.DataFrame(data=[(reg,info['mass (kg)'].item(),info.gait.item(),info['vel (km/h)'].item(),i,wInt)],columns = totalWork.columns)
            # se agrega la fila al total de resultados
            totalWork = totalWork.append(t,ignore_index=True)

# se exporta el total de trabajos calculados
totalWork.to_pickle('totalWork.pkl')
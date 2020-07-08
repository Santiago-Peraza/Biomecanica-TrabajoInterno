import numpy as np
from scipy import signal
import math
import pandas as pd


def energia_rot(aux, masa, n):
    # masas relativas:
    m_bra = masa * 0.028
    m_ant = masa * 0.022
    m_mus = masa * 0.100
    m_leg = masa * 0.0465
    m_foo = masa * 0.0145
    aux[n]=aux[n]/1000
    start = aux[n].index[0]
    dt = 0.1
    win = np.array([1 / (2 * dt), 0, -1 / (2 * dt)])

    d1_r = []
    d2_r = []
    d3_r = []
    d4_r = []
    d5_r = []
    d6_r = []
    d7_r = []
    d8_r = []
    d9_r = []
    d10_r = []
    d11_r = []

    a1_r = []
    a2_r = []
    b1_r = []
    b2_r = []
    b3_r = []

    d1_l = []
    d2_l = []
    d3_l = []
    d4_l = []
    d5_l = []
    d6_l = []
    d7_l = []
    d8_l = []
    d9_l = []
    d10_l = []
    d11_l = []

    a1_l = []
    a2_l = []
    b1_l = []
    b2_l = []
    b3_l = []

    h = 0
    
    for i in range(start, start + len(aux[n]['RLOBx'])):
        # LADOS
        
        #  DERECHA  ####################################################################################################
        d1_r.append(math.sqrt(((aux[n]['RSHx'][i]) - (aux[n]['RELBx'][i])) ** 2 + (
                    (aux[n]['RSHy'][i]) - (aux[n]['RELBy'][i])) ** 2 + (
                                          (aux[n]['RSHz'][i]) - (aux[n]['RELBz'][i])) ** 2))
        d2_r.append(math.sqrt(((aux[n]['RWRx'][i]) - (aux[n]['RELBx'][i])) ** 2 + (
                    (aux[n]['RWRy'][i]) - (aux[n]['RELBy'][i])) ** 2 + (
                                          (aux[n]['RWRz'][i]) - (aux[n]['RELBz'][i])) ** 2))
        d3_r.append(math.sqrt(
            ((aux[n]['RSHx'][i]) - (aux[n]['RWRx'][i])) ** 2 + ((aux[n]['RSHy'][i]) - (aux[n]['RWRy'][i])) ** 2 + (
                        (aux[n]['RSHz'][i]) - (aux[n]['RWRz'][i])) ** 2))
        d4_r.append(math.sqrt(((aux[n]['RGTx'][i]) - (aux[n]['RELBx'][i])) ** 2 + (
                    (aux[n]['RGTy'][i]) - (aux[n]['RELBy'][i])) ** 2 + (
                                          (aux[n]['RGTz'][i]) - (aux[n]['RELBz'][i])) ** 2))
        d5_r.append(math.sqrt(
            ((aux[n]['RSHx'][i]) - (aux[n]['RGTx'][i])) ** 2 + ((aux[n]['RSHy'][i]) - (aux[n]['RGTy'][i])) ** 2 + (
                        (aux[n]['RSHz'][i]) - (aux[n]['RGTz'][i])) ** 2))
        d6_r.append(math.sqrt(
            ((aux[n]['RSHx'][i]) - (aux[n]['RKNx'][i])) ** 2 + ((aux[n]['RSHy'][i]) - (aux[n]['RKNy'][i])) ** 2 + (
                        (aux[n]['RSHz'][i]) - (aux[n]['RKNz'][i])) ** 2))
        d7_r.append(math.sqrt(
            ((aux[n]['RGTx'][i]) - (aux[n]['RKNx'][i])) ** 2 + ((aux[n]['RGTy'][i]) - (aux[n]['RKNy'][i])) ** 2 + (
                        (aux[n]['RGTz'][i]) - (aux[n]['RKNz'][i])) ** 2))
        d8_r.append(math.sqrt(((aux[n]['RGTx'][i]) - (aux[n]['RHEEx'][i])) ** 2 + (
                    (aux[n]['RGTy'][i]) - (aux[n]['RHEEy'][i])) ** 2 + (
                                          (aux[n]['RGTz'][i]) - (aux[n]['RHEEz'][i])) ** 2))
        d9_r.append(math.sqrt(((aux[n]['RHEEx'][i]) - (aux[n]['RKNx'][i])) ** 2 + (
                    (aux[n]['RHEEy'][i]) - (aux[n]['RKNy'][i])) ** 2 + (
                                          (aux[n]['RHEEz'][i]) - (aux[n]['RKNz'][i])) ** 2))
        d10_r.append(math.sqrt(
            ((aux[n]['RKNx'][i]) - (aux[n]['RMTx'][i])) ** 2 + ((aux[n]['RKNy'][i]) - (aux[n]['RMTy'][i])) ** 2 + (
                        (aux[n]['RKNz'][i]) - (aux[n]['RMTz'][i])) ** 2))
        d11_r.append(math.sqrt(((aux[n]['RMTx'][i]) - (aux[n]['RHEEx'][i])) ** 2 + (
                    (aux[n]['RMTy'][i]) - (aux[n]['RHEEy'][i])) ** 2 + (
                                           (aux[n]['RMTz'][i]) - (aux[n]['RHEEz'][i])) ** 2))

        # ANGULOS
        a1_r.append(math.acos((d1_r[h] ** 2 + d2_r[h] ** 2 - d3_r[h] ** 2) / (2 * d1_r[h] * d2_r[h])) * (
                    180 / math.pi))  # angulo de antebrazo
        a2_r.append(math.acos((d1_r[h] ** 2 + d5_r[h] ** 2 - d4_r[h] ** 2) / (2 * d1_r[h] * d5_r[h])) * (
                    180 / math.pi))  # angulo del brazo

        b1_r.append(math.acos((d5_r[h] ** 2 + d7_r[h] ** 2 - d6_r[h] ** 2) / (2 * d5_r[h] * d7_r[h])) * (
                    180 / math.pi))  # angulo muslo
        b2_r.append(math.acos((d7_r[h] ** 2 + d9_r[h] ** 2 - d8_r[h] ** 2) / (2 * d7_r[h] * d9_r[h])) * (
                    180 / math.pi))  # angulo tibia
        b3_r.append(math.acos((d9_r[h] ** 2 + d11_r[h] ** 2 - d10_r[h] ** 2) / (2 * d9_r[h] * d11_r[h])) * (
                    180 / math.pi))  # angulo pie

        #  IZQUIERDA  ##################################################################################################
        d1_l.append(math.sqrt(((aux[n]['LSHx'][i]) - (aux[n]['LELBx'][i])) ** 2 + (
                    (aux[n]['LSHy'][i]) - (aux[n]['LELBy'][i])) ** 2 + (
                                          (aux[n]['LSHz'][i]) - (aux[n]['LELBz'][i])) ** 2))
        d2_l.append(math.sqrt(((aux[n]['LWRx'][i]) - (aux[n]['LELBx'][i])) ** 2 + (
                    (aux[n]['LWRy'][i]) - (aux[n]['LELBy'][i])) ** 2 + (
                                          (aux[n]['LWRz'][i]) - (aux[n]['LELBz'][i])) ** 2))
        d3_l.append(math.sqrt(
            ((aux[n]['LSHx'][i]) - (aux[n]['LWRx'][i])) ** 2 + ((aux[n]['LSHy'][i]) - (aux[n]['LWRy'][i])) ** 2 + (
                        (aux[n]['LSHz'][i]) - (aux[n]['LWRz'][i])) ** 2))
        d4_l.append(math.sqrt(((aux[n]['LGTx'][i]) - (aux[n]['LELBx'][i])) ** 2 + (
                    (aux[n]['LGTy'][i]) - (aux[n]['LELBy'][i])) ** 2 + (
                                          (aux[n]['LGTz'][i]) - (aux[n]['LELBz'][i])) ** 2))
        d5_l.append(math.sqrt(
            ((aux[n]['LSHx'][i]) - (aux[n]['LGTx'][i])) ** 2 + ((aux[n]['LSHy'][i]) - (aux[n]['LGTy'][i])) ** 2 + (
                        (aux[n]['LSHz'][i]) - (aux[n]['LGTz'][i])) ** 2))
        d6_l.append(math.sqrt(
            ((aux[n]['LSHx'][i]) - (aux[n]['LKNx'][i])) ** 2 + ((aux[n]['LSHy'][i]) - (aux[n]['LKNy'][i])) ** 2 + (
                        (aux[n]['LSHz'][i]) - (aux[n]['LKNz'][i])) ** 2))
        d7_l.append(math.sqrt(
            ((aux[n]['LGTx'][i]) - (aux[n]['LKNx'][i])) ** 2 + ((aux[n]['LGTy'][i]) - (aux[n]['LKNy'][i])) ** 2 + (
                        (aux[n]['LGTz'][i]) - (aux[n]['LKNz'][i])) ** 2))
        d8_l.append(math.sqrt(((aux[n]['LGTx'][i]) - (aux[n]['LHEEx'][i])) ** 2 + (
                    (aux[n]['LGTy'][i]) - (aux[n]['LHEEy'][i])) ** 2 + (
                                          (aux[n]['LGTz'][i]) - (aux[n]['LHEEz'][i])) ** 2))
        d9_l.append(math.sqrt(((aux[n]['LHEEx'][i]) - (aux[n]['LKNx'][i])) ** 2 + (
                    (aux[n]['LHEEy'][i]) - (aux[n]['LKNy'][i])) ** 2 + (
                                          (aux[n]['LHEEz'][i]) - (aux[n]['LKNz'][i])) ** 2))
        d10_l.append(math.sqrt(
            ((aux[n]['LKNx'][i]) - (aux[n]['LMTx'][i])) ** 2 + ((aux[n]['LKNy'][i]) - (aux[n]['LMTy'][i])) ** 2 + (
                        (aux[n]['LKNz'][i]) - (aux[n]['LMTz'][i])) ** 2))
        d11_l.append(math.sqrt(((aux[n]['LMTx'][i]) - (aux[n]['LHEEx'][i])) ** 2 + (
                    (aux[n]['LMTy'][i]) - (aux[n]['LHEEy'][i])) ** 2 + (
                                           (aux[n]['LMTz'][i]) - (aux[n]['LHEEz'][i])) ** 2))

        # ANGULOS
        a1_l.append(math.acos((d1_l[h] ** 2 + d2_l[h] ** 2 - d3_l[h] ** 2) / (2 * d1_l[h] * d2_l[h])) * (
                    180 / math.pi))  # angulo de antebrazo
        a2_l.append(math.acos((d1_l[h] ** 2 + d5_l[h] ** 2 - d4_l[h] ** 2) / (2 * d1_l[h] * d5_l[h])) * (
                    180 / math.pi))  # angulo del brazo

        b1_l.append(math.acos((d5_l[h] ** 2 + d7_l[h] ** 2 - d6_l[h] ** 2) / (2 * d5_l[h] * d7_l[h])) * (
                    180 / math.pi))  # angulo muslo
        b2_l.append(math.acos((d7_l[h] ** 2 + d9_l[h] ** 2 - d8_l[h] ** 2) / (2 * d7_l[h] * d9_l[h])) * (
                    180 / math.pi))  # angulo tibia
        b3_l.append(math.acos((d9_l[h] ** 2 + d11_l[h] ** 2 - d10_l[h] ** 2) / (2 * d9_l[h] * d11_l[h])) * (
                    180 / math.pi))  # angulo pie

        h = h + 1
    # OMEGA DERECHA
    wa1_r = signal.convolve(a1_r, win, 'same')
    wa1_r[0] = wa1_r[1]
    wa1_r[len(wa1_r)-1] = wa1_r[len(wa1_r)-2]

    wa2_r = signal.convolve(a2_r, win, 'same')
    wa2_r[0] = wa2_r[1]
    wa2_r[len(wa2_r)-1] = wa2_r[len(wa2_r)-2]

    wb1_r = signal.convolve(b1_r, win, 'same')
    wb1_r[0] = wb1_r[1]
    wb1_r[len(wb1_r)-1] = wb1_r[len(wb1_r)-2]

    wb2_r = signal.convolve(b2_r, win, 'same')
    wb2_r[0] = wb2_r[1]
    wb2_r[len(wb2_r)-1] = wb2_r[len(wb2_r)-2]

    wb3_r = signal.convolve(b3_r, win, 'same')
    wb3_r[0] = wb3_r[1]
    wb3_r[len(wb3_r)-1] = wb3_r[len(wb3_r)-2]

    # OMEGA IZQUIERDA
    wa1_l = signal.convolve(a1_l, win, 'same')
    wa1_l[0] = wa1_l[1]
    wa1_l[len(wa1_l)-1] = wa1_l[len(wa1_l)-2]

    wa2_l = signal.convolve(a2_l, win, 'same')
    wa2_l[0] = wa2_l[1]
    wa2_l[len(wa2_l)-1] = wa2_l[len(wa2_l)-2]

    wb1_l = signal.convolve(b1_l, win, 'same')
    wb1_l[0] = wb1_l[1]
    wb1_l[len(wb1_l)-1] = wb1_l[len(wb1_l)-2]

    wb2_l = signal.convolve(b2_l, win, 'same')
    wb2_l[0] = wb2_l[1]
    wb2_l[len(wb2_l)-1] = wb2_l[len(wb2_l)-2]

    wb3_l = signal.convolve(b3_l, win, 'same')
    wb3_l[0] = wb3_l[1]
    wb3_l[len(wb3_l)-1] = wb3_l[len(wb3_l)-2]

    # Energia DERECHA
    E_bra_r = []
    E_ant_r = []
    E_mus_r = []
    E_leg_r = []
    E_foo_r = []
    for k in range(0, len(wa1_r)):
        E_bra_r.append(0.5 * m_bra * d1_r[k] ** 2 * wa2_r[k] ** 2)
        E_ant_r.append(0.5 * m_ant * d2_r[k] ** 2 * wa1_r[k] ** 2)
        E_mus_r.append(0.5 * m_mus * d7_r[k] ** 2 * wb1_r[k] ** 2)
        E_leg_r.append(0.5 * m_leg * d9_r[k] ** 2 * wb2_r[k] ** 2)
        E_foo_r.append(0.5 * m_foo * d11_r[k] ** 2 * wb3_r[k] ** 2)

    # Energia IZQUIERDA
    E_bra_l = []
    E_ant_l = []
    E_mus_l = []
    E_leg_l = []
    E_foo_l = []
    for k in range(0, len(wa1_l)):
        E_bra_l.append(0.5 * m_bra * d1_l[k] ** 2 * wa2_l[k] ** 2)
        E_ant_l.append(0.5 * m_ant * d2_l[k] ** 2 * wa1_l[k] ** 2)
        E_mus_l.append(0.5 * m_mus * d7_l[k] ** 2 * wb1_l[k] ** 2)
        E_leg_l.append(0.5 * m_leg * d9_l[k] ** 2 * wb2_l[k] ** 2)
        E_foo_l.append(0.5 * m_foo * d11_l[k] ** 2 * wb3_l[k] ** 2)

    E_rot = pd.DataFrame(data={'E_b_r': E_bra_r, 'E_a_r': E_ant_r, 'E_g_r': E_mus_r, 'E_p_r': E_leg_r, 'E_pie_r': E_foo_l, 'E_b_l': E_bra_l, 'E_a_l': E_ant_l, 'E_g_l': E_mus_l, 'E_p_l': E_leg_l, 'E_pie_l': E_foo_l})
    return E_rot


file = 'data_proyecto_biomec2020.npy'
data = np.load(file, allow_pickle=True).item()
datos = data['MP_W_065']['kinematic_l']
m = data['MP_W_065']['info']['mass (kg)'][0]

e_rot = energia_rot(datos, m, 0)


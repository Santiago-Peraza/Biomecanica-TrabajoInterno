import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import math
import pandas as pd


def energia_rot(aux, masa):
    # masas relativas:
    m_bra = masa * 0.028
    m_ant = masa * 0.022
    m_mus = masa * 0.100
    m_leg = masa * 0.0465
    m_foo = masa * 0.0145

    start = 36
    dt = 0.1
    win = np.array([1 / (2 * dt), 0, -1 / (2 * dt)])
    E_b = []
    E_a = []
    E_g = []
    E_p = []
    E_pie = []
    for n in range(0, len(aux) - 1):
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
        h = 0
        for i in range(start, start + len(aux[n]['RLOBx']) - 1):
            # LADOS
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

            h = h + 1
        # OMEGA
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

        # Energia
        E_bra = []
        E_ant = []
        E_mus = []
        E_leg = []
        E_foo = []
        for k in range(0, len(wa1_r) - 1):
            E_bra.append(0.5 * m_bra * d1_r[k] ** 2 * wa2_r[k] ** 2)
            E_ant.append(0.5 * m_ant * d2_r[k] ** 2 * wa1_r[k] ** 2)
            E_mus.append(0.5 * m_mus * d7_r[k] ** 2 * wb1_r[k] ** 2)
            E_leg.append(0.5 * m_leg * d9_r[k] ** 2 * wb2_r[k] ** 2)
            E_foo.append(0.5 * m_foo * d11_r[k] ** 2 * wb3_r[k] ** 2)
        E_b.append(E_bra)  # energia rot del segmento del braso
        E_a.append(E_ant)  # energia rot del antebrazo
        E_g.append(E_mus)  # energia del gluteo
        E_p.append(E_leg)  # energia de la pierna
        E_pie.append(E_foo)  # energia de pie

        start = start + len(aux[n]['RLOBx'])
    # print(type(E_b))
    E_rot = pd.DataFrame(data={'E_b': E_b, 'E_a': E_a, 'E_g': E_g, 'E_p': E_p, 'E_pie': E_pie})
    return E_rot

# Retorna un df con la energia rotacional de cada segmento, tiene columnas E_b, E_a...
# con la energia de cada segmento de todos los pasos


file = 'data_proyecto_biomec2020.npy'
data = np.load(file, allow_pickle=True).item()
datos_l = data['MP_W_065']['kinematic_l']
m_l = data['MP_W_065']['info']['mass (kg)'][0]

e_rot_l = energia_rot(datos_l, m_l)
# print(e_rot_l['E_b'][0])

# plt.plot(1)
# plt.figure(e_rot_l['E_b'][0])
# plt.show()

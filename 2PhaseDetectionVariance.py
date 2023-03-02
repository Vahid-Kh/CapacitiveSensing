
import pandas as pd                 # Dataframe library
import numpy as np                  # Scientific computing with nD object support
import random as rd
import math
from functions import sct_ave_groupby,plot_5_maxed,sct_df, sct,  plt, sct_fit, fit,plot_1 ,plot_5, sctFitAve, sctMVAve, plot_5_Scalable
from scipy.signal import butter, lfilter, freqz


def rec_ave(n, xold, x, x10):
    return xold + 1 / n * (x - x10)


def recursive_variance(data):
    if len(data) == 1:
        return 0
    else:
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        # return math.sqrt(variance + recursive_variance(data[:-1]))
        return variance + recursive_variance(data[:-1])


def mov_ave(a, n=100):
    if n > 0:
        list_mov_ave = a[0:n]
        x_old = sum(list_mov_ave) / n
        for i in range(n, len(a)):
            x_new = rec_ave(n, x_old, a[i], a[i - n])
            list_mov_ave.append(x_new)
            x_old = x_new
        return list_mov_ave

    else:
        return a


def mov_var(a, n=50):
    if n > 0:
        list_var = a[0:n]
        var_old = 0
        for i in range(n, len(a)):
            var_new = recursive_variance(a[i - n:i])
            list_var.append(var_new)
            var_old = var_new
        return list_var

    else:
        return a


def logic(index):
    if index % step == 0:
        return False
    return True


""" ___ CONSTANTS ___ """
step = 1
nMovAve = 200
nVarAve = 50
lowRange = 0
highRange = 1



""" Choose data from a list of available data"""

days = [
    # "230106 - Liquid Detection",
    "MSS - HIH6021 - 27-02-2023",
    # "MSS-HIH6020-28-02-2023"
    ]


for daily in range(len(days)):
    """ Color of plot """
    if daily == 0:
        col = (1, 0, 0)
    elif daily == 1:
        col = (0, 0.9, 1)
    elif daily == 2:
        col = (0.6, 0.2, 0.8)
    elif daily == 3:
        col = (1, 0, 1)
    elif daily == 4:
        col = (0.4, 1, 0)
    elif daily == 5:
        col = (0, 0.2, 1)
    elif daily == 6:
        col = (1, 1, 0)
    elif daily == 7:
        col = (0, 0, 0)
    else:
        col = (
                rd.random(),
                rd.random(),
                rd.random()
                )

    dfRaw = pd.read_excel('Data/Clean/' + days[daily] + ".xlsx", skiprows=lambda x: logic(x))
    """ To take a portion of dataframe """

    df_Raw = dfRaw[int(len(dfRaw)*lowRange):int(len(dfRaw)*highRange)]


    """ Defining variables to be used """
    time = df_Raw['time'].tolist()
    Temp = np.array(df_Raw['Temp'])
    RH = np.array(df_Raw['RH%'])
    P_Suction = np.array(df_Raw['Pressure-1'])


    """ Antioine equaation """
    AntioineA = 8.07131  # Valid for range 0 t0 100
    AntioineB = 1730.63  # Valid for range 0 t0 100
    AntioineC = 233.426  # Valid for range 0 t0 100
    PSat = 10**(AntioineA-(AntioineB/(AntioineC+Temp)))
    PPartial = ((RH/100) * PSat).tolist()
    Temp = list(Temp)

    """ PLOT """

    label = ["Time [s]",
             "Capacitance [-]",
             "Moving average Capacitance",
             "Variance of capacitance",
             "Measured temperature [degC]",
             "Variance of Tempreture [-]"]



    plot_5_maxed(time[nMovAve:],
                    PPartial[nMovAve:],
                    mov_ave(PPartial,nMovAve)[nMovAve:],
                    mov_ave(mov_var(PPartial,nVarAve),nMovAve)[nMovAve:],
                    Temp[nMovAve:],
                    mov_ave(mov_var(Temp,nVarAve),nMovAve)[nMovAve:],
                    label, "  ")

plt.show()



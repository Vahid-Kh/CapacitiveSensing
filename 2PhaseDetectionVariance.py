
import pandas as pd                 # Dataframe library
import numpy as np                  # Scientific computing with nD object support
import random as rd
import math
from functions import sct_ave_groupby,sct_df, sct,  plt, sct_fit, fit,plot_1 ,plot_2, sctFitAve, sctMVAve
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


def mov_var(a, n=100):
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

""" ___ CONSTANTS ___ """

step = 1
label = [0]*100
n =50
timeGap = 8
sumGapLimit = 4


"""__________Functions_________"""
# # # Refrence for Low pass filter : https://www.delftstack.com/howto/python/low-pass-filter-python/


def logic(index):
    if index % step == 0:
        return False
    return True


# def butter_lowpass(cutoff, fs, order=5):
#     nyq = 0.5 * fs
#     normal_cutoff = cutoff / nyq
#     b, a = butter(order, normal_cutoff, btype='low', analog=False)
#     return b, a
#
#
# def butter_lowpass_filter(data, cutoff, fs, order=5):
#     b, a = butter_lowpass(cutoff, fs, order=order)
#     y = lfilter(b, a, data)
#     return y




"""________________________________________________________________________________"""

days = [


    "230106 - Liquid Detection",
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
    df_Raw = dfRaw
    # df_Raw = dfRaw[2000:]
    df_Raw = dfRaw[int(len(dfRaw)*0.1):int(len(dfRaw)*1)]
    # df_Raw = dfRaw[:2000]
    """______________________________________ X _________________________________________"""
    # v1, label[1] = df['Temp'], 'Temp [degC] '
    v1, label[1] = df_Raw['time'], 'Time [s]'
    # v1, label[1] = df[''], ''
    # v1, label[1] = df[''], ''
    # v1, label[1] = df[''], ''
    """______________________________________ Y _________________________________________"""


    v2, label[2] = df_Raw['RH%'], 'RH%'
    # v2, label[2] = df['Temp'], 'Temp [degC] '
    # v2, label[2] = df[],
    # v2, label[2] = df[],

    time = df_Raw['time'].tolist()
    var1 = v1.tolist()
    var2 = v2.tolist()

    """ Antioine equaation """
    AntioineA = 8.07131  # Valid for range 0 t0 100
    AntioineB = 1730.63  # Valid for range 0 t0 100
    AntioineC = 233.426  # Valid for range 0 t0 100
    Temp = np.array(df_Raw['Temp'])
    RH = np.array(df_Raw['RH%'])
    PSat = 10**(AntioineA-(AntioineB/(AntioineC+Temp)))
    PPartial = ((RH/100) * PSat).tolist()

    """ PLOT """
    """To fix the legend"""
    legend = 18
    wt = " "
    leg = []
    n_ave = 1
    po = 2


    weeklist = " "
    lpdm = len(days)
    for i in range(lpdm):
        leg.append(days[i][:legend] + "Scatter data")
        leg.append(days[i][:legend] + "Moving average")
        leg.append(days[i][:legend] + "Moving average derivative difference")
        leg.append(days[i][:legend] + "Moving average derivative difference exceeding threshold")
    """__________________________________________________________________________________"""

    dict_dff = {
        label[1]: var1,
        label[2]: var2,
        }
    df = pd.DataFrame(dict_dff)



    """         """
    """    ---------       """
    print("  Average of  ", days[daily][:3], sum(df[label[2]]) / (len(df[label[2]])))
    plt.figure(str(str(label[1]) + " vs, " +  str(label[2]) + " for " + str(weeklist )))

    plt.axes().set_facecolor(color=(0.97, 0.97, 0.97))
    x=df[label[1]].tolist()
    y=df[label[2]].tolist()
    plt.scatter(df[label[1]], df[label[2]], marker='.', color=(0.7, 0.7, 0.2), s=1)
    # print(len(mov_ave(df[label[2]], 100)))
    plt.scatter(df[label[1]], mov_ave(df[label[2]].tolist(), n), marker='.', color=(1.00,0.65,0.50), s=0.4)
    # plt.scatter(x, np.array(y) - np.array(mov_ave(y, 100)), marker=',',color=(rd.random(), rd.random(), rd.random()), s=1)
    y_diff = np.array(y) - np.array(mov_ave(y, n)) - abs(np.array(y) - np.array(mov_ave(y, n)))

    # y=y
    y=y_diff
    dx = x[1] - x[0]
    dydx = np.gradient(y, dx)

    capturedPoints = []
    derivativeSum = []
    derivativeSumFull = []
    for i in range(len(dydx)-timeGap):
        sumGap= sum(abs(dydx[i:i+timeGap]))
        derivativeSumFull.append(sumGap)
        if sumGap> sumGapLimit:
            print("Bubble detected @ time: ", print(time[i]))
            capturedPoints.append(i)
            derivativeSum.append(sumGap)


    # plt.scatter(x, dydx, marker=',', color=(0.698, 0.847, 1.00),s=1)
    # plt.scatter([var1[i] for i in capturedPoints], [var2[i] for i in capturedPoints] , marker='*', color=(0.0, 0.9, 0.9),s=3)

    # plt.scatter([var1[i] for i in capturedPoints], [derivativeSum[j] for j in range(len(derivativeSum))], marker='.', color=(0.0, 0.9, 0.9),
    #             s=7)
    # plt.scatter([var1[i] for i in capturedPoints], [derivativeSum[j] for j in range(len(derivativeSum))], marker='.', color=(0.0, 0.5, 0.9),
    #             s=7)
    print(len(var1), len(derivativeSumFull))
    # plt.scatter(var1[timeGap:], derivativeSumFull, marker='.', color=(0.5, 0.2, 0.2),
    #             s=7)
    plt.scatter(var1[timeGap:], mov_ave(mov_var(list(np.array(PPartial)*10))[timeGap:],100), marker='.', color=(0.2, 0.2, 0.2),                s=7)
    plt.scatter(var1[timeGap:], Temp[timeGap:], marker='.', color=(0.2, 0.8, 0.2), s=7)
    plt.scatter(var1[timeGap:], mov_ave(mov_var(list(Temp[timeGap:])),100), marker='.', color=(0.7, 0.7, 0.2), s=7)
    plt.xlabel(label[1])

    plt.ylabel(label[2])
    plt.grid(c='grey', linestyle='-', linewidth=0.5, alpha=0.7)

    plt.legend(leg)
    plt.figure("rh")
    plt.scatter(var1[timeGap:], mov_ave(mov_var(var2)[timeGap:],100), marker='.', color=(0.2, 0.2, 0.2), s=7)
    plt.scatter(df[label[1]], df[label[2]], marker='.', color=col, s=1)

plt.show()

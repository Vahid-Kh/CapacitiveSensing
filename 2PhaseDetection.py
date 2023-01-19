
import pandas as pd                 # Dataframe library
import numpy as np                  # Scientific computing with nD object support
import random as rd
from functions import sct_ave_groupby,sct_df, sct, mov_ave, plt, sct_fit, fit,plot_1 ,plot_2, sctFitAve, sctMVAve
from scipy.signal import butter, lfilter, freqz

""" ___ CONSTANTS ___ """

step = 1
label = [0]*100
n =200
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

    # "220914",
    # "220915",
    # "220916",
    # "220919",
    # "220920",
    # "220921",
    # "220922",
    # "220923",
    # "220926",
    # "220929",
    # "220930",
    # "2209301",
    # "2209302",
    # "2209303",
    # "2209304",
    # "2209305",
    # "221005",
    # "221006",
    # "221011",
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
    plt.scatter(df[label[1]], df[label[2]], marker='.', color=col, s=1)
    # print(len(mov_ave(df[label[2]], 100)))
    plt.scatter(df[label[1]], mov_ave(df[label[2]].tolist(), n), marker='.', color=(1.00,0.65,0.50), s=0.4)
    # plt.scatter(x, np.array(y) - np.array(mov_ave(y, 100)), marker=',',color=(rd.random(), rd.random(), rd.random()), s=1)
    y_diff = np.array(y) - np.array(mov_ave(y, n)) - abs(np.array(y) - np.array(mov_ave(y, n)))

    # y=y
    y=y_diff
    dx = x[1] - x[0]
    dydx = np.gradient(y, dx)

    capturedPoints = []
    for i in range(len(dydx)-timeGap):
        sumGap= sum(abs(dydx[i:i+timeGap]))
        if sumGap> sumGapLimit:
            print("Bubble detected @ time: ", print(time[i]))
            capturedPoints.append(i)

    print()
    plt.scatter(x, dydx, marker=',', color=(0.698, 0.847, 1.00),s=1)
    plt.scatter([var1[i] for i in capturedPoints], [var2[i] for i in capturedPoints] , marker='*', color=(0.0, 0.9, 0.9),s=3)
    plt.xlabel(label[1])

    plt.ylabel(label[2])
    plt.grid(c='grey', linestyle='-', linewidth=0.5, alpha=0.7)

    plt.legend(leg)

plt.show()

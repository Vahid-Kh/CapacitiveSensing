
import pandas as pd                 # Dataframe library
import numpy as np                  # Scientific computing with nD object support
import random as rd
import math
from functions import mov_ave, mov_var,plot_4, plot_2,plot_2_maxed, plot_4_maxed, plot_5_maxed,  plt, plot_6_maxed, plot_7_maxed
from scipy.signal import butter, lfilter, freqz
from TDN import TDN, PSI



""" ___ CONSTANTS ___ """
step = 1
nMovAve = 10
nVarAve = 5
lowRange = 0
highRange = 1
printInterval = 1000
R = "R134a"

""" Choose data from a list of available data"""

days = [
    # "230106 - Liquid Detection",
    # "MSS - HIH6021 - 27-02-2023",
    # "MSS-HIH6020-28-02-2023",
    # "SH-v1-10-03-2023",
    # "230323",
    # "221011",
    # "SH-03-04-2023"
    # "230512_COM10",
    # "230517_COM10",

    # "230513_COM10",

    # "230517_COM10_Test",
    # "230517_COM7_Test",
    # "230531_COM7",
    # "230531_COM10",
    # "230601_COM7",
    # "230601_COM10",
    "240216 - COM20",
    "240216 - COM21"
    ]


def logic(index):
    if index % step == 0:
        return False
    return True


for daily in range(len(days)):
    print("________________________________________________________________________________")
    print("For data file:   ", days[daily])

    dfRaw = pd.read_excel('Data/Clean/' + days[daily] + ".xlsx", skiprows=lambda x: logic(x))
    """ To take a portion of dataframe """

    df_Raw = dfRaw[int(len(dfRaw)*lowRange):int(len(dfRaw)*highRange)]
    print(df_Raw.head())
    print(df_Raw.columns)


    label = ["Time [s]",
             "Capacitance (Partial pressure)",
             "Variance of capacitance [-]",
             "Temp [degC]",
             "Variance of tempreture [-]",
             ]
    print(type(df_Raw['  Temp[degC]'][1]))
    print(df_Raw['  Temp[degC]'][1])
    plot_4(df_Raw['Time'],
                 mov_ave(df_Raw[' PPartial[Pa]*10'].tolist(),nMovAve),
                 mov_ave(df_Raw[' Var_PPartial'].tolist(),nMovAve),
                 mov_ave(df_Raw['  Temp[degC]'].tolist(),nMovAve),
                 mov_ave(mov_var(df_Raw['  Temp[degC]'].tolist(), nVarAve), nMovAve),
                 label,
                 days[daily])
    # plot_4(df_Raw['Time'],
    #             mov_ave(df_Raw['  Temp[degC]'].tolist(), 150),
    #             mov_ave(df_Raw['  Temp[degC]'].tolist(), 150),
    #             mov_ave(df_Raw['  Temp[degC]'].tolist(), 150),
    #             mov_ave(df_Raw['  Temp[degC]'].tolist(), 150),
    #              label,
    #              days[daily])
    # plot_4(df_Raw['Time'],
    #              mov_ave(df_Raw[' Var_PPartial'].tolist(),150),
    #              mov_ave(df_Raw[' Var_PPartial'].tolist(),150),
    #              mov_ave(mov_var(df_Raw['  Temp[degC]'].tolist(), nVarAve), 150),
    #              mov_ave(mov_var(df_Raw['  Temp[degC]'].tolist(), nVarAve), 150),
    #              label,
    #              days[daily])
    fCorr = plt.figure("CorrPlot Date " + days[daily], figsize=(19, 15))
    plt.matshow(df_Raw.corr(), fignum=fCorr.number)
    plt.xticks(range(df_Raw.select_dtypes(['number']).shape[1]), df_Raw.select_dtypes(['number']).columns, fontsize=14, rotation=90)
    plt.yticks(range(df_Raw.select_dtypes(['number']).shape[1]), df_Raw.select_dtypes(['number']).columns, fontsize=14)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    plt.title('Correlation Matrix', fontsize=16)

plt.show()










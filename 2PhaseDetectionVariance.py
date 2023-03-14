
import pandas as pd                 # Dataframe library
import numpy as np                  # Scientific computing with nD object support
import random as rd
import math
from functions import mov_ave, mov_var, plot_2,plot_2_maxed, plot_4_maxed, plot_5_maxed,  plt, plot_6_maxed, plot_7_maxed
from scipy.signal import butter, lfilter, freqz
from TDN import TDN, PSI



""" ___ CONSTANTS ___ """
step = 1
nMovAve = 50
nVarAve = 25
lowRange = 0
highRange = 1
printInterval = 500
R = "R134a"

""" Choose data from a list of available data"""

days = [
    "230106 - Liquid Detection",
    "MSS - HIH6021 - 27-02-2023",
    "MSS-HIH6020-28-02-2023",
    "SH-v1-10-03-2023"
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

    """
    List of variables: 
    'Time', 'T_suction', 'RH', 'P_suction', 'P_discharge', 'Status', 'SH_ref', 'SH', 'OD', 'S2', 'P_evap', 'P_satEvap', 
    """
    """ Defining variables to be used """
    time = df_Raw['Time'].tolist()
    Temp = np.array(df_Raw['T_suction'])
    RH = np.array(df_Raw['RH'])
    P_Suction = np.array(df_Raw['P_suction'])

    try:
        SH = np.array(df_Raw["SH"])
        SH_ref = np.array(df_Raw["SH_ref"])
        OD = np.array(df_Raw["OD"])

    except:
        SH=[]
        print("No data provided for OD & SH")

    l_Temp = list(Temp)
    l_P_Suction = list(P_Suction)

    if days[daily] == "230106 - Liquid Detection":
        for i in range(len(P_Suction)):
            try:
                # print((PSI('T', 'Q', 1, 'P', l_P_Suction[i]*1e5, R)))
                SH.append(l_Temp[i] - (PSI('T', 'Q', 1, 'P', l_P_Suction[i]*1e5+1e5, R) - 273.15))
            except:
                SH.append(0)


    """ Antioine equaation """
    AntioineA = 8.07131  # Valid for range 0 t0 100
    AntioineB = 1730.63  # Valid for range 0 t0 100
    AntioineC = 233.426  # Valid for range 0 t0 100
    PSat = 10**(AntioineA-(AntioineB/(AntioineC+Temp)))
    PPartial = ((RH/100) * PSat).tolist()
    Temp = list(Temp)

    Rho = []
    RhoOPPartial = []
    for i in range(len(P_Suction)):
        # print(l_Temp[i]+273.15)
        # print(l_P_Suction[i] * 1e5 + 1e5)
        # print(PSI('D', 'T', l_Temp[i]+273.15 , 'P', l_P_Suction[i] * 1e5 + 1e5, R))
        # print(l_Temp[i])
        Rho.append(1 / (PSI('D', 'T', l_Temp[i] + 273.15, 'P', l_P_Suction[i] * 1e5 + 1e5, R)))
        RhoOPPartial.append(Rho[i] /PPartial[i]*100)

    """ Prepare var for plotting """
    ave_PPartial        = mov_ave(PPartial, nMovAve)[nMovAve:]
    var_ave_PPartial    = mov_ave(mov_var(PPartial, nVarAve), nMovAve)[nMovAve:]
    var_ave_Temp        = mov_ave(mov_var(Temp, nVarAve), nMovAve)[nMovAve:]


    """ PLOT """
    try:
        for i in range(len(time)):
            if i % printInterval == 0:
                print("#",'{:>8}'.format(i),
                      " | SH_ref :", '{:>6}'.format(str(round(SH_ref[i],2))),
                      " | SH :", '{:>6}'.format(str(round(SH[i],2))),
                      " | T :", '{:>7}'.format(str(round(Temp[i],2))),
                      " | ", '{:>120}'.format(str(TDN.propl(TDN(l_P_Suction[i]*1e5, 0, l_Temp[i]+273.15, 0, 0, R))))
                      )

    except:
        for i in range(len(time)):
            if i % printInterval == 0:
                print("#",'{:>8}'.format(i),
                      " | T :", '{:>6}'.format(str(round(Temp[i],2))),
                      " | SH :", '{:>6}'.format(str(round(SH[i], 2))),
                      " | ", '{:>120}'.format(str(TDN.propl(TDN(l_P_Suction[i]*1e5, 0, l_Temp[i]+273.15, 0, 0, R))))
                      )

    try:
        label = ["Time [s]",
                 "Capacitance [-]",
                 "Move Ave Capacitance [-]",
                 "Variance of capacitance [-]",
                 "Measured Temp [degC]",
                 "Variance of Temp [-]",
                 "Superheat [K]",
                 "Actual OD [-]"
                 ]


        plot_7_maxed(time[nMovAve:],
                     PPartial[nMovAve:],
                     ave_PPartial,
                     var_ave_PPartial,
                     Temp[nMovAve:],
                     var_ave_Temp,
                     SH[nMovAve:],
                     OD[nMovAve:],
                     label,
                     days[daily])
        label = ["Time [s]",
                 "Variance of capacitance [-]",
                 "Measured Temp [degC]",
                 "Variance of Temp [-]",
                 "Superheat [K]",
                 "Actual OD [-]"
                 ]
        plot_5_maxed(time[nMovAve:],
                     var_ave_PPartial,
                     Temp[nMovAve:],
                     var_ave_Temp,
                     SH[nMovAve:],
                     OD[nMovAve:],
                     label,
                     days[daily])
        label = ["Time [s]",
                 "Variance of capacitance [-]",
                 "Variance of Temp [-]",
                 ]
        plot_2_maxed(time[nMovAve:],
                     var_ave_PPartial,
                     var_ave_Temp,
                     label,
                     days[daily])


        """  
        label = ["Time [s]",
                 "Variance of capacitance [-]",
                 "Variance of Temp [-]",
                 "Superheat [K]",
                 "Actual OD [-]"
                 ]
        plot_4_maxed(time[nMovAve:],

                        mov_ave(mov_var(PPartial,nVarAve),nMovAve)[nMovAve:],
                        mov_ave(mov_var(Temp,nVarAve),nMovAve)[nMovAve:],
                        SH[nMovAve:],
                        OD[nMovAve:],
                        label,
                        days[daily])

        label = ["Time [s]",
                 "Variance of capacitance [-]",
                 "Variance of Temp [-]",
                 ]
        plot_2(time[nMovAve:],
                        mov_ave(mov_var(PPartial,nVarAve),nMovAve)[nMovAve:],
                        mov_ave(mov_var(Temp,nVarAve),nMovAve)[nMovAve:],
                        label,
                        days[daily])

        # This is a plot for Rho over PPartial to check if there is dependancy
        label = ["Time [s]",
                 "Quality sensor [-]",
                 "Move Ave Quality sensor [-]",
                 "RhoOPPartial[nMovAve:],",
                 "Measured Temp [degC]",
                 "Superheat [K]",
                 "Actual OD [-]"
                 ]
        plot_6_maxed(time[nMovAve:],
                        PPartial[nMovAve:],
                        mov_ave(PPartial,nMovAve)[nMovAve:],
                        mov_ave(mov_var( RhoOPPartial, nVarAve), nMovAve)[nMovAve:],
                        Temp[nMovAve:],
                        SH[nMovAve:],
                        OD[nMovAve:],
                        label,
                        days[daily]) 
         
        # Simillarly for corrolation plot
                       
        dict_dff = {
                "PPartial": list(PPartial),
                "Temp": list(Temp),
                "Rho": list(Rho),
                "RhoOverPPartia": list(RhoOPPartial),
                }
        dff = pd.DataFrame(dict_dff)
        fCorrdff = plt.figure("CorrPlot Date dff " + days[daily], figsize=(19, 15))
        plt.matshow(dff.corr(), fignum=fCorrdff.number)
        plt.xticks(range(dff.select_dtypes(['number']).shape[1]), dff.select_dtypes(['number']).columns, fontsize=14, rotation=90)
        plt.yticks(range(dff.select_dtypes(['number']).shape[1]), dff.select_dtypes(['number']).columns, fontsize=14)
        cbdff = plt.colorbar()
        cbdff.ax.tick_params(labelsize=14)
        plt.title('Correlation Matrix', fontsize=16);
        
        """


    except:
        label = ["Time [s]",
                 "Capacitance [-]",
                 "Move Ave Capacitance [-]",
                 "Variance of capacitance [-]",
                 "Measured Temp [degC]",
                 "Variance of Temp [-]",
                 "Superheat [K]",

                 ]
        plot_6_maxed(time[nMovAve:],
                     PPartial[nMovAve:],
                     ave_PPartial,
                     var_ave_PPartial,
                     Temp[nMovAve:],
                     var_ave_Temp,
                     SH[nMovAve:],
                     label,
                     days[daily])

        label = ["Time [s]",
                 "Variance of capacitance [-]",
                 "Measured Temp [degC]",
                 "Variance of Temp [-]",
                 "Superheat [K]",

                 ]
        plot_4_maxed(time[nMovAve:],
                     var_ave_PPartial,
                     Temp[nMovAve:],
                     var_ave_Temp,
                     SH[nMovAve:],
                     label,
                     days[daily])
        label = ["Time [s]",
                 "Variance of capacitance [-]",
                 "Variance of Temp [-]",
                 ]
        plot_2_maxed(time[nMovAve:],
                     var_ave_PPartial,

                     var_ave_Temp,
                     label,
                     days[daily])

    fCorr = plt.figure("CorrPlot Date " + days[daily], figsize=(19, 15))
    plt.matshow(df_Raw.corr(), fignum=fCorr.number)
    plt.xticks(range(df_Raw.select_dtypes(['number']).shape[1]), df_Raw.select_dtypes(['number']).columns, fontsize=14, rotation=90)
    plt.yticks(range(df_Raw.select_dtypes(['number']).shape[1]), df_Raw.select_dtypes(['number']).columns, fontsize=14)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    plt.title('Correlation Matrix', fontsize=16)

plt.show()



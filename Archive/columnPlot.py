
import pandas as pd                 # Dataframe library
import numpy as np                  # Scientific computing with nD object support
from functions import sct_ave_groupby,sct_df, mov_ave, plt, sct_fit, fit,plot_1 ,plot_2, sctFitAve, sctMVAve



"""________________________________________________________________________________"""

"""________________________________________________________________________________"""

"""Label list set up"""
label = [0]*100
step = 1


"""________________________________________________________________________________"""


def logic(index):
    if index % step == 0:
        return False
    return True


"""________________________________________________________________________________"""
""" One at a time """
days = [

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
    # "221012",
    # "221013",
    # "22101",
    # "22101",
    # "22101",
    # "22101",
    # "221027_Uno(COM6)",
    # "221027_UnoWiFi(COM7)",
    # "221104 - Flow",
    # "221108 - Uno(COM6)",
    # "221108 - WiFi(COM9)",
    # "221115 - Defrost - COM6",
    # "221115 - Defrost - COM9",
    # "221116 - Defrost - COM6",
    # "221116 - Defrost - COM9",
    # "221027_Uno(COM6)",
    # "221027_UnoWiFi(COM7)",
    # "221104 - Flow",
    # "221108 - Uno(COM6)",
    # "221108 - WiFi(COM9)",
    # "221115 - Defrost - COM6",
    # "221115 - Defrost - COM9",
    # "221116 - Defrost - COM6",
    # "221116 - Defrost - COM9",
    # "Defrost - COM6",
    # "Defrost - COM9",
    # "Defrost - COM6 - RH&TOut - flowIn",
    # "Defrost - COM9 - RH&TIn - flowOut",
    # "221119 - Defrost - COM6 - DTI Ammonia",
    # "221119 - Defrost - COM7 - DTI Ammonia",
    # "221120 - Defrost - COM6 - DTI Ammonia",
    # "221120 - Defrost - COM7 - DTI Ammonia",
    # "221121 - Defrost - COM6 - DTI Ammonia",
    # "221121 - Defrost - COM7 - DTI Ammonia",
    # "221119-21 - Defrost - COM6 - DTI Ammonia",
    # "221119-21 - Defrost - COM7 - DTI Ammonia",
    # "221122 - Defrost - COM6 - DTI Ammonia",
    # "221122 - Defrost - COM7 - DTI Ammonia",
    # # "",

    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
    # "",
]

cNum = list(range(100))

listCurveFitX = []
listCurveFitY = []

for daily in range(len(days)):
    """     Random colors    """
    # col = (
    #         rd.random(),
    #         rd.random(),
    #         rd.random()
    #         )

    """     Danfoss colors   """
    # if pdm == 0:
    #     col = (1, 0, 0)
    # if pdm == 1:
    #     col = (0, 0, 0)
    # if pdm == 2:
    #     col = (0.5, 0.5, 0.5)
    # if pdm == 3:
    #     col = (0.8, 0.8, 0.8)
    # if pdm == 4:
    #     col = (0.6, 0.1, 0.1)
    # if pdm == 5:
    #     col = (0.2, 0.2, 0.2)
    # if pdm == 6:
    #     col = (1, 0.5, 0.5)
    # if pdm == 7:
    #     col = (1, 0.9, 0.9)

    """     Visible colors   """
    if daily == 0:
        col = (1, 0, 0)
    if daily == 1:
        col = (0, 0.9, 1)
    if daily == 2:
        col = (0.6, 0.2, 0.8)
    if daily == 3:
        col = (1, 0, 1)
    if daily == 4:
        col = (0.4, 1, 0)
    if daily == 5:
        col = (0, 0.2, 1)
    if daily == 6:
        col = (1, 1, 0)
    if daily == 7:
        col = (0, 0, 0)

    df = pd.read_excel('Data/Clean/' + days[daily]+ ".xlsx", skiprows=lambda x: logic(x))
    """ To take a portion of dataframe """


    """___________________________________________________________________________________________________________
    ____________________________________________________PLOTS_____________________________________________________
    ___________________________________________________________________________________________________________"""
    """
    First plots the lines and then 'ro' spesifies red dots  __ r ::  for red and o :: for circle
        Color               Shape                  shape
        b : blue            "8"	: octagon          "," : pixel
        g : green           "s"	: square           "o" : circle
        r : red             "p"	: pentagon         "v" : triangle_down
        c : cyan            "P"	: plus (filled)    "x" : x
        m : magenta         "*"	: star             "X" : x (filled)
        y : yellow          "h"	: hexagon1         "D" : diamond
        k : black           "H"	: hexagon2         "d" : thin_diamond
        w : white           "+"	: plus
    """

    """___________________________________________________________________________________________________________
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  PERFORMANCE PLOTS  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ___________________________________________________________________________________________________________"""

    """To fix the legend"""
    legend = 25
    wt = " "
    leg = []

    weeklist = " "
    lpdm = len(days)
    for i in range(lpdm):
        leg.append(days[i][:legend] + " - Scatter data")
        # leg.append(days[i][:legend] + "Average weekly line")
        # leg.append(days[i][:legend] + "Grouped average based on X axis")
    """__________________________________________________________________________________"""

    print(leg)
    n_ave = 1
    po = 2
    movAveNum = 200

    # print(df.columns)
    # df.time_tag = pd.to_datetime(df["Time"])
    # print(df)
    # ax = df.plot
    """______________________________________ X _________________________________________"""
    var0, label[0] = df[df.columns[cNum[0]]], df.columns[cNum[0]]
    index = (np.array(df.index.values)/12/60).tolist()
    """______________________________________ Y _________________________________________"""
    var1, label[1] = df[df.columns[cNum[1]]].tolist(), df.columns[cNum[1]]
    var2, label[2] = df[df.columns[cNum[2]]].tolist(), df.columns[cNum[2]]
    var3, label[3] = df[df.columns[cNum[3]]].tolist(), df.columns[cNum[3]]
    # var5, label[5] = df[df.columns[cNum[4]]].tolist(), df.columns[cNum[4]]

    print(label[:])

    """ Antioine equaation """
    AntioineA = 8.07131  # Valid for range 0 t0 100
    AntioineB = 1730.63  # Valid for range 0 t0 100
    AntioineC = 233.426  # Valid for range 0 t0 100
    Temp = np.array(var2)
    RH = np.array(var1)
    PSat = 10**(AntioineA-(AntioineB/(AntioineC+Temp)))
    PPartial = ((RH/100) * PSat).tolist()
    # ax2 = plt.scatter(var1, mov_ave(RHTRatio, 100), marker='.', color=col, s=1)

    PPartialMovAve = mov_ave(PPartial, movAveNum)
    tempMovAve = mov_ave(var2, movAveNum)
    flowMovAve = mov_ave(var3, movAveNum*10)

    plt.figure(label[1])
    ax2 = plt.scatter(index, PPartialMovAve, marker='.', color=col, s=1)
    plt.legend(leg)

    plt.figure(label[2])
    ax3 = plt.scatter(index, tempMovAve, marker='.', color=col, s=1)
    plt.legend(leg)

    plt.figure(label[3])
    ax = plt.scatter(index, flowMovAve, marker='.', color=col, s=1)
    plt.legend(leg)

    dict_dff = {
        label[0]: var0,
        label[1]: PPartialMovAve,
        label[2]: tempMovAve,
        label[3]: flowMovAve,
        # label[5]: mov_ave(var5, 200),
        # "diff 1": mov_ave((np.array(var2)-np.array(var3)).tolist()),
        # "diff 2": mov_ave((np.array(var4) - np.array(var5)).tolist()),
    }

    dfRel = pd.DataFrame(dict_dff)

    if daily==0:
        dfRel1 = dfRel
    elif daily ==1:
        dfRel2 = dfRel

    """ Old print method using Matplotlib, could not fix the time ticker interval """
    # plt.figure(str(str(label[1]) + " vs, " +  str(label[2]) + " for " + str(weeklist )))
    # plt.scatter(var1,var2,c=col, marker=",", s=1)
    # plt.tick_params(axis='x', labelsize=10, rotation=60)
    # sct_ave_groupby(dfRel, po, col, label)
    # plt.legend(leg)

    # ax = dfRel.plot()


    # if daily == 0:
    #     ax = dfRel.plot()
    # else:
    #     ax = dfRel.plot()
    # convert the time_tag column to a datetime dtype
    # df.time_tag = pd.to_datetime(df["Time"])

    # set the time_tag column as the index
    # df.set_index('Time', inplace=True)

    # plot the dataframe
    """ To overplot data """
    # Rename the column not to creat confusion which is which
    # df.rename(columns={df.columns[cNum[1]]: df.columns[cNum[1]]+"  "+days[daily]}, inplace=True)

    # if daily == 0:
    #     ax = df[[df.columns[cNum[1]]]].plot()
    # else:
    #     df[[df.columns[cNum[1]]]].plot(ax=ax)
    # plt.scatter(var1, mov_ave(var4,100), marker='.', color=col, s=1)


length = min(len(dfRel1), len(dfRel2))
dfRel1 = dfRel1[:length]
dfRel2 = dfRel2[:length]

var0 = dfRel1[dfRel1.columns[cNum[0]]]
index = (np.array(dfRel1.index.values) / 12 / 60).tolist()

var1 = np.array(dfRel1[dfRel1.columns[cNum[1]]]-dfRel2[dfRel2.columns[cNum[1]]]).tolist()
var2 = np.array(dfRel1[dfRel1.columns[cNum[2]]]-dfRel2[dfRel2.columns[cNum[2]]]).tolist()
var3 = np.array(dfRel1[dfRel1.columns[cNum[3]]]-dfRel2[dfRel2.columns[cNum[3]]]).tolist()

plt.figure(label[1] + " Difference ")
ax2 = plt.scatter(index, var1, marker='.', color=col, s=1)

plt.figure(label[2] + " Difference ")
ax3 = plt.scatter(index, var2, marker='.', color=col, s=1)

plt.figure(label[3] + " Difference " )
ax = plt.scatter(index, var3, marker='.', color=col, s=1)


plt.show()







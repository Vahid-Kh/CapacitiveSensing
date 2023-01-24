
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
    "221201 - 3 to 4.5 SH",


    ]
""" Those with constant PPM"""
# days = [
#
#     # "220915",
#     # "220916",
#     # "220919",
#     # "220920",
#     # "220921",
#     # "220922",
#     "220923",
#     "220926",
#     "220929",
#     # "220930",
#     "2209301",
#     "2209302",
#     # "2209303",
#     # "2209304",
#     # "2209305",
#     # "221005",
#     # "221006",
#     # "221011_Stable",
#     ]

""" All days  """
# days = [
#
#     "220915",
#     "220916",
#     "220919",
#     "220920",
#     "220921",
#     "220922",
#     "220923",
#     "220926",
#     "220929",
#     # "220930",
#     "2209301",
#     "2209302",
#     "2209303",
#     # "2209304",
#     "2209305",
#     "221005",
#     "221006",]

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
    # df = df[2000:]

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
    legend = 18
    wt = " "
    leg = []

    weeklist = " "
    lpdm = len(days)
    for i in range(lpdm):
        leg.append(days[i][:legend] + "Scatter data")
        leg.append(days[i][:legend] + "Average weekly line")
        leg.append(days[i][:legend] + "Grouped average based on X axis")
    """__________________________________________________________________________________"""


    n_ave = 1
    po = 2
    relHumidRaw = [(np.poly1d(np.polyfit(df['Temp'], df['RH%'], po))(np.unique([24]))).tolist()[0]]*len(df['Temp'])
    relHumidTrue = df['RH%'].copy()
    ratioRelHumidRawToTrue = (np.array(relHumidRaw)/np.array(relHumidTrue)).tolist()

    """______________________________________ X _________________________________________"""
    tempreture, label[1] = df['Temp'], 'Temp [degC] '
    # v1, label[1] = df['time'], 'Time [s]'
    # v1, label[1] = df[''], ''
    # v1, label[1] = df[''], ''
    # v1, label[1] = df[''], ''
    """______________________________________ Y _________________________________________"""

    ratioRelHumidRawToTrue, label[2] = ratioRelHumidRawToTrue, 'RH_Raw / RH_True @ 24degC ref.'
    # v2, label[2] = df['Temp'], 'Temp [degC] '
    # v2, label[2] = df[],
    # v2, label[2] = df[],
    z = np.polyfit(tempreture, ratioRelHumidRawToTrue, 1)


    dict_dff = {
        label[1]: tempreture,
        label[2]: ratioRelHumidRawToTrue,
        }

    dfRel = pd.DataFrame(dict_dff)
    plt.figure(str(str(label[1]) + " vs, " +  str(label[2]) + " for " + str(weeklist )))
    sct_ave_groupby(dfRel, po, col, label)
    plt.legend(leg)
    print("RH_Raw / RH_True vs. Temperature - 24degC as refrence", z , "for ", days[daily])
    listCurveFitX.append(z[0])
    listCurveFitY.append(z[1])

    """______________________________________ X _________________________________________"""
    # v1, label[1] = df['Temp'], 'Temp [degC] '
    v1, label[1] = df['time'], 'Time [s]'
    # v1, label[1] = df[''], ''
    # v1, label[1] = df[''], ''
    # v1, label[1] = df[''], ''
    """______________________________________ Y _________________________________________"""


    v2, label[2] = df['RH%'], 'RH%'
    # v2, label[2] = df['Temp'], 'Temp [degC] '
    # v2, label[2] = df[],
    # v2, label[2] = df[],


    """_________________________________ var1, var2 ______________________________________"""
    time = df['time'].tolist()
    var1 = v1.tolist()
    var2 = v2.tolist()


    dict_dff = {
        label[1]: var1,
        label[2]: var2,
        }
    dff = pd.DataFrame(dict_dff)

    print("  Average of  ", days[daily][:3], sum(dff[label[2]]) / (len(dff[label[2]])))
    plt.figure(str(str(label[1]) + " vs, " +  str(label[2]) + " for " + str(weeklist )))
    sct_ave_groupby(dff, po, col, label)
    plt.legend(leg)


print(np.average(listCurveFitX), np.average(listCurveFitY))

plt.show()








import pandas as pd                 # Dataframe library
import numpy as np                  # Scientific computing with nD object support
from functions import sct_ave_groupby,sct_df, mov_ave, plt, sct_fit, fit,plot_1 ,plot_2, sctFitAve, sctMVAve



"""________________________________________________________________________________"""

"""________________________________________________________________________________"""

"""Label list set up"""
label = [0]*100
step = 1
# plotStyle= "-" # Plots as continoius line
plotStyle= "." # Plots as medium sized dots
# plotStyle= "," # Plots as tiny sized dots


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
    "220920",
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
    ]


listCurveFitX = []
listCurveFitY = []
cNum = list(range(100))
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

    df = pd.read_excel('Data/Raw/' + days[daily]+ ".xlsx", skiprows=lambda x: logic(x))
    """ To take a portion of dataframe """
    df = df[150:1000]

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

    """______________________________________ X _________________________________________"""
    var1, label[1] = df[df.columns[cNum[0]]], df.columns[cNum[0]]
    """______________________________________ Y _________________________________________"""

    var2, label[2] = df[df.columns[cNum[1]]], df.columns[cNum[1]]

    dict_dff = {
        label[1]: var1,
        label[2]: var2,
        }

    dfRel = pd.DataFrame(dict_dff)
    """ Old print method using Matplotlib, could not fix the time ticker interval """
    # plt.figure(str(str(label[1]) + " vs, " +  str(label[2]) + " for " + str(weeklist )))
    # plt.scatter(var1,var2,c=col, marker=",", s=1)
    # plt.tick_params(axis='x', labelsize=10, rotation=60)
    # sct_ave_groupby(dfRel, po, col, label)
    # plt.legend(leg)


    # convert the time_tag column to a datetime dtype
    # df.time_tag = pd.to_datetime(df["Time"])
    print(df)

    # set the time_tag column as the index
    df.set_index('Time', inplace=True)

    # plot the dataframe
    """ To overplot data """
    #Rename the column not to creat confusion which is which
    df.rename(columns={df.columns[cNum[0]]: df.columns[cNum[0]]+"  "+days[daily]}, inplace=True)

    if daily == 0:
        ax = df[[df.columns[cNum[0]]]].plot(style=plotStyle, fontsize=12)

    else:
        df[[df.columns[cNum[0]]]].plot(ax=ax, style=plotStyle, fontsize=12)

""" DF PLOT LIB: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html """
plt.show()






19.53


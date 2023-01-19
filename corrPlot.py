
import pandas as pd                 # Dataframe library
import numpy as np                  # Scientific computing with nD object support
from functions import mov_ave, plt, sct_fit, fit,plot_1 ,plot_2, sctFitAve
import random as rd
import matplotlib.pyplot as plt
import xlrd, openpyxl
import seaborn as sns
import numpy as np
import statsmodels.api as sm


# fileName = r"C:\Users\U375297\Danfoss\RAC Tech Center - Programming Projects - Python Projects\RH-T Sensor\Data\Raw\220923.xlsx"
# fileName = r"C:\Users\U375297\Danfoss\RAC Tech Center - Programming Projects - Python Projects\RH-T Sensor\Data\Raw\220926.xlsx"
# fileName = r"C:\Users\U375297\Danfoss\RAC Tech Center - Programming Projects - Python Projects\RH-T Sensor\Data\Raw\220929.xlsx"



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
    "2209301",
    "2209302",
    "2209303",
    "2209304",
    "2209305",

]

for daily in range(len(days)):
    fileName = "C:\\Users\\U375297\\Danfoss\\RAC Tech Center - Programming Projects - Python Projects\\RH-T Sensor\\\Data\\Raw\\" + days[daily] + ".xlsx"

    """Label list set up"""
    label = [0]*100
    step = 1
    n_ave= 1



    def logic(index):
        if index % step == 0:
            return False
        return True


    df = pd.read_excel(fileName, skiprows=lambda x: logic(x))
    RH = df[["RH%"]]
    # df["RH/Temp"] = np.array(df[["RH%"]])/np.array(df[["Temp"]]).tolist()


    fCorr = plt.figure("CorrPlot Date " + fileName[-11:-5], figsize=(19, 15))
    plt.matshow(df.corr(), fignum=fCorr.number)
    plt.xticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14, rotation=45)
    plt.yticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    plt.title('Correlation Matrix', fontsize=16);

    print(df.columns)
    print(df.head())



    """Adds PPM values to the dataframe"""
    df["PPM"] = [200]*len(RH)

    y=  df[["PPM"]]
    x= [df[["RH%"]],
        df[["Temp"]],

        ]

    def reg_m(y, x):
        ones = np.ones(len(x[0]))
        X = sm.add_constant(np.column_stack((x[0], ones)))
        for ele in x[1:]:
            X = sm.add_constant(np.column_stack((ele, X)))
        results = sm.OLS(y, X).fit()
        return results

    print(reg_m(y, x).summary())
    # """Seaborn version"""
    # # sns.heatmap(df.corr(),
    # #             xticklabels=df.corr().columns.values,
    # #             yticklabels=df.corr().columns.values)
    # # plt.show()

plt.show()

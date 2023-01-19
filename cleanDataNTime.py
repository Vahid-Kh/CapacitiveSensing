
import pandas as pd                 # Dataframe library
import numpy as np                  # Scientific computing with nD object support
from datetime import datetime
from functions import mov_ave
import seaborn as sns

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
    # "221005",
    # "221006",
    # "221011",
    # "221011_Stable",
    # "221012",
    # "221013",
    # "22",
    # "22",
    "230106 - Liquid Detection",

]

renameDays = days




"""Label list set up"""
label = [0]*8
label[0] = 'Time [s]'
"""----------------- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%------------- """
"""Steps for reading data, takes one data out of #Step """

step_c = 1
length = 500
n = 180    # Moving averaging sample size


for daily in range(len(days)):

    """ To append data frames together """
    # data_tr = pd.read_csv(PDM[week_tr[0] - 21], na_filter=True, skip_blank_lines=True, low_memory=False)
    # for i in week_tr[1:]:
    #     df = pd.read_csv(PDM[i - 21], na_filter=True, skip_blank_lines=True, low_memory=False)
    #     data_tr = data_tr.append(df)

    """----------------- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%------------- """

    def logic(index):

        if index % step_c == 0:
            return False
        return True

    weekdata = 'Data/' + days[daily]
    """ DataFrame read from CSV file, na_filter=False, skip_blank_lines=False """

    df = pd.read_excel('Data/Raw/' + days[daily]+ ".xlsx", skiprows=lambda x: logic(x))
    print(df.shape)
    # df.drop(df.columns[0], axis=1, inplace=True)
    for i in range(len(df)):
        print(str(df.loc[i][0]))

    """Change date format from 2019 - 08 - 01 17: 05:45.119  "%Y-%m-%d %H:%M:%S.%f "  to Seconds"""
    # t0 = datetime.strptime(df.loc[0][0], "%Y-%m-%d %H:%M:%S.%f")  # Time refrence for date conversion
    t0 = datetime.strptime("00:00:00.000000", "%H:%M:%S.%f")  # Time refrence for date conversion
    for i in range(df.shape[0]):
        try:
            DT = datetime.strptime(str(df.loc[i][0]), "%H:%M:%S.%f")
        except:
            try:
                DT = datetime.strptime(str(df.loc[i][0]), "%H:%M:%S")
            except:
                try:
                    DT = datetime.strptime(str(df.loc[i][0]), "%Y-%m-%d %H:%M:%S.%f")
                except:
                    DT = datetime.strptime(str(df.loc[i][0]), "%Y-%m-%d %H:%M:%S")

        df.at[i, 'time'] = (DT - t0).total_seconds()

    df = df.apply(pd.to_numeric, errors='coerce')

    """DROP NAN acting only on the COLUMNS with more than 1000 nan values"""
    df = df.dropna(axis='columns', thresh=1000 / step_c, subset=None, inplace=False)
    """DROP NAN acting only on the ROWS with any nan values"""


    time = df['time'].tolist()

    """________________________________________________________________________________"""
    cols = df.columns
    for j in range(10):
        for i in range(1, len(cols) - 1):
            if i >= len(cols):
                break
            try:
                if df.isnull().iloc[len(cols)-1][i]:
                    df.drop(cols[i], axis=1, inplace=True)
            except:
                print("Dont know what I just did here")

    """________________________________________________________________________________"""
    print(df.shape)
    print(df.head)
    df.to_excel("Data/Clean/" + str(renameDays[daily]) +".xlsx", index = False)


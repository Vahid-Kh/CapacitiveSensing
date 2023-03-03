
import pandas as pd                 # Dataframe library
import numpy as np                  # Scientific computing with nD object support
from datetime import datetime
from functions import mov_ave
import seaborn as sns

"""________________________________________________________________________________"""


days = [
    "221119 - Defrost - COM6 - DTI Ammonia",
    "221119 - Defrost - COM7 - DTI Ammonia",
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
    # "",
    # "",
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
    """ To select only few data from a dataframe and skip rows with Logic turned TRUE """
    def logic(index):
        if index % step_c == 0:
            return False
        # if index not in [0,1,2]:
        #     return False
        return True

    weekdata = 'Data/' + days[daily]
    """ DataFrame read from CSV file, na_filter=False, skip_blank_lines=False """

    df = pd.read_csv('Data/Raw/' + days[daily] + ".txt", skiprows=lambda x: logic(x), sep=",")




    cols = df.columns

    df.rename(columns={df.columns[0]: "Time"}, inplace=True)
    df['Time'] = df['Time'].astype(str).str.replace('->', '')

    """Change date format from 2019 - 08 - 01 17: 05:45.119  "%Y-%m-%d %H:%M:%S.%f "  to Seconds"""
    # t0 = datetime.strptime(df.loc[0][0][:-2], "%H:%M:%S.%f")  # Time refrence for date conversion
    df = df[~df[df.columns[0]].isin(["Error"])]

    """ From time format to seconds for easier handling """
    t0 = datetime.strptime("00:00:00.000", "%H:%M:%S.%f")  # Time refrence for date conversion
    for i in range(df.shape[0]):
        try:
            DT = datetime.strptime(str(df.loc[i][0][:12]), "%H:%M:%S.%f")
        except:
            DT = datetime.strptime(str(df.loc[i][0][:12]), "%H:%M:%S")
        df.at[i, 'Time'] = (DT - t0).total_seconds()

    # df = df.apply(pd.to_numeric, errors='coerce')
    """________________________________________________________________________________"""
    """________________________________________________________________________________"""


    df = df.dropna(axis='rows', subset=None, inplace=False)
    print(df.shape)
    print(df.columns)
    print(df.tail)
    df.to_excel("Data/Clean/" + str(renameDays[daily]) +".xlsx", index = False)




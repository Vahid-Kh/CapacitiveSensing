
import pandas as pd                 # Dataframe library
from datetime import datetime
# from functions import mov_ave
# import seaborn as sns
# import numpy as np     # Scientific computing with nD object support


"""________________________________________________________________________________"""


days = [
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
    "TEST",
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

""" CHOOSE number of columns want to include"""
cNum =[


    1,
    2,
    # 3,
    # 4,
]
""" ____________________________________________"""

"""CHOOSE if you want datatime format to be secoond or original"""
dateTimeFormat = "Second"
# dateTimeFormat = "Original"

"""____________________________________________"""
renameDays = days

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

    print(df)
    cols = df.columns

    df.rename(columns={df.columns[0]: "Time"}, inplace=True)
    df['Time'] = df['Time'].astype(str).str.replace('->', '')

    """Change date format from 2019 - 08 - 01 17: 05:45.119  "%Y-%m-%d %H:%M:%S.%f "  to Seconds"""
    # t0 = datetime.strptime(df.loc[0][0][:-2], "%H:%M:%S.%f")  # Time refrence for date conversion
    df = df[~df[df.columns[0]].isin(["Error"])]

    """ From time format to seconds for easier handling """

    if dateTimeFormat =="Second":
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


    """______________________________________ X _________________________________________"""
    dict_dff = { }
    dict_dff['Time'] = df['Time'].tolist()
    print(cNum)
    print(cols[1])
    #
    for i in range(len(cNum)):
        print(cols[cNum[i]])
        print(df[cols[cNum[i]]].tolist())
        dict_dff[str(cols[cNum[i]])] = df[cols[cNum[i]]].tolist()
    print(dict_dff)

    dfNew = pd.DataFrame(dict_dff)
    dfNew = dfNew.dropna(axis='rows', subset=None, inplace=False)
    print(dfNew.shape)
    print(dfNew.columns)
    print(dfNew.tail)
    dfNew.to_excel("Data/Clean/" + " Columns_Selected " + str(cNum) + str(renameDays[daily]) +".xlsx", index = False)




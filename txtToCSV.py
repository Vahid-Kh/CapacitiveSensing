import pandas as pd  # Dataframe library
from datetime import datetime
import numpy as np  # Scientific computing with nD object support

# from functions import mov_ave
# import seaborn as sns


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

    # "230131 - COM5 - Orange",
    # "230131 - COM7 - No Color",
    "230512_COM10",
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
label = [0] * 8
label[0] = 'Time [s]'
"""----------------- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%------------- """
"""Steps for reading data, takes one data out of #Step """

step_c = 1
length = 500
n = 180  # Moving averaging sample size

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
    print(df.columns)
    [print(*row, sep=', ') for row in df.values.tolist()]
    print("______________________________________________________________________")
    df_original = df.copy()
    cols = df.columns

    # df[df.columns[2]] = df_original[df_original.columns[1]]
    for i in range(len(df.columns)):
        if 0 < i < len(df.columns) - 1:
            df[df.columns[i + 1]] = df_original[df_original.columns[i]]

    df.rename(columns={df.columns[0]: "Time"}, inplace=True)
    # df['Time'] = df['Time'].astype(str).str.replace('->', ',')
    df[[df.columns[0], df.columns[1]]] = df[df.columns[0]].str.split('->', expand=True)

    """Change date format from 2019 - 08 - 01 17: 05:45.119  "%Y-%m-%d %H:%M:%S.%f "  to Seconds"""
    # t0 = datetime.strptime(df.loc[0][0][:-2], "%H:%M:%S.%f")  # Time refrence for date conversion
    df = df[~df[df.columns[0]].isin(["Error"])]

    # set the threshold value
    threshold = 0.7

    # calculate the number of NaN values in each column
    nans = df.isnull().mean()

    # drop columns with more NaN values than the threshold
    df = df.drop(columns=nans[nans > threshold].index, axis=1)

    # df = df.apply(pd.to_numeric, errors='coerce')

    df = df.dropna().reset_index(drop=True)

    """ From time format to seconds for easier handling """
    t0 = datetime.strptime("00:00:00", "%H:%M:%S")  # Time refrence for date conversion

    [print(*row, sep=', ') for row in df.values.tolist()];
    for i in range(df.shape[0]):
        try:
            try:
                DT = datetime.strptime(str(df.iloc[i][0]), "%H:%M:%S.%f")
            except:
                DT = datetime.strptime(str(df.iloc[i][0][:-1]), "%H:%M:%S.%f")
        except:
            try:
                DT = datetime.strptime(str(df.iloc[i][0][:-1]), "%H:%M:%S")
            except:
                try:
                    DT = datetime.strptime(str(df.iloc[i][0][:-1]), "%Y-%m-%d %H:%M:%S.%f")
                except:
                    DT = datetime.strptime(str(df.iloc[i][0][:-1]), "%Y-%m-%d %H:%M:%S")
        df.at[i, 'Time'] = (DT - t0).total_seconds()

    df = df.astype({' RH_HIH[%]': 'float'})
    df = df.astype({'  T_HIH[degC]': 'float'})

    df = df[((df[' RH_HIH[%]']) <= 100)]
    print(df.columns)
    [print(*row, sep=', ') for row in df.values.tolist()];
    """________________________________________________________________________________"""
    """________________________________________________________________________________"""

    df.to_excel("Data/Clean/" + str(renameDays[daily]) + ".xlsx", index=False)




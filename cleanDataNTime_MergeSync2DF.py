
import pandas as pd                 # Dataframe library
import numpy as np                  # Scientific computing with nD object support
from datetime import datetime
from functions import mov_ave
import seaborn as sns

"""________________________________________________________________________________"""


days = [
    "MSS - HIH6021 - 27-02-2023",
    # "MSS-HIH6020-28-02-2023"

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
    df2 = pd.read_excel('Data/Raw/' + days[daily]+ ".xlsx", sheet_name="SH", skiprows=lambda x: logic(x))
    print("Shape of first tab : ", df.shape, "Shape of second tab : ", df2.shape)

    # df.drop(df.columns[0], axis=1, inplace=True)
    # for i in range(len(df)):
    #     print(str(df.loc[i][0]))

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
        df.at[i, 'time'] = round((DT - t0).total_seconds(), 0)
        # print("DT", df.loc[i][0], DT, t0, round((DT - t0).total_seconds(), 0))


    i=0
    # print(df2.loc[i][0])
    # print("00:00:00 "+str(df2.loc[i][0])[:10])
    try:
        t0 = datetime.strptime( str(df2.loc[i][0])[:10]+" 00:00:00", "%Y-%m-%d %H:%M:%S")  # Time refrence for date conversion
    except:
        try:
            t0 = datetime.strptime(str(df2.loc[i][0])[:10] + " 00:00:00", "%Y:%m:%d %H:%M:%S")
        except:
            try:
                datetime.strptime(str(df2.loc[i][0])[:10], "%H:%M:%S")
            except:
                t0 = datetime.strptime("00:00:00 "+str(df2.loc[i][0])[:10] , "%Y:%m:%d %H:%M:%S")


    if days[daily] == "MSS - HIH6021 - 27-02-2023":
        for i in range(df2.shape[0]):
            try:
                DT2 = datetime.strptime(str(df2.loc[i][0]), "%Y-%m-%d %H:%M:%S")
            except:
                try:
                    DT2 = datetime.strptime(str(df2.loc[i][0]), "%H:%M:%S")
                except:
                    try:
                        DT2 = datetime.strptime(str(df2.loc[i][0]), "%d/%m/%Y %H.%M.%S")
                    except:
                        DT2 = datetime.strptime(str(df2.loc[i][0]), "%Y-%m-%d %H:%M:%S")

            # print(i, i%60)
            # print(str(df2.loc[i][0]), (DT2 - t0).total_seconds() + i%60)
            df2.at[i, 'Time'] = (DT2 - t0).total_seconds() + i%60
            # print("DT2",df2.loc[i][0],DT2, t0, (DT2 - t0).total_seconds())

    else:
        for i in range(df2.shape[0]):
            try:
                DT2 = datetime.strptime(str(df2.loc[i][0]), "%Y-%m-%d %H:%M:%S")
            except:
                try:
                    DT2 = datetime.strptime(str(df2.loc[i][0]), "%H:%M:%S")
                except:
                    try:
                        DT2 = datetime.strptime(str(df2.loc[i][0]), "%d/%m/%Y %H.%M.%S")
                    except:
                        DT2 = datetime.strptime(str(df2.loc[i][0]), "%Y-%m-%d %H:%M:%S")
            # print(str(df2.loc[i][0]), (DT2 - t0).total_seconds())
            df2.at[i, 'Time'] = (DT2 - t0).total_seconds()
            # print("DT2",df2.loc[i][0],DT2, t0, (DT2 - t0).total_seconds())

    df = df.apply(pd.to_numeric, errors='coerce')
    df2 = df2.apply(pd.to_numeric, errors='coerce')
    """DROP NAN acting only on the COLUMNS with more than 1000 nan values"""
    df = df.dropna(axis='columns', thresh=1000 / step_c, subset=None, inplace=False)
    df2 = df2.dropna(axis='columns', thresh=1000 / step_c, subset=None, inplace=False)
    """DROP NAN acting only on the ROWS with any nan values"""

    time = df['time'].tolist()
    time2 = df2['Time'].tolist()

    df2.rename(columns={'Time': 'time'}, inplace=True)
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

    df_merged = pd.merge(df, df2, on='time')
    df_merged.rename(columns={
        'time':                                                     'Time',
        'Temp':                                                     'T_suction',
        'RH%':                                                      'RH',
        'Suction Pressure':                                         'P_suction',
        'Discharge Pressure':                                       'P_discharge',
        'Operation status|U118|Par_Operation_Status':               'Status',
        'Actual SH reference (K)|U022|Par_Actual_SH_Reference':     'SH_ref',
        'Actual superheat (K)|U021|Par_Actual_Superheat':           'SH',
        'Actual OD (%)|U024|Par_Act_OD':                            'OD',
        'S2 suction pipe (°C)|U020|Par_s2':                         'S2',
        'Pe evaporator (barg)|U025|Par_p0':                         'P_evap',
        'Te saturated evaporation temperature (°C)|U026|Par_T0':    'P_satEvap',
    }, inplace=True)
    print("Shape of merged dataframes : ", df_merged.shape)
    print(df_merged.head)
    df_merged.to_excel("Data/Clean/" + str(renameDays[daily]) +".xlsx", index = False)


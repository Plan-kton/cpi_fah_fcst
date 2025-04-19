# forecast_inputs_feb_to_july.py

# Forward month variables (can also be defined here if needed)
fwrd_1 = '2025-02-01'
fwrd_2 = '2025-03-01'
fwrd_3 = '2025-04-01'
fwrd_4 = '2025-05-01'
fwrd_5 = '2025-06-01'
fwrd_6 = '2025-07-01'

import pandas as pd

# Independent forward forecast estimates
ind_label_0_dic = {
    pd.to_datetime(fwrd_1): -5.77,
    pd.to_datetime(fwrd_2): -21.46,
    pd.to_datetime(fwrd_3): -15.94418465,
    pd.to_datetime(fwrd_4): -9.956877132,
    pd.to_datetime(fwrd_5): -2.478309822,
    pd.to_datetime(fwrd_6): 2.144393784
}

ind_label_1_dic = {
    pd.to_datetime(fwrd_1): 9.86,
    pd.to_datetime(fwrd_2): 12.88,
    pd.to_datetime(fwrd_3): 16.18,
    pd.to_datetime(fwrd_4): 7.96,
    pd.to_datetime(fwrd_5): 7.96,
    pd.to_datetime(fwrd_6): 7.96
}

ind_label_2_dic = {
    pd.to_datetime(fwrd_1): 2.32,
    pd.to_datetime(fwrd_2): 2.1,
    pd.to_datetime(fwrd_3): 3.67,
    pd.to_datetime(fwrd_4): 3.28,
    pd.to_datetime(fwrd_5): 4.38,
    pd.to_datetime(fwrd_6): 5.22
}

ind_label_3_dic = {
    pd.to_datetime(fwrd_1): 5.06,
    pd.to_datetime(fwrd_2): 6.83,
    pd.to_datetime(fwrd_3): 2.18,
    pd.to_datetime(fwrd_4): 2.18,
    pd.to_datetime(fwrd_5): 2.18,
    pd.to_datetime(fwrd_6): 2.18
}

ind_label_4_dic = {
    pd.to_datetime(fwrd_1): 1.8,
    pd.to_datetime(fwrd_2): 1.8,
    pd.to_datetime(fwrd_3): 1.8,
    pd.to_datetime(fwrd_4): 1.8,
    pd.to_datetime(fwrd_5): 1.8,
    pd.to_datetime(fwrd_6): 1.8
}

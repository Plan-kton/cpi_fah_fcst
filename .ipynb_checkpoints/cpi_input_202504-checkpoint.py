# forecast_inputs_apr_to_sep.py

import pandas as pd

# Forward month strings
fwrd_1 = '2025-04-01'
fwrd_2 = '2025-05-01'
fwrd_3 = '2025-06-01'
fwrd_4 = '2025-07-01'
fwrd_5 = '2025-08-01'
fwrd_6 = '2025-09-01'

# Independent forward forecast estimates
ind_label_0_dic = {
    pd.to_datetime(fwrd_1): -9.95,
    pd.to_datetime(fwrd_2): -2.478,
    pd.to_datetime(fwrd_3): 2.144,
    pd.to_datetime(fwrd_4): -7.399,
    pd.to_datetime(fwrd_5): -16.04,
    pd.to_datetime(fwrd_6): -21.58
}

ind_label_1_dic = {
    pd.to_datetime(fwrd_1): 7.69,
    pd.to_datetime(fwrd_2): 7.69,
    pd.to_datetime(fwrd_3): 7.69,
    pd.to_datetime(fwrd_4): 7.00,
    pd.to_datetime(fwrd_5): 6.50,
    pd.to_datetime(fwrd_6): 6.00
}

ind_label_2_dic = {
    pd.to_datetime(fwrd_1): 3.28,
    pd.to_datetime(fwrd_2): 4.38,
    pd.to_datetime(fwrd_3): 5.22,
    pd.to_datetime(fwrd_4): 4.46,
    pd.to_datetime(fwrd_5): 4.50,
    pd.to_datetime(fwrd_6): 4.50
}

ind_label_3_dic = {
    pd.to_datetime(fwrd_1): 2.20,
    pd.to_datetime(fwrd_2): 2.20,
    pd.to_datetime(fwrd_3): 2.20,
    pd.to_datetime(fwrd_4): 2.20,
    pd.to_datetime(fwrd_5): 2.20,
    pd.to_datetime(fwrd_6): 2.20
}

ind_label_4_dic = {
    pd.to_datetime(fwrd_1): 1.80,
    pd.to_datetime(fwrd_2): 1.70,
    pd.to_datetime(fwrd_3): 1.60,
    pd.to_datetime(fwrd_4): 1.50,
    pd.to_datetime(fwrd_5): 1.50,
    pd.to_datetime(fwrd_6): 1.50
}

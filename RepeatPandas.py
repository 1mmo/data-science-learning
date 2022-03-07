import pandas as pd
import numpy as np


all_user_ids = np.arange(1, 1000)
all_product_ids = np.arange(1, 100)

n = 10000

user_ids = np.random.choice(all_user_ids, n)
product_ids = np.random.choice(all_product_ids, n)

start_date = pd.to_datetime('2022-01-01')
times = pd.date_range(start_date, periods=n, freq='1min')

user_actions = pd.DataFrame({
        'user_id': user_ids,
        'product_ids': product_ids,
        'time': times,
    })
print(user_actions.iloc[1: 10, ])

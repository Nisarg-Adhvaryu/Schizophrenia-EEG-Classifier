"""
Each file contains an EEG record for one subject.
First 7680 samples represent 1st channel, then 7680 - 2nd channel, and so on.

Export data from eea file to seperate csv files, every 7680 line should be a single column for one file.
"""

import pandas as pd
import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

for file in os.listdir():
    if file.endswith('.eea'):
        data_arr = read_file(file)
        df = pd.DataFrame()

        for i in range(16):
            channel = data_arr[i*7680:(i+1)*7680]
            df[f'channel{i}'] = channel
            df.to_csv(f'{file}.csv', index=False)

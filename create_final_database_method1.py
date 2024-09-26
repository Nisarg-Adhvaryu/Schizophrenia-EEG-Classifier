"""
Person | Channel1Data1 | Channel1Data2 | ... | Channel1Data7680 | Channel2Data1 | ... | Channel16Data7680 | Label
Person1| 1.0           | 2.0           | ... | 3.0             | 4.0           | ... | 5.0              | 0
"""

import pandas as pd
import os
import threading

import time

inittime = time.time()

from warnings import simplefilter
simplefilter(action="ignore", category=pd.errors.PerformanceWarning) # Ignore performance warning

destination_file = 'final_database.csv'

# Save list of all csv files
all_files = os.listdir() # Get all files in the directory
all_csv_files = [file for file in all_files if file.endswith('.csv')] # Get all csv files in the directory
all_csv_files.remove(destination_file) # Remove the destination file from the list so that it does not get inc;uded in for loop

done_file_nums = [] # List to keep track of files that have been processed

final_df = pd.DataFrame() # Create an empty dataframe to store all data

def process_file(n):
    global final_df

    df = pd.read_csv(all_csv_files[n])
    # df has columns: channel0, channel1, ..., channel15, 7680 rows

    new_df = pd.DataFrame() # Create a new dataframe for each file

    new_df.loc[n, 'person'] = all_csv_files[n]
    new_df.loc[n, 'label'] = 0 # Healthy: 0, Unhealthy: 1

    for i in range(16): # number of channels
        for j in range(7680): # number of data points in each channel
            new_df.loc[n, f'channel{i}data{j}'] = df[f'channel{i}'][j] # Assign data to new_df

        # print(f'File {n} Channel {i} done') # for debugging

    print(f'File {n} done') # for debugging

    final_df = pd.concat([final_df, new_df]) # Append new_df to final_df
    final_df.to_csv('final_database.csv') # Save final_df to csv file

# create a thread for each file
threads = []
for n in range(len(all_csv_files)):
    if n not in done_file_nums:
        t = threading.Thread(target=process_file, args=(n,))
        threads.append(t)
        done_file_nums.append(n)

[t.start() for t in threads]
[t.join() for t in threads]

print('Time taken:', time.time()-inittime) # Print time taken to process all files
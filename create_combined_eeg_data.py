import os
import pandas as pd

# Paths to the folders
healthy_folder = "C:\\Users\\nisar\\one drive\\Desktop\\IEEE\\healthy"
schizophrenic_folder = "C:\\Users\\nisar\\one drive\\Desktop\\IEEE\\schizophrenic"

# List to store dataframes
df_list = []

# Function to read and combine .csv files from a folder
def combine_files_from_folder(folder_path, label):
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path)
            df['label'] = label  # Add a column to indicate healthy or schizophrenic
            df['file_name'] = file  # Add a column to indicate the file name
            df_list.append(df)

# Combine healthy .csv files
combine_files_from_folder(healthy_folder, '0')

# Combine schizophrenic .csv files
combine_files_from_folder(schizophrenic_folder, '1')

# Concatenate all the dataframes
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined dataframe to a new .csv file
combined_df.to_csv('combined_eeg_data.csv', index=False)

print("Data combined and saved to 'combined_eeg_data.csv'.")

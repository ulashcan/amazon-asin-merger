import os
import pandas as pd

folder_path = '/Users/wingman/PycharmProjects/amazon/data'

csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

unique_asins = set()

file_counter = 1
asin_counter = 0

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)

    if 'ASIN' in df.columns:
        for asin in df['ASIN']:
            if asin not in unique_asins:
                unique_asins.add(asin)
                asin_counter += 1

                if asin_counter % 3000 == 0:
                    with open(f'asins_{file_counter}.txt', 'w') as f:
                        for a in unique_asins:
                            f.write(a + '\n')
                    file_counter += 1
                    unique_asins.clear()

if unique_asins:
    with open(f'asins_{file_counter}.txt', 'w') as f:
        for asin in unique_asins:
            f.write(asin + '\n')

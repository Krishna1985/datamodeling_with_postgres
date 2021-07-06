import os
import glob
import numpy as np
import psycopg2
import pandas as pd
import sql_query


# def get_files(filepath):
#     all_files = []
#     for root, dirs, files in os.walk(filepath):
#         files = glob.glob(os.path.join(root,'*.json'))
#         for f in files :
#             all_files.append(os.path.abspath(f))
    
#     return all_files
all_files = []
for root, dirs, files in os.walk('song_data'):
    files = glob.glob(os.path.join(root,'*.json'))
    for f in files :
        all_files.append(os.path.abspath(f))

print(type(all_files),len(all_files))

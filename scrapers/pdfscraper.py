import pandas as pd # library for data manipulation
import numpy as np
import pdfplumber # library for scraping pdfs
# from tqdm import tqdm
import time

path = "/home/pandas/Downloads/2021-22 PUS Generic Application Form mod.pdf"

pdf = pdfplumber.open(path)
# print(pdf.metadata)
# print(pdf.pages)
pages = pdf.pages

# pages[1].extract_table()[7][0].replace("\n",'')

# string = "This is a sample string"

# Find the index of the substring "sample"
# start_index = string.find('Bachelor')

# Print the portion of the string starting from the index of the substring "sample"
# print(string[start_index:])

pg = []
for j in range(len(pages)):
    for i in range(len(pages[j].extract_table())):
        try:
            if 'Bachelor' in pages[j].extract_table()[i+1][0].replace("\n",''):
                course = pages[j].extract_table()[i+1][0].replace("\n",'')
                # Find the index of the substring "sample"
                start_index = course.find('Bachelor')
#                 print(pages[j].extract_table()[i+1][3].replace("\n",''))
                print(course[start_index:])
                pg.append(course[start_index:])
    #             print(pages[j].extract_table()[i+1][9].replace("\n",''))


                print()
            else:
                continue

        except:
            continue

arr = np.array(pg)
df_path = '/home/pandas/Documents/career-guidance-system/datasets'
pd.DataFrame(data = {"programs":arr}).to_excel(df_path+'programs.xlsx', index = False)

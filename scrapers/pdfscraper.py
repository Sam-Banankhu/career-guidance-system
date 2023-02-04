import pandas as pd # library for data manipulation
import pdfplumber # library for scraping pdfs
# from tqdm import tqdm
import time

path = "/home/pandas/Downloads/2021-22 PUS Generic Application Form mod.pdf"

pdf = pdfplumber.open(path)
# print(pdf.metadata)
# print(pdf.pages)
pages = pdf.pages

# pages[1].extract_table()[7][0].replace("\n",'')

string = "This is a sample string"

# Find the index of the substring "sample"
start_index = string.find('Bachelor')

# Print the portion of the string starting from the index of the substring "sample"
# print(string[start_index:])

import pandas as pd # library for data manipulation
import pdfplumber # library for scraping pdfs
# from tqdm import tqdm
import time

path = "/home/pandas/Downloads/2021-22 PUS Generic Application Form mod.pdf"

pdf = pdfplumber.open(path)
# print(pdf.metadata)
# print(pdf.pages)
pages = pdf.pages
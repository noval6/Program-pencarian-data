import pandas as pd
import csv

data=[]
Frame = pd.read_csv(r'D:\Tugas kuliah\DATA\DATA.csv')

cari= False
Publication = str(input("Cari Publication :"))

for i in range(101):
    if Frame.values[i][1] == Publication:
        cari = True
        break
      
if cari:
    print(Frame.values[i])
    print("Data didapatkan")
else:
    print("Data tidak di dapatkan")
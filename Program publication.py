import pandas as pd
import csv

data=[]

DFrame = pd.read_csv(r'D:\Tugas kuliah\Semester 3\Praktikum STRUKDAT\Google Scholar - Top English Publications.csv')
search = False
Publication = str(input("Masukan Publication yg dicari :"))
for i in range(101):
    if DFrame.values[i][1] == Publication:
        search = True
        break
if search:
    print(DFrame.values[i])
    print("Data telah ditemukan")
else:
    print("Data tidak ditemukan")
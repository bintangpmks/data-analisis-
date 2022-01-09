# -*- coding: utf-8 -*-
"""

@materi : algoritma dan pemograman
@judul : Data analisis
@hari/tanggal : Kamis/23/12/2021
@nim : 065002100023
@author : Tri Bintang Pamungkas 
"""

import pandas as pd

def pertama(data):

    file = open("negaraMean.csv","w")
    file.write(data)
    file.close()

def kedua(data):

    file = open("NegaraStandarDevisiasi.csv","w")
    file.write(data)
    file.close()

data = {"Negara": ["Indonesia", "Jepang", "India", "China", "Amerika Serikat", "Brazil", "Rusia"],
        "Ibu Kota": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brazilia", "Moskow"],
        "Benua": ["Asia", "Asia", "Asia", "Asia", "Amerika", "Amerika", "Asia"],
        "Luas": [1905, 377, 3287, 9597, 9834, 8515, 17098],
        "Populasi": [264, 143, 1252, 1357, 329, 210, 146] }

df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("Berikut Data Framenya:\n")
print(df)
print("\nBerikut Data Mean:")
print(mean)
print("\nBerikut Data Standar Devisiasi")
print(std)
pertama(str(mean))
kedua(str(std))
print("\nFile Berhasil dibuat")
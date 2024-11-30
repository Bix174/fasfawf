import numpy as np

# arr = np.array([90,60,70,50])
# arr = np.arange([0,10,2])
# print(arr)

# print(f'hasil penjumlahan{arr + 2}')

arr = np.array([90,60,70,50])
total = np.sum(arr)
rata2 = np.mean(arr)
jumlah_nilai_diatas_rata2 = np.sum(arr>60)
nilai_tertinggi = np.max(arr)
nilai_terendah = np.min
print(f'total data : {total}')
print(f'rata rata data : {rata2}') 
print(f'jumlah nilai diatas rata2 : {jumlah_nilai_diatas_rata2}') 
print(f'nilai tertinggi : {nilai_tertinggi}') 
print(f'nilai terendah : {nilai_terendah}') 

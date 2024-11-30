import numpy

jumlah_siswa =int(input('masukan jumlah siswa :'))

nilai_ujian = [0]

for i in range(jumlah_siswa):
    nilai = int(input(f'masukan nilai ujian siswa'))
    nilai_ujian.append(nilai)

rata2_nilai = sum(nilai_ujian)/jumlah_siswa
nilai_tertinggi = max(nilai_ujian)
nilai_terendah = min(nilai_ujian)
jumlah_rata2_
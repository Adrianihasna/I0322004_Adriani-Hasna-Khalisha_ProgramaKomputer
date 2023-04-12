#inputdata
harga_rumah = int(input("Masukkan harga (sesuai tipe) rumah dalam juta:"))
uang_muka = int(input("Masukkan uang muka dalam juta :"))
JangkaWaktu = int(input("Masukkan jangka waktu dalam tahun :"))
Bunga = 0.005

#Report I
Besar_hutang = harga_rumah - uang_muka
Cicilan_pokokbulanan = Besar_hutang / (JangkaWaktu * 12)
Cicilan_bungabulanan = ((Bunga * Besar_hutang * JangkaWaktu)/(JangkaWaktu * 12))
Total_cicilan = Cicilan_pokokbulanan + Cicilan_bungabulanan

print("=========================================")
print(f'Besar hutang = Rp. {Besar_hutang} juta rupiah')
print(f'Cicilan pokok bulanan = Rp. {Cicilan_pokokbulanan} juta /bulan')
print(f'Cicilan bunga bulanan = Rp. {Cicilan_bungabulanan} juta rupiah/bulan')
print(f'Total cicilan setiap bulan = Rp. {Total_cicilan} juta rupiah/bulan')

Biaya_notaris = 2
Biaya_provisi = 1.5
pajak_pembelian = 0.025*harga_rumah
pnpb = 0.65
balik_nama = 2.5
total_pembayaran = uang_muka + Total_cicilan + Biaya_notaris + Biaya_provisi + balik_nama + pnpb

print("=========================================")
print(f'Uang Muka = Rp. {uang_muka} juta rupiah')
print(f'Cicilan bulanan pertama = Rp. {Total_cicilan} juta rupiah')
print(f'Biaya Notaris = Rp. {Biaya_notaris} juta rupiah')
print(f'Biaya Provisi = Rp. {Biaya_provisi} juta rupiah')
print(f'Pajak Pembelian = Rp. {pajak_pembelian} juta rupiah')
print(f'PNPB = Rp. {pnpb} juta rupiah')
print(f'Biaya Balik nama = Rp. {balik_nama} juta rupiah')
print(f'Total pembayaran pertama = Rp. {total_pembayaran} juta rupiah')
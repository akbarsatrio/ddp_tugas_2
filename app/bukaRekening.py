import random, string
import getpass
import app.index as index
import app.bukaRekening as bukaRekening
import app.daftarTransfer as daftarTransfer
import app.setoranTunai as setoranTunai
import app.tarikTunai as tarikTunai
import app.transfer as transfer

def main():
  print('\n*** BUKA REKENING ***')
  namaNasabah = input('Masukan nama : ')  #input untuk memasukan Nama
  while True: #perulangan tanpa henti jika pengguna memasukan input yang nilainya false
    print('[ PIN HARUS 6 DIGIT ]')
    pinNasabah = getpass.getpass('Buat PIN Anda : ')  #buat pin nasabah dengan fungsi getpass
    if len(pinNasabah) == 6:  #jika pin nasabah panjangnya adalah 6, maka jalankan statement dibawah
      pinNasabah2 = getpass.getpass('Konfirmasi PIN Anda : ') #buat konfirmasi pin
      if pinNasabah == pinNasabah2: #jika pin nasabah valuenya sama dengan pinnasabah2
        setoranNasabah = int(input('Masukan setoran awal : Rp. '))  #input untuk seotran nasabah
        if setoranNasabah >= 10000: #percabangan untuk memvalidasi harus ada minimul setoran yaitu 10rb
          norekNasabah = 'REK'+''.join(random.choice(string.digits) for _ in range(3))  #generate nomor otomatis menggunakan random string
          openNasabah = open('data/nasabah.txt', 'a') #membuka file nasabah.txt
          data = [norekNasabah, namaNasabah, str(setoranNasabah), pinNasabah+'\n']  #vaiabel data untuk menampung data list
          openNasabah.writelines(','.join(data)) #input data menggunakan writelines dengan value dari variabel data digabungkan dengan ','
          openNasabah.close() #tutup setelah melakukan operasi
          break #stop
        else:
          print('Masukan jumlah setoran minimal Rp.10000\n')  #jika setoran dibawah 10rb, balik lagi ke while
          pass
      else:
        print('\nKonfirmasi PIN anda salah')
        pass
    else:
      print('\nPanjang pin harus 6')
      pass
  print('\nPembukaan rekening dengan nomor', norekNasabah, 'atas nama', namaNasabah, 'berhasil.')
  print('Tekan enter untuk ke menu')
  input()
  index.main()
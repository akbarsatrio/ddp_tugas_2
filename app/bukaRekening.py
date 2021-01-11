import random, string
import getpass
import app.index as index
import app.bukaRekening as bukaRekening
import app.daftarTransfer as daftarTransfer
import app.setoranTunai as setoranTunai
import app.tarikTunai as tarikTunai
import app.transfer as transfer

def main():
  # # Masukan Nama Nasabah
  # namaNasabah = input('Masukan Nama Nasabah : ')
  # # Masukan Setoran Awal
  # setoranAwal = input('Masukan Setoran Awal : Rp. ')
  # # Generate nomor rekening lewat random string
  # norekNasabah = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
  # pinNasabah = getpass.getpass('Masukan PIN : ')
  # # simpan ketiga variabel ke dalam variabel data
  # data = (norekNasabah+','+namaNasabah+','+setoranAwal+','+pinNasabah+'\n')
  # # buka file nasabah.txt dan simpan kedalam variabel file dengan permission 'a'
  # file = open('data/nasabah.txt', 'a')
  # # panggil variabel file lalu tulis menggunakan fungsi writelines dengan value variabel data
  # file.writelines(data)
  # # tutup jika penulisan data sudah selesai
  # file.close()
  # print('Pembuatan Rekening baru berhasil')
  print('\n*** BUKA REKENING ***')
  namaNasabah = input('Masukan nama : ')  #input untuk memasukan Nama
  while True: #perulangan tanpa henti jika pengguna memasukan input yang nilainya false
    print('[ PIN HARUS 6 DIGIT ]')
    pinNasabah = getpass.getpass('Buat PIN Anda : ')
    if len(pinNasabah) == 6:
      pinNasabah2 = getpass.getpass('Konfirmasi PIN Anda : ')
      if pinNasabah == pinNasabah2:
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
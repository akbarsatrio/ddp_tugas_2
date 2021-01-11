import random, string
import getpass
import app.index as index
import app.bukaRekening as bukaRekening
import app.daftarTransfer as daftarTransfer
import app.setoranTunai as setoranTunai
import app.tarikTunai as tarikTunai
import app.transfer as transfer

def main():
  # Masukan Nama Nasabah
  namaNasabah = input('Masukan Nama Nasabah : ')
  # Masukan Setoran Awal
  setoranAwal = input('Masukan Setoran Awal : Rp. ')
  # Generate nomor rekening lewat random string
  norekNasabah = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
  pinNasabah = getpass.getpass('Masukan PIN : ')
  # simpan ketiga variabel ke dalam variabel data
  data = (norekNasabah+','+namaNasabah+','+setoranAwal+','+pinNasabah+'\n')
  # buka file nasabah.txt dan simpan kedalam variabel file dengan permission 'a'
  file = open('data/nasabah.txt', 'a')
  # panggil variabel file lalu tulis menggunakan fungsi writelines dengan value variabel data
  file.writelines(data)
  # tutup jika penulisan data sudah selesai
  file.close()
  print('Pembuatan Rekening baru berhasil')

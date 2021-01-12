import getpass
import app.index as index
import app.bukaRekening as bukaRekening
import app.daftarTransfer as daftarTransfer
import app.setoranTunai as setoranTunai
import app.tarikTunai as tarikTunai
import app.transfer as transfer

def main():
  print('\n*** DATA TRANSFER ***')
  while True: #perulangan while dengan kondisi True, ini digunakan ketika pengguna memasukan input yang mengeluarkan nilai False, maka akan terus berulang
    norekNasabah = input('Masukan nomor rekening Anda : ')  #norek nasabah untuk memasukan nomor rekening nasabah
    pinNasabah = getpass.getpass('Masukan PIN Anda : ') #norek nasabah untuk memasukan pin rekening nasabah
    if checkNorek(norekNasabah, pinNasabah) is True:  #jika fungsi checkNorek mengembalikan nilai True, maka..
      if checkTransfer(norekNasabah) is True: #jika fungsi checkTransfer mengembalikan nilai True, maka..
        print('\nDaftar transfer dari rekening', norekNasabah, ':')
        for dataTransfer in checkTransfer.getTransferData:  #loop value dari variabel getTransferData yang berada di fungsi checkTransfer lalu ditampung kedalam variabel dataTransfer
          dataTransferSplit = dataTransfer.split(',') #buat variabel dataTrasnferSplit untuk mengubah kedalam array list
          if dataTransferSplit[1] == norekNasabah:  #jika dataTransferSplit index ke 1 (No Rekening) nilainya sama dengan value dari variabel norekNasabah, maka...
            dataTransferResult = dataTransfer.replace(',', ' ') #buat variabel dataTransferResult dengan value dataTransfer yang dimana tanda koma (',') di replace dengan whitespace
            print(dataTransferResult, end="")
          else:
            pass
        print('\nTekan Enter untuk ke menu')
        input()
        index.main()
        return False
      else:
        print('Tidak ada data yang ditampilkan')
    else:
      print('PIN atau nomor rekening Anda salah')

def checkNorek(norekNasabah, pinNasabah): #fungsi checkNorek untuk memvalidasi nomor rekening di dalam nasabah.txt
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # nama variabel yang diawali dengan nama fungsi itu sendiri agar variabelnya bisa dipanggil di fungsi lain  #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  openNasabah = open('data/nasabah.txt')  #buka file nasabah.txt lalu simpan kedalam variabel openNasabah
  checkNorek.getNasabahData = openNasabah.readlines() #buat variabel getNasabahData dengan value openNasabah.readlines()
  for nasabahData in checkNorek.getNasabahData: #loop value dari checkNorek.getNasabahData sebagai nasabahData
    nasabahData = nasabahData.split(',')  #variabel nasabah data di split dengan ',' lalu simpan kedalam variabel itu sendiri
    if nasabahData[0] == norekNasabah:  #jika nasabah data index 0 (rekening) sama dengan norekNasabah (input), maka...
      if nasabahData[3] == pinNasabah+'\n': #jika nasabah data index 3 (rekening) sama dengan pinNasabah (input), maka...
        return True #kembalikan nilai True
      else:
        pass
    else:
      pass
  openNasabah.close() #tutup file openNasabah

def checkTransfer(norekNasabah):
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # nama variabel yang diawali dengan nama fungsi itu sendiri agar variabelnya bisa dipanggil di fungsi lain  #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  openTransfer = open('data/transfer.txt')  #buka file transfer.txt lalu simpan kedalam variabel openTransfer
  checkTransfer.getTransferData = openTransfer.readlines()  #buat variabel getTransferData dengan value openTransfer.readlines()
  for transferData in checkTransfer.getTransferData:  #loop value dari checkTransfer.getTransfer sebagai nasabahData
    transferData = transferData.split(',')  #variabel transfer data di split dengan ',' lalu simpan kedalam variabel itu sendiri
    if transferData[1] == norekNasabah: #jika transferData index ke 1 (nomor rekening) valuenya sama dengan norekNasabah, maka..
      return True #kembalikan nilai True
    else:
      pass
  openTransfer.close()  #tutup file openTransfer

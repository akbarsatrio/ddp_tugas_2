import random, string
import getpass
import app.index as index
import app.bukaRekening as bukaRekening
import app.daftarTransfer as daftarTransfer
import app.setoranTunai as setoranTunai
import app.tarikTunai as tarikTunai
import app.transfer as transfer

def main():
  print('*** TRANSFER ***')
  while True: #menjalankan perulangan dengan kondisi True
    norekNasabah = input('Masukan nomor rekening Anda : ')  #memasukan nomor rekening sumber/nasabah
    pinNasabah = getpass.getpass('Masukan PIN : ')  #memasukan pin rekening sumber/nasabah
    if checkNorek(norekNasabah, pinNasabah) is True:  #panggil fungsi checknorek dengan parameter norek nasabah dan pin nasabah
      while True: #jika fungsi diatas mengembalikan nilai true, maka jalankan perulangan while ke-2 dengan kondisi True
        print()
        norekTujuan = input('Masukan nomor rekening tujuan : ') #input norek tujuan
        if checkNorekTujuan(norekTujuan) is True: #panggil funsgi check norek tujuan dan jika mengembalikan nilai true, maka...
          nominalTransfer = int(input('Masukan nominal yang akan di transfer : Rp. '))  #masukan nominal transfer
          if int(checkNorek.getNasabahSaldo) >= nominalTransfer:  #ambil data saldo nasabah di fungsi check norek
            totalUangNasabah = int(checkNorek.getNasabahSaldo)-nominalTransfer  #kurangi data saldo nasabah dengan nominal jumlah transfer lalu masukan kedalam total uang nasabah
            totalUangTujuan = int(checkNorekTujuan.getTujuanDataSaldo)+nominalTransfer  #tambahkan data saldo tujuan dengan nominal transfer lalu simpan kedalam total uang tujuan
            currentDataNasabah = [norekNasabah, checkNorek.getNasabahNama, str(totalUangNasabah), pinNasabah+'\n']  #buat data nasabah sumber yang baru/diubah dan simpan kedalam variabel currentDataNasabah dengan tipe data list
            currentDataTujuan = [norekTujuan, checkNorekTujuan.getTujuanNama, str(totalUangTujuan), checkNorekTujuan.getTujuanPin]  #buat data nasbaah tujuan yang baru/diubah dan simpan kedalam variabel currentDataTUjuan dengan tipe data list
            checkNorek.getNasabahData[checkNorek.getNasabahIndex] = ','.join(currentDataNasabah)  #panggil variabel getNasabahData di fungsi checkNorek serta index nasabah sumber pada checkNorek.getNasabahIndex, lalu valuenya diganti dengan currentDataNasabah
            checkNorek.getNasabahData[checkNorekTujuan.getTujuanIndex] = ','.join(currentDataTujuan)  #panggil variabel getNasabahData di fungsi checkNorek serta index nasabah tujuan pada checkNorekTujuan.getTujuanIndex, lalu valuenya diganti dengan currentDataTujuan
            openNasabahWrite = open('data/nasabah.txt', 'w')  #buka file nasabah txt dengan permission write lalu simpan kedalam openNasabahWrite
            for dataInput in checkNorek.getNasabahData: #loop value dari checkNorek.getNasabahData sebagai variabel dataInput
              openNasabahWrite.writelines(dataInput)  #panggil variabel openNasabahWrite lalu tulis dengan fungsi writelines dengan value dataInput, otomatis file nasabah.txt akan ditimpa semuanya dengan dataInput
            openNasabahWrite.close()  #tutup file jika aksi sudah selesai
            openTransfer = open('data/transfer.txt', 'a') #sekarang buka file transfer, dengan permisssion file 'a'
            dataTransfer = ['TRF'+''.join(random.choice(string.digits) for _ in range(3)), norekNasabah, norekTujuan, str(nominalTransfer)+'\n']  #buat dataTransfer ddengan value kode unik transfer, norek nasabah, norek tujuan, nominal transfer
            openTransfer.writelines(','.join(dataTransfer)) #tulis data transfer ke openTransfer menggunakan fungsi writelines
            openTransfer.close()  #tutup jika aksi sudah selesai
            print('Transfer berhasil, total saldo Anda sekarang Rp.', totalUangNasabah)
            print('Tekan Enter untuk ke menu')
            input()
            index.main()
            return False
          else:
            print('Saldo tidak mencukupi. Transfer gagal')
            print('Tekan enter untuk ke menu')
            input()
            index.main()
            return False
        else:
          print('Nomor rekening tujuan tidak ditemukan :(')
    else:
      print('PIN atau nomor rekening Anda salah')
      pass

def checkNorek(norekNasabah, pinNasabah): #definisikan checkNorek dengan parameter norekNasabah dan pinNasabah
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # nama variabel yang diawali dengan nama fungsi itu sendiri agar variabelnya bisa dipanggil di fungsi lain  #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  openNasabah = open('data/nasabah.txt')  #buka file nasabah.txt dan simpan kedalam openNasabah
  checkNorek.getNasabahData = openNasabah.readlines() #buat variabel getNasabahData dengan value openNasabah.readlines()
  checkNorek.getNasabahIndex = 0  #ini untuk menampung index ke berapa dalam data nasabah (untuk foreign key norek sumber)
  checkNorek.getNasabahNama = ''  #ini untuk menampung nama nasabah sumber
  checkNorek.getNasabahSaldo = 0  #ini untuk menampung nasbaah saldo
  for nasabahData in checkNorek.getNasabahData: #loop value dari getNasabahData sebagai nasabahData
    nasabahData = nasabahData.split(',')  #variabel nasabah data di split dengan ',' lalu simpan kedalam variabel itu sendiri
    if nasabahData[0] == norekNasabah:  #jika nasabah data index 0 (rekening) sama dengan norekNasabah (input), maka...
      if nasabahData[3] == pinNasabah+'\n': #jika nasabah data index 3 (rekening) sama dengan pinNasabah (input), maka...
        checkNorek.getNasabahNama = nasabahData[1]  #timpa variabel getNasabahNama dengan nasabahData index 1
        checkNorek.getNasabahSaldo = nasabahData[2] #timpa variabel getNasabahSaldo dengan nasabahData index 2
        print('Nomor rekening', norekNasabah, 'a/n', nasabahData[1], 'dengan saldo Rp.', nasabahData[2], end="")
        return True
      else:
        pass
    else:
      checkNorek.getNasabahIndex += 1
      pass
  openNasabah.close()

def checkNorekTujuan(norekTujuan):
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # nama variabel yang diawali dengan nama fungsi itu sendiri agar variabelnya bisa dipanggil di fungsi lain  #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  openNorekTujuan = open('data/nasabah.txt') #buka file nasabah.txt dan simpan kedalam openNasabah
  checkNorekTujuan.getNorekTujuanData = openNorekTujuan.readlines()
  checkNorekTujuan.getTujuanIndex = 0
  checkNorekTujuan.getTujuanNama = ''
  checkNorekTujuan.getTujuanDataSaldo = 0
  checkNorekTujuan.getTujuanPin = ''
  for nasabahTujuanData in checkNorekTujuan.getNorekTujuanData:
    nasabahTujuanData = nasabahTujuanData.split(',')
    if nasabahTujuanData[0] == norekTujuan:
      checkNorekTujuan.getTujuanNama = nasabahTujuanData[1]
      checkNorekTujuan.getTujuanDataSaldo = nasabahTujuanData[2]
      checkNorekTujuan.getTujuanPin = nasabahTujuanData[3]
      print('Nomor rekening tujuan a/n', nasabahTujuanData[1])
      return True
    else:
      checkNorekTujuan.getTujuanIndex += 1
      pass
    
import getpass
import app.index as index
import app.bukaRekening as bukaRekening
import app.daftarTransfer as daftarTransfer
import app.setoranTunai as setoranTunai
import app.tarikTunai as tarikTunai
import app.transfer as transfer

def main():
  print('*** TARIK TUNAI ***')
  while True: #perulangan while dengan kondisi True, ini digunakan ketika pengguna memasukan input yang mengeluarkan nilai False, maka akan terus berulang
    norekNasabah = input('Masukan nomor rekening Anda : ')  #norek nasabah untuk memasukan nomor rekening nasabah
    pinNasabah = getpass.getpass('Masukan PIN Anda : ') #norek nasabah untuk memasukan pin rekening nasabah
    if checkNorek(norekNasabah, pinNasabah) is True:  #jika fungsi checkNorek mengembalikan nilai True, maka..
      while True:
        print()
        tarikTunai = int(input('Masukan nominal yang akan ditarik : Rp. '))
        if tarikTunai >= 50000:
          totalSaldo = int(checkNorek.getNasabahSaldo)-tarikTunai
          currentData = [norekNasabah, checkNorek.getNasabahNama, str(totalSaldo), pinNasabah+'\n']
          checkNorek.getNasabahData[checkNorek.getNasabahIndex] = ','.join(currentData)
          openNasabahWrite = open('data/nasabah.txt', 'w')
          for dataInput in checkNorek.getNasabahData:
            openNasabahWrite.writelines(dataInput)
          openNasabahWrite.close()
          print('Tarik tunai berhasil, total saldo Anda sekarang Rp.', totalSaldo)
          print('Tekan Enter untuk ke menu')
          input()
          index.main()
          return False
        else:
          pass
    else:
      print('PIN atau nomor rekening Anda salah')


def checkNorek(norekNasabah, pinNasabah): #fungsi checkNorek untuk memvalidasi nomor rekening di dalam nasabah.txt
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # nama variabel yang diawali dengan nama fungsi itu sendiri agar variabelnya bisa dipanggil di fungsi lain  #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  openNasabah = open('data/nasabah.txt')  #buka file nasabah.txt lalu simpan kedalam variabel openNasabah
  checkNorek.getNasabahData = openNasabah.readlines() #buat variabel getNasabahData dengan value openNasabah.readlines()
  checkNorek.getNasabahIndex = 0
  checkNorek.getNasabahNama = ''
  checkNorek.getNasabahSaldo = 0
  for nasabahData in checkNorek.getNasabahData: #loop value dari checkNorek.getNasabahData sebagai nasabahData
    nasabahData = nasabahData.split(',')  #variabel nasabah data di split dengan ',' lalu simpan kedalam variabel itu sendiri
    if nasabahData[0] == norekNasabah:  #jika nasabah data index 0 (rekening) sama dengan norekNasabah (input), maka...
      if nasabahData[3] == pinNasabah+'\n': #jika nasabah data index 3 (rekening) sama dengan pinNasabah (input), maka...
        checkNorek.getNasabahNama = nasabahData[1]
        checkNorek.getNasabahSaldo = nasabahData[2]
        return True #kembalikan nilai True
      else:
        pass
    else:
      checkNorek.getNasabahIndex += 1
      pass
  openNasabah.close() #tutup file openNasabah
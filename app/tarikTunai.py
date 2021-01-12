import getpass
import app.index as index
import app.bukaRekening as bukaRekening
import app.daftarTransfer as daftarTransfer
import app.setoranTunai as setoranTunai
import app.tarikTunai as tarikTunai
import app.transfer as transfer

def main():
<<<<<<< HEAD
  print('*** TARIK TUNAI ***')
  while True: #perulangan while dengan kondisi True, ini digunakan ketika pengguna memasukan input yang mengeluarkan nilai False, maka akan terus berulang
    norekNasabah = input('Masukan nomor rekening Anda : ')  #norek nasabah untuk memasukan nomor rekening nasabah
    pinNasabah = getpass.getpass('Masukan PIN Anda : ') #norek nasabah untuk memasukan pin rekening nasabah
    if checkNorek(norekNasabah, pinNasabah) is True:  #jika fungsi checkNorek mengembalikan nilai True, maka..
      while True:
        print()
        tarikTunai = int(input('Masukan nominal yang akan ditarik : Rp. '))
        if tarikTunai >= 50000:
          if int(checkNorek.getNasabahSaldo) >= tarikTunai:
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
            print('Saldo anda tidak mencukupi')
            pass
        else:
          print('Tarik tunai minimal Rp. 50000')
          pass
=======
  # This is your main area
  # nanti untuk baca file txt, cukup panggil open('data/{nama file}.txt')
  # untuk panggil fungsi di file lain, cukup panggil - namafile.namafungsi()
  # contoh bukaRekening.main()
  print('TARIK TUNAI')
  while True: 
    norekNasabah = input('Masukan nomor rekening Anda : ')
    pinNasabah = getpass.getpass ('Masukan PIN Anda : ')
    if checkNorek(norekNasabah, pinNasabah) is True:
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
        print('Tekan Enter untuk menu')
        input()
        index.main()
        return False
      else:
        print('Tarik tunai minimal Rp. 50000')
        pass
>>>>>>> 40c072d452be4b4e29c71bc64a801aee08318b07
    else:
      print('PIN atau nomor rekening Anda salah')

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
<<<<<<< HEAD
        checkNorek.getNasabahNama = nasabahData[1]
        checkNorek.getNasabahSaldo = nasabahData[2]
        print('Nomor rekening', norekNasabah, 'a/n', nasabahData[1], 'dengan saldo Rp.', nasabahData[2], end="")
        return True #kembalikan nilai True
=======
        checkNorek.getNasabahNama = nasabahData[1]  #timpa variabel getNasabahNama dengan nasabahData index 1
        checkNorek.getNasabahSaldo = nasabahData[2] #timpa variabel getNasabahSaldo dengan nasabahData index 2
        print('Nomor rekening', norekNasabah, 'a/n', nasabahData[1], 'dengan saldo Rp.', nasabahData[2], end="")
        return True
>>>>>>> 40c072d452be4b4e29c71bc64a801aee08318b07
      else:
        pass
    else:
      checkNorek.getNasabahIndex += 1
      pass
  openNasabah.close()
import getpass
import app.index as index
import app.bukaRekening as bukaRekening
import app.daftarTransfer as daftarTransfer
import app.setoranTunai as setoranTunai
import app.tarikTunai as tarikTunai
import app.transfer as transfer

def main():
  print('\n*** TARIK TUNAI ***')
  while True: #perulangan while dengan kondisi True, ini digunakan ketika pengguna memasukan input yang mengeluarkan nilai False, maka akan terus berulang
    norekNasabah = input('Masukan nomor rekening Anda : ').upper()  #norek nasabah untuk memasukan nomor rekening nasabah
    pinNasabah = getpass.getpass('Masukan PIN Anda : ') #norek nasabah untuk memasukan pin rekening nasabah
    if checkNorek(norekNasabah, pinNasabah) is True:  #jika fungsi checkNorek mengembalikan nilai True, maka..
      while True: #loop while dengan kondisi true
        print()
        tarikTunai = int(input('Masukan nominal yang akan ditarik : Rp. ')) #masukan input nominal tarik tunai kedalam variabel tarikTunai
        if tarikTunai >= 50000: #set minimum tarik tunai 50 ribu
          if int(checkNorek.getNasabahSaldo) >= tarikTunai: #cek saldo nasabah dan pastikan lebih besar = dari jumlah tarik tunai, data diambil dari fungsi checkNorek.getNasabahSaldo.
            totalSaldo = int(checkNorek.getNasabahSaldo)-tarikTunai #set total saldo nasbah, dikurangi dengan jumlah tarik tunai
            currentData = [norekNasabah, checkNorek.getNasabahNama, str(totalSaldo), pinNasabah+'\n'] #buat ada list yang valuenya adalah data2 pendukung untuk menimpa data sebelumnya
            checkNorek.getNasabahData[checkNorek.getNasabahIndex] = ','.join(currentData) #ambil data pada variabel getNasabahData pada fungsi checkNorek dan di indexing sesuai index nasbaah, dan timpa varluenya dengan variabel currentData
            openNasabahWrite = open('data/nasabah.txt', 'w')  #buka nasabah.txt dengan permission w
            for dataInput in checkNorek.getNasabahData: #loop data getNasabahData dari fungsi checkNorek sebagai dataInput, lalu...
              openNasabahWrite.writelines(dataInput)  #panggil openNasabahWrite dan gabungkan dengan fungsi writelines dengan value dataInput
            openNasabahWrite.close()  #tutup file jika sudah selesai
            break
          else:
            print('Saldo anda tidak mencukupi')
            pass
        else:
          print('Tarik tunai minimal Rp. 50000')
          pass
      break
    else:
      print('PIN atau nomor rekening Anda salah')
  print('Tarik tunai Rp.', tarikTunai, 'berhasil. Total saldo Anda sekarang Rp.', totalSaldo)
  print('Tekan Enter untuk ke menu')
  input()
  index.main()

def checkNorek(norekNasabah, pinNasabah): #definisikan checkNorek dengan parameter norekNasabah dan pinNasabah
  openNasabah = open('data/nasabah.txt')  #buka file nasabah.txt dan simpan kedalam openNasabah
  checkNorek.getNasabahData = openNasabah.readlines() #buat variabel getNasabahData dengan value openNasabah.readlines()
  checkNorek.getNasabahIndex = 0  #ini untuk menampung index ke berapa dalam data nasabah (untuk foreign key norek sumber)
  checkNorek.getNasabahNama = ''  #ini untuk menampung nama nasabah sumber
  checkNorek.getNasabahSaldo = 0  #ini untuk menampung nasbaah saldo
  for nasabahData in checkNorek.getNasabahData: #loop value dari getNasabahData sebagai nasabahData
    nasabahData = nasabahData.split(',')  #variabel nasabah data di split dengan ',' lalu simpan kedalam variabel itu sendiri
    if nasabahData[0] == norekNasabah:  #jika nasabah data index 0 (rekening) sama dengan norekNasabah (input), maka...
      if nasabahData[3] == pinNasabah+'\n': #jika nasabah data index 3 (rekening) sama dengan pinNasabah (input), maka...
        checkNorek.getNasabahNama = nasabahData[1]
        checkNorek.getNasabahSaldo = nasabahData[2]
        print('Nomor rekening', norekNasabah, 'a/n', nasabahData[1], 'dengan saldo Rp.', nasabahData[2], end="")
        return True #kembalikan nilai True
      else:
        pass
    else:
      checkNorek.getNasabahIndex += 1
      pass
  openNasabah.close()
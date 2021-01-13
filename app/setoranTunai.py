import getpass
import app.index as index
import app.bukaRekening as bukaRekening
import app.daftarTransfer as daftarTransfer
import app.setoranTunai as setoranTunai
import app.tarikTunai as tarikTunai
import app.transfer as transfer

def main():
  print('\n*** SETOR TUNAI ***')
  while True:
    norekNasabah = input('Masukan Nomor Rekening : ').upper()
    pinNasabah = getpass.getpass('Masukan PIN : ')
    if checkNorek(norekNasabah, pinNasabah) is True:
      while True:
        print()
        setoranTunai = int(input('Masukan setoran tunai : Rp. '))
        if setoranTunai >= 10000:
          totalSetoran = int(checkNorek.getNasabahSaldo)+setoranTunai
          currentData = [norekNasabah, checkNorek.getNasabahNama, str(totalSetoran), pinNasabah+'\n']
          checkNorek.getNasabahData[checkNorek.getNasabahIndex] = ','.join(currentData)
          openNasabahWrite = open('data/nasabah.txt', 'w')
          for dataInput in checkNorek.getNasabahData:
            openNasabahWrite.writelines(dataInput)
          openNasabahWrite.close()
          print('Setoran tunai berhasil, total saldo Anda sekarang Rp.', totalSetoran)
          break
        else:
          print('Minimum setoran adalah Rp. 10000')
      break
    else:
      print('PIN atau nomor rekening Anda salah')
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
        checkNorek.getNasabahNama = nasabahData[1]  #timpa variabel getNasabahNama dengan nasabahData index 1
        checkNorek.getNasabahSaldo = nasabahData[2] #timpa variabel getNasabahSaldo dengan nasabahData index 2
        print('Nomor rekening', norekNasabah, 'a/n', nasabahData[1], 'dengan saldo Rp.', nasabahData[2], end="")
        return True
      else:
        pass
    else:
      checkNorek.getNasabahIndex += 1
      pass
  openNasabah.close() #tutup file openNasabah
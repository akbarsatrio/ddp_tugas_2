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
  while True:
    norekNasabah = input('Masukan nomor rekening Anda : ')
    pinNasabah = getpass.getpass('Masukan PIN : ')
    if checkNorek(norekNasabah, pinNasabah) is True:
      while True:
        print()
        norekTujuan = input('Masukan nomor rekening tujuan : ')
        if checkNorekTujuan(norekTujuan) is True:
          nominalTransfer = int(input('Masukan nominal yang akan di transfer : Rp. '))
          if int(checkNorek.getNasabahDataSaldo) >= nominalTransfer:
            totalUangNasabah = int(checkNorek.getNasabahDataSaldo)-nominalTransfer
            totalUangTujuan = int(checkNorekTujuan.getTujuanDataSaldo)+nominalTransfer
            currentDataNasabah = [norekNasabah, checkNorek.getNasabahDataNama, str(totalUangNasabah), pinNasabah+'\n']
            currentDataTujuan = [norekTujuan, checkNorekTujuan.getTujuanNama, str(totalUangTujuan), checkNorekTujuan.getTujuanPin]
            checkNorek.getNasabahData[checkNorek.getNasabahDataIndex] = ','.join(currentDataNasabah)
            checkNorek.getNasabahData[checkNorekTujuan.getTujuanDataIndex] = ','.join(currentDataTujuan)
            openNasabahWrite = open('data/nasabah.txt', 'w')
            for dataInput in checkNorek.getNasabahData:
              openNasabahWrite.writelines(dataInput)
            openNasabahWrite.close()
            openTransfer = open('data/transfer.txt', 'a')
            dataTransfer = ['TRF'+''.join(random.choice(string.digits) for _ in range(3)), norekNasabah, norekTujuan, str(nominalTransfer)]
            openTransfer.writelines(','.join(dataTransfer))
            openTransfer.close()
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

def checkNorek(norekNasabah, pinNasabah):
  openNasabah = open('data/nasabah.txt')
  checkNorek.getNasabahData = openNasabah.readlines()
  nasabahDataList = []
  checkNorek.getNasabahDataIndex = 0
  checkNorek.getNasabahDataNama = ''
  checkNorek.getNasabahDataSaldo = 0
  checkNorek.getAllNasabah = []
  for nasabahData in checkNorek.getNasabahData:
    nasabahData = nasabahData.split(',')
    if nasabahData[0] == norekNasabah:
      if nasabahData[3] == pinNasabah+'\n':
        checkNorek.getNasabahDataNama = nasabahData[1]
        checkNorek.getNasabahDataSaldo = nasabahData[2]
        print('Nomor rekening', norekNasabah, 'a/n', nasabahData[1], 'dengan saldo Rp.', nasabahData[2], end="")
        return True
      else:
        pass
    else:
      checkNorek.getNasabahDataIndex += 1
      pass
  openNasabah.close()

def checkNorekTujuan(norekTujuan):
  openNorekTujuan = open('data/nasabah.txt')
  checkNorekTujuan.getNorekTujuanData = openNorekTujuan.readlines()
  tujuanDataList = []
  checkNorekTujuan.getTujuanDataIndex = 0
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
      checkNorekTujuan.getTujuanDataIndex += 1
      pass
    
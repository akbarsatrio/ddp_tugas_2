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
          print('Tekan Enter untuk ke menu')
          input()
          index.main()
          return False
        else:
          print('Minimum setoran adalah Rp. 10000')
          pass
    else:
      print('PIN atau nomor rekening Anda salah')


def checkNorek(norekNasabah, pinNasabah):
  openNasabah = open('data/nasabah.txt')
  checkNorek.getNasabahData = openNasabah.readlines()
  checkNorek.getNasabahIndex = 0
  checkNorek.getNasabahNama = ''
  checkNorek.getNasabahSaldo = 0
  for nasabahData in checkNorek.getNasabahData:
    nasabahData = nasabahData.split(',')
    if nasabahData[0] == norekNasabah:
      if nasabahData[3] == pinNasabah+'\n':
        checkNorek.getNasabahNama = nasabahData[1]
        checkNorek.getNasabahSaldo = nasabahData[2]
        print('Nomor rekening', norekNasabah, 'a/n', nasabahData[1], 'dengan saldo Rp.', nasabahData[2], end="")
        return True
      else:
        pass
    else:
      checkNorek.getNasabahIndex += 1
      pass
  openNasabah.close()
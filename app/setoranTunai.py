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
    norekNasabah = input('Masukan Nomor Rekening : ')
    pinNasabah = getpass.getpass('Masukan PIN : ')
    if checkNorek(norekNasabah, pinNasabah) is True:
      while True:
        print()
        setoranTunai = int(input('Masukan setoran tunai : '))
        if setoranTunai >= 10000:
          totalSetoran = int(checkNorek.getNasabahDataSaldo)+setoranTunai
          currentData = [norekNasabah, checkNorek.getNasabahDataNama, str(totalSetoran), pinNasabah+'\n']
          checkNorek.getNasabahData[checkNorek.getNasabahDataIndex] = ','.join(currentData)
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
      print('Nomor rekening tidak ditemukan :(')
      loop = False


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







  # condition = True
  # while condition:
  #   norekNasabah = input('Masukan nomor rekening : ')
  #   openNasabah = open('data/nasabah.txt')
  #   getNasabah = openNasabah.readlines()  #mambaca file nasabar dalam satu baris & list
  #   openNasabah.close() #tutup setelah melakukan aksi
  #   getIndex = 0  #digunakan untuk membaca index keberapa yang nomor rekeningnya yang cocok
  #   for singleNasabah in getNasabah:  #perulangan untuk sin`gleNasabah dalam variabel getNasabah
  #     singleNasabah = singleNasabah.split(',')  #split single nasabah menggunakan koma
  #     if singleNasabah[0] == norekNasabah:  #jika singleNasabah[0] (norek) sama dengan apa yg diinput
  #       print('Nomor rekening atas nama', singleNasabah[1], 'dengan saldo Rp.',singleNasabah[2], end="")
  #       setoranTunai = int(input('Masukan jumlah setoran : Rp. '))  #jalankan setoran tunai
  #       if setoranTunai >= 10000:
  #         totalSetoran = int(singleNasabah[2])+setoranTunai #buat total setoran dari sebelumnya dengan yang baru untuk dijumlahkan
  #         data = [norekNasabah, singleNasabah[1], str(totalSetoran)+'\n'] #buat variabel data untuk memasukan data baru
  #         getNasabah[getIndex] = ','.join(data) #panggil variabel getNasabah dengan index keberapa, lalu masukan value dari variabel data di join dengan koma
  #         openNasabah = open('data/nasabah.txt', 'w') #buka kembali file nasabah, dengan aksi written
  #         for addReplace in getNasabah: #perulangan untuk addReplace dalam getNasabah
  #           openNasabah.writelines(addReplace)  #panggil openNasabah, lalu masukan data baris perbaris
  #         openNasabah.close() #tutup
  #         print('Setoran tunai sebesar Rp.',setoranTunai, 'ke rekening', norekNasabah, 'a/n', singleNasabah[1], 'berhasil')
  #         print('Total saldo', singleNasabah[1], 'adalah Rp.', totalSetoran)
  #         condition = False
  #         print('Tekan Enter untuk ke menu')
  #         input()
  #         index.main()
  #       else:
  #         print('Minimum setor tunai adalah Rp. 10000')
  #         pass
  #     else:
  #       pass
  #     getIndex += 1
import app.index as index
import app.bukaRekening as bukaRekening
import app.daftarTransfer as daftarTransfer
import app.setoranTunai as setoranTunai
import app.tarikTunai as tarikTunai
import app.transfer as transfer

def main(status = True, params = ''):
  print('**** SELAMAT DATANG DI NF BANK ****')
  print('MENU :')
  print('[1] Buka rekening')
  print('[2] Setoran tunai')
  print('[3] Tarik tunai')
  print('[4] Transfer')
  print('[5] Lihat daftar transfer')
  print('[6] Keluar \n')
  if status == False: print('Nomor', params, ' tidak ada di menu, silahkan coba lagi')
  try: inp = int(input('Masukan pilihan Anda : '))
  except ValueError: menu()
  pilihMenu(params = inp)

def pilihMenu(params):
  if params == 1:
    bukaRekening.main()
  elif params == 2:
    setoranTunai.main()
  elif params == 3:
    tarikTunai.main()
  elif params == 4:
    transfer.main()
  elif params == 5:
    daftarTransfer.main()
  elif params == 6:
    print('Program selesai')
    print('Terimakasih atas kunjungan Anda')
  else:
    main(False, params)
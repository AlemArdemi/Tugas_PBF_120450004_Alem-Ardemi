from spetools import encrypt

while True:
  selection = input('Apakah anda ingin melakukan enkripsi? [Y/N]')
  if selection == 'Y':
      inpass = input("Masukkan Password yang ingin dienkripsi: ")
      encrypted = encrypt(inpass)
      print('Password anda adalah : ', (encrypted))
  elif selection == 'N':
      break
  else:
      print('Invalid Input')
      continue
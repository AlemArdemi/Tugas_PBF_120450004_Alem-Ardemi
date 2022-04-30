def encrypt(psw):
  splitpass = list(psw)

  asciipass = list()
  for char in splitpass:
    asciichar = ord(char)
    asciipass.append(asciichar)

  encryptedpass = ""
  for num in asciipass:
    firstval = num//26 + 80
    secondval = num%26 + 80
    if firstval > secondval:
      thirdval = '+'
    else:
      thirdval = '-'

    encryptedpass = encryptedpass + chr(firstval) + chr(secondval) + thirdval
  return encryptedpass

def decrypt(psw):
  splitpass = [psw[i:i+3] for i in range(0, len(psw), 3)]

  asciipass = list()
  for word in splitpass:
    firstval = ord(word[0]) - 80
    secval = ord(word[1]) - 80
    val = 26 * firstval + secval
    asciipass.append(val)

  password = ''
  for i in asciipass:
    char = chr(i)
    password = password + char

  return password
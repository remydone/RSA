# -*- coding: utf-8 -*-
## Asymetric coding system

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

a = 40
b = 50
c = 60
d = 70

m = a*b - 1
e = c*m + a
f = d*m + b
n = (e*f - 1)/m
message = "banana"

def Code(n, e, message):
  coded_message = []
  for i in range(len(message)):
    letter = message[i]
    if letter.isalpha():
      for j in range(len(alphabet)):
        if alphabet[j] == letter:
          num_letter = j
      coded = e*num_letter % n
      coded_message.append(coded)
    else:
      coded_message.append(message[i])
  return coded_message

def Decode(f, coded_message):
  message = ""
  for i in range(len(coded_message)):
    coded = coded_message[i]
    if str(coded).isdigit():
      num_letter = coded_message[i]*f % n
      letter = alphabet[num_letter]
    else:
      letter = coded_message[i]
    message += letter
  return message
  
#print Decode(f, Code(n, e, message))

##########################################################################################################################

# RSA

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def PGCD(n1, n2):
  n1 = abs(n1)
  n2 = abs(n2)
  minn = min(n1, n2)
  maxn = max(n1, n2)
  if minn == 0 :
    return 1
  while (True) :
    r = maxn % minn
    if r == 0 :
      return minn
    maxn = minn
    minn = r

def GetPublicKey(p, q):
  secret = (p-1)*(q-1)
  e = 5
  n = p*q
  return [n, e]

def Diophante(pOne, pTwo, c):
  a = max(pOne, pTwo)
  b = min(pOne, pTwo)
  ac = 0
  bc = 0
  ap = 0
  bp = 1
  ase = 1
  bse = 0
  while  True:
    q = a/b
    r = a % b
    if r == 0:
      if c % b == 0:
        ap *= c/b
        bp *= c/b
        if pOne == max(pOne,pTwo):
          return [ap, bp, True]
        else:
          return [bp, ap, True]
      else:
        return [0, 0, False]
    ac = ase - q*ap
    bc = bse - q*bp
    ase = ap
    bse = bp
    ap = ac
    bp = bc
    a = b
    b = r

def GetPrivateKey(p, q):
  secret = (p-1)*(q-1)
  pub_key = GetPublicKey(p, q)
  e = pub_key[1]
  dio = Diophante(e, secret, 1)
  d = dio[0]
  if d < 0:
    d += secret
  n = pub_key[0]
  return [d, n]

def CodeRSA(n, e, message):
  coded_message = []
  for i in range(len(message)):
    letter = message[i]
    if letter.isalpha():
      for j in range(len(alphabet)):
        if alphabet[j] == letter:
          num_letter = j
      coded = num_letter**e % n
      coded_message.append(coded)
    else:
      coded_message.append(message[i])
  return coded_message

def DecodeRSA(d, n, coded_message):
  message = ""
  for i in range(len(coded_message)):
    coded = coded_message[i]
    if str(coded).isdigit():
      num_letter = coded_message[i]**d % n
      letter = alphabet[num_letter]
    else:
      letter = coded_message[i]
    message += letter
  return message

text = "j'ai reussi!"
PublicKey = GetPublicKey(29,13)
PrivateKey = GetPrivateKey(29,13)
print DecodeRSA(PrivateKey[0], PrivateKey[1], CodeRSA(PublicKey[0], PublicKey[1], text))

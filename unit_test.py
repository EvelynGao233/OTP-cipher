
from cipher import *

a = generatePad(1000)

with open("encrypted-message.txt","w") as file:
  file.write(encipher("encipherTest.txt","One_time_pad.txt"))

with open("decipherTest.txt", "w") as file:
  file.write((open("encrypted-message.txt")).read())

with open("decrypted-message.txt", "w") as file:
  file.write(decipher("decipherTest.txt","One_time_pad.txt"))



    
  


def test_generatePad():
  with open ("One_time_pad.txt") as file:
    pad = file.read()
  assert a == pad

def test_decipher():
  d = open("decipherTest.txt").read()
  d2 = open("encrypted-message.txt").read()
  assert d == d2

def test_encipher():
  e = open("encrypted-message.txt").read()
  e2 = open("decipherTest.txt").read()
  assert e == e2

  


   

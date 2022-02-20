
from cipher import *

#generate One_time_pad in size 1000to test
generated_pad = generatePad(1000)
#create txt called encipherTest
with open("encipherTest.txt", "w") as file:
  file.write("This is a test for encipher and decipher. Gook Luck! If you see this, Congratulations!")
#create encrypted-message.txt to test encipher encipherTest.txt by using One_time_pad.txt
with open("encrypted-message.txt","w") as file:
  file.write(encipher("encipherTest.txt","One_time_pad.txt"))
#use encrypted message in the encrypted-message.txt as decipherTest.txt
with open("decipherTest.txt", "w") as file:
  file.write((open("encrypted-message.txt")).read())
#create decrypted-message.txt to test decipher decipherTest.txt by using One_time_pad.txt
with open("decrypted-message.txt", "w") as file:
  file.write(decipher("decipherTest.txt","One_time_pad.txt"))


#test genereatPad
def test_generatePad():
  #save pad in One_time_pad.txt to pad, if pad equals to generated_pad at the begining, passed test
  with open ("One_time_pad.txt") as file:
    pad = file.read()
  assert generated_pad == pad
#test decipher
def test_decipher():
  #if the information in the decipherTest and decrypted-message is same , passed test
  d = open("encipherTest.txt").read()
  d2 = open("decrypted-message.txt").read()
  assert d == d2
#test encipher
def test_encipher():
  #if the information in the encipherTest and encrypted-message is same , passed test
  e = open("encrypted-message.txt").read()
  e2 = open("decipherTest.txt").read()
  assert e == e2

  


   

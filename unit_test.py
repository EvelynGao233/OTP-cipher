
from cipher import *


def test_shiftLetter_by_3():
    assert shiftLetter("a", 3) == "d"

def test_shiftLetter_by_negative_3():
    assert shiftLetter("a", -3) == "x"

def test_shiftLetter_by_3():
    assert shiftLetter("A", 3) == "D"

def test_shiftLetter_by_negative_3():
    assert shiftLetter("A", -3) == "X"

def test_randomLetter():
    assert (randomLetter() == randomLetter() and randomLetter() == randomLetter()) == False

def test_generatePad():
    assert generatePad(10) != generatePad(10)

def test_generatePadFile():
    generatePadFile("test.txt",100)
    with open("test.txt") as file:
        assert len(file.read()) == 100

def test_addPad_of_A():
    addPad("ABC","AAA") == "ABC"

def test_addPad_of_Z():
    addPad("ABC","ZZZ") == "ZAB"

def test_addPad_punctuation():
    addPad("AB!C4D","EFGHIJK") == "EG!I4K"

def test_subPad_of_A():
    addPad("ABC","AAA") == "ABC"

def test_subPad_of_Z():
    addPad("ZAB","ZZZ") == "ABC"

def test_subPad_punctuation():
    addPad("EG!I4K","EFGHIJK") == "AB!C4D"

  

message = "This is a test for encipher and decipher. Gook Luck! If you see this, Congratulations!"

with open("encrypted-message.txt","w") as file:
  file.write(encipher(message,"test.txt"))

decipher_test = open("encrypted-message.txt").read()

with open("decrypted-message.txt", "w") as file:
  file.write(decipher(decipher_test,"test.txt"))

decrypted = open("decrypted-message.txt").read()

with open("encrypted-test.txt", "w") as file:
  file.write(encipher(decrypted,"test.txt"))

def test_decipher():
  assert decrypted == message
  
def test_encipher():
  encrypted = open("encrypted-test.txt").read()
  assert encrypted == decipher_test

   


   

from random import random
import sys
import getopt

#generate random letter
def randomLetter():
    return chr(65 + int(26 * random()))
#generate pad in given size
def generatePad(size):
  pad = []
  for i in range(0, size):
    pad.append(randomLetter())
  return "".join(pad)
#generate pad in given size and save it in file filename
def generatePadFile(filename,size):
  pad = generatePad(size)
  file = open(filename,"w")
  file.write(pad)
  file.close()

#method to shift letter by number shift
def shiftLetter(char,shift):
    asc = ord(char)

    if (asc >= 65) and (asc <= 90):
        shifted = (asc - 65 + shift) % 26 + 65
    elif (asc >= 97) and (asc <= 122):
        shifted = (asc - 97 + shift) % 26 + 97
    else:
        shifted = asc
    
    return chr(shifted)

#addPad method for encipher
def addPad(message,pad):
    newMessage = []
    count = 0
    for i in range(0, len(message)):
        c = ord(message[i])
        if ((c >= 65) and (c <= 90)) or (c >= 97) and (c <= 122):
            newMessage.append(shiftLetter(message[i], ord(pad[i])))
            count += 1
        else:
            newMessage.append(message[i])
    return "".join(newMessage)

#subPad method for decipher
def subPad(message,pad):
    newMessage = []
    count = 0
    for i in range(0, len(message)):
        c = ord(message[i])
        if ((c >= 65) and (c <= 90)) or (c >= 97) and (c <= 122):
            newMessage.append(shiftLetter(message[i], -ord(pad[i])))
            count += 1
        else:
            newMessage.append(message[i])
    return "".join(newMessage)

# decipher given message with padfile
def decipher(message,padfile):
    f = open(padfile)
    pad = f.read()
    return subPad(message,pad)
#encipher given message with padfile
def encipher(message,padfile):
    f = open(padfile)
    pad = f.read()
    return addPad(message,pad)


def main(argv):
  #save input name from arg
  One_time_pad = ''
  unencryptedfile = ''
  encryptedfile = ''
  try:
    opts, args = getopt.getopt(argv,"mp:e:d:w:")
  except getopt.GetoptError:
    print('please check manual')
    sys.exit(2)
  if not opts or len(opts) >2:
    print("too many argument.")
    sys.exit(2)
  for opt,arg in opts:
    #if command is "-m", print mamual
    if opt == '-m':
      print('mamual: \n -p <size>: generate 10000 pad and store it in given file \n -e <inputfile> -w <padfile> : encrypt the <inputfile> by the <padfile> \n -d <inputfile> -w <padfile> : decipher <inputfile> by the <padfile>')
      sys.exit()
    #if command is "-p", user input int size, generate one time pad in given size and save it into "One-time-pad.txt"
    elif opt == "-p":
      generatePadFile(arg,10000)
      print("One-time-pad in size 10000 has been generated and saved in file " + arg)
      sys.exit()
    #if command is "-e", user can input filename as unencryptedfile to enciper
    elif opt == "-e":
      unencryptedfile = arg
    #if command is "-d", user can input filename as encryptedfile to decipher
    elif opt == "-d": 
      encryptedfile = arg
    #if command is "-w", with one-time-pad 
    elif opt == "-w":
      One_time_pad = arg
  #if user input file to encipher and one-time-pad, encipher the given file with One_time_pad
  if unencryptedfile and One_time_pad:
    with open(unencryptedfile) as file:
      message = file.read()
    with open("encrypted-message.txt","w") as file:
      file.write(encipher(message,One_time_pad))
    print("The message in", unencryptedfile, " has been encrypted and save to encrypted-message.txt")
  #if user input file to decipher and one-time-pad, decipher the given file with One_time_pad
  elif encryptedfile and One_time_pad:
    with open(encryptedfile) as file:
      message = file.read()
    with open("decrypted-message.txt","w") as file:
      file.write(decipher(message,One_time_pad))
    print("The message in", encryptedfile, " has been decrypted and save to decrypted-message.txt")
  #incorrect
  else:
    print("Incorrect amount of argument. Please check the manual.")

if __name__ == "__main__":
  main(sys.argv[1:])
    
    

    




    

    





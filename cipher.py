import random
import sys
import getopt
#generate one-time-pad
def generatePad(size):
#open file and use random to generate random alphabet 
  with open ("One_time_pad.txt","w") as file:
    for i in range(size):      
      file.write(chr(random.randrange(65,65+26)))

  with open ("One_time_pad.txt") as file:
    pad = file.read()
  
  return pad

# decipher
def decipher(filename,pad):

  message = open(filename, "r").read()
  pad = open(pad,"r").read()
  decipher = ""
  count = 0
#if it is alphabet, use pad to decipher, otherwise add the original index element
  for i in range (len(message)):
    if message[i].isalpha()== True:
      asc = ord(message[i])      
      asc_pad = ord(pad[count])-65      
      de_asc = asc - asc_pad
      if 64 < asc < 91:
        if de_asc < 65:
          de_asc = de_asc + 26
      else: 
        if de_asc < 97:
          de_asc = de_asc + 26        
      decipher += chr(de_asc)
      count += 1
    else:
      decipher += message[i]

  return decipher

#encipher
def encipher(filename,pad):
  message = open(filename, "r").read()
  pad = open(pad,"r").read()
  encipher = ""
  count = 0
#if it is alphabet, use pad to encipher, otherwise add the original index element
  for i in range (len(message)):
    if message[i].isalpha()== True:
      asc = ord(message[i])      
      asc_pad = ord(pad[count])-65
      en_asc = asc + asc_pad
      if 64 < asc < 91:
        if en_asc > 90:
          en_asc = en_asc - 26
      else: 
        if en_asc > 122:
          en_asc = en_asc - 26
      encipher += chr(en_asc)
      count += 1
    else:
      encipher += message[i]

  return encipher

def main(argv):
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
    if opt == '-m':
      print('mamual: \n -p <size>: generate one-time-pad in given size and store it in "One_time_pad.txt" \n -e <inputfile> -w <padfile> : encrypt the <inputfile> by the <padfile> \n -d <inputfile> -w <padfile> : decipher <inputfile> by the <padfile>')
      sys.exit()
    elif opt == "-p":
      generatePad(int(arg))
      print("One-time-pad in size", arg, " has been generated and saved in One_time_pad.txt")
      sys.exit()
    elif opt == "-e":
      unencryptedfile = arg
    elif opt == "-d":
      encryptedfile = arg
    elif opt == "-w":
      One_time_pad = arg
  if unencryptedfile and One_time_pad:
    with open("encrypted-message.txt","w") as file:
      file.write(encipher(unencryptedfile,One_time_pad))
    print("The ", unencryptedfile, " has been encrypted and save to encrypted-message.txt")
  elif encryptedfile and One_time_pad:
    with open("decrypted-message.txt","w") as file:
      file.write(decipher(encryptedfile,One_time_pad))
    print("The ", encryptedfile, " has been decrypted and save to decrypted-message.txt")
  else:
    print("Incorrect amount of argument. Please check the manual.")

if __name__ == "__main__":
  main(sys.argv[1:])
    
    

    





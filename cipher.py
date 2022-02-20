import random
import sys
import getopt

#generate one-time-pad in given size 
def generatePad(size):
#open file and use random to generate random alphabet 
  with open ("One_time_pad.txt","w") as file:
    for i in range(size):      
      file.write(chr(random.randrange(65,65+26)))

  with open ("One_time_pad.txt") as file:
    pad = file.read()
  
  return pad

# decipher given file with generated one-time-pad
def decipher(filename,pad):
  # open file, one-time-pad, read and save string 
  message = open(filename, "r").read()
  pad = open(pad,"r").read()
  decipher = ""
  count = 0
#if it is alphabet, use pad to decipher, otherwise add the original index element
  for i in range (len(message)):
    if message[i].isalpha()== True:
      #ascii number of the alphabet
      asc = ord(message[i])
      #ascii number of the pad
      asc_pad = ord(pad[count])-65
      #decipher, substract the ascii number of the pad
      de_asc = asc - asc_pad
      #if original number is uppercase and after substracting pad ascii number it becomes lower than 65,
      #add 26 to get correct decipher alphabet
      if 64 < asc < 91:
        if de_asc < 65:
          de_asc = de_asc + 26
      #if original number is lowercase and after substracting pad ascii number it becomes lower than 97,
      #add 26 to get correct decipher alphabet
      else: 
        if de_asc < 97:
          de_asc = de_asc + 26
      # use chr to get the alphabet and add to decipher
      decipher += chr(de_asc)
      #move to next alphabet in one-time-pad
      count += 1
    else:
      #not alphabet, directly add to decipher
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
      #ascii number of the alphabet
      asc = ord(message[i])
      #ascii number of the pad
      asc_pad = ord(pad[count])-65
      #encipher, add the ascii number of the pad
      en_asc = asc + asc_pad
      #if original number is uppercase and after adding pad ascii number it becomes larger than 90,
      #substract 26 to get correct encipher alphabet
      if 64 < asc < 91:
        if en_asc > 90:
          en_asc = en_asc - 26
      #if original number is lowercase and after adding pad ascii number it becomes larger than 122,
      #substract 26 to get correct encipher alphabet
      else: 
        if en_asc > 122:
          en_asc = en_asc - 26
      # use chr to get the alphabet and add to encipher
      encipher += chr(en_asc)
      #move to next alphabet in one-time-pad
      count += 1
    else:
      #not alphabet, directly add to encipher
      encipher += message[i]

  return encipher

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
      print('mamual: \n -p <size>: generate one-time-pad in given size and store it in "One_time_pad.txt" \n -e <inputfile> -w <padfile> : encrypt the <inputfile> by the <padfile> \n -d <inputfile> -w <padfile> : decipher <inputfile> by the <padfile>')
      sys.exit()
    #if command is "-p", user input int size, generate one time pad in given size and save it into "One-time-pad.txt"
    elif opt == "-p":
      generatePad(int(arg))
      print("One-time-pad in size", arg, " has been generated and saved in One_time_pad.txt")
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
    with open("encrypted-message.txt","w") as file:
      file.write(encipher(unencryptedfile,One_time_pad))
    print("The ", unencryptedfile, " has been encrypted and save to encrypted-message.txt")
  #if user input file to decipher and one-time-pad, decipher the given file with One_time_pad
  elif encryptedfile and One_time_pad:
    with open("decrypted-message.txt","w") as file:
      file.write(decipher(encryptedfile,One_time_pad))
    print("The ", encryptedfile, " has been decrypted and save to decrypted-message.txt")
  #incorrect
  else:
    print("Incorrect amount of argument. Please check the manual.")

if __name__ == "__main__":
  main(sys.argv[1:])
    
    

    





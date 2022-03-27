# Spring2022-CSC151

Instruction:

Main cipher program:

In this cipher.py, I use the method taught in the class to run the program from the command line.
Basically, I use the mode same as the given example.

"-m": shows mamual

"-p": type "-p" and name of the padfile, it will generate pad with size 10000 and save into the file you named

eg: -p "pad.txt" (generate pad.txt which contains pad of size 10000)

"-e": encipher command. Type filename you want to encipher. Use it combined with command "-w", and encipher with given pad file. Save it to encrypted-message.txt.

"-d": decipher command. Type filename you want to decipher. Use it combined with command "-w", and decipher with given pad file. Save it to decrypted-message.txt.

"-w": Type filename as pad. Use it with command "-e" or "-d"

eg: -e unencrypted.txt -w One_time_pad.txt
    -d encrypted.txt -w One_time_pad.txt
    
    
unit_test:

test each individual function contained in the main cipher.py program.

The last part of testing encipher and decipher:

Create message to test

Create "encrypted-message.txt" to save the message enciphered using "test.txt" generated before

Create "decrypted-message.txt" to test decipher "encrypted-message.txt" by using "test.txt"

Create "encrypted-test.txt" to encipher the "decrypted-message.txt" by using "test.txt"

In this case, if the message in "encrypted-test.txt" equals to message in "encrypted-message.txt", and the message in "decrypted-message.txt" equals to test message, test passed.

(The message in the "encipherTest.txt" include uppercase, lowercase, punctuation to examine the correctness of decipher and encipher)

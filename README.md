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





In the end, typing pytest to see the result of each test suite.
Generate "One_time_pad.txt" by generatePad() to use as pad and save it for later test.

Create a file called "encipherTest.txt", write message to it as test tool.

Create "encrypted-message.txt" to test encipher "encipherTest.txt" by using "One_time_pad.txt".

Use encrypted message in the "encrypted-message.txt" as "decipherTest.txt"

Create "decrypted-message.txt" to test decipher "decipherTest.txt" by using "One_time_pad.txt"

In this way, if the encipher and decipher method work, messages in the "encipherTest.txt" should be same as messages in the "decrypted-message.txt", and messages in the "decipherTest.txt" should be same as messages in the "encrypted-message.txt". Also, the pad in the "One_time_pad.txt" should be same as the result of generatePad().

If all the methods works, all the assumption above will be true and tests will pass.

(The message in the "encipherTest.txt" include uppercase, lowercase, punctuation to examine the correctness of decipher and encipher)

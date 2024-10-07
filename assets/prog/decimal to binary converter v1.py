# Program to convert a decimal number into its binary constituent bits
#

import sys

while True:
        binDigit = 128 #most significant bit in a byte

        print('')
        decNum = int(input('Enter decimal number: ')) #ask for number
        print('|128| 64| 32| 16|  8|  4|  2|  1|') #prepare display
        sys.stdout.write('| ')

        while binDigit > 0.5: #loop until we have competely broken down the decimal number

                if decNum - binDigit > -1: #we have found a binary digit
                        #print('1 |'),
                        sys.stdout.write('1 | ')
                        decNum -= binDigit
                else:
                        sys.stdout.write('0 | ')
                binDigit /= 2 #prepare to try the next bit to the right
        print('')

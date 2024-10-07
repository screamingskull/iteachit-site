
key = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 
       'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 
       'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
       'y':'-.--', 'z':'--..', 
       '.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', '--.':'g', '....':'h', 
       '..':'i', '.---':'j', '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o', '.--.':'p', 
       '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x',
       '-.--':'y', '--..':'z', 
       'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 
       'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 
       'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
       'Y':'-.--', 'Z':'--..', 
       '.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H', 
       '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', 
       '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X',
       '-.--':'Y', '--..':'Z',
       ' ':' ', '!':'!', '?':'?'}

while True:
		print('')
		myCode = input('Message to cipher: ')
		
		if myCode[0] == '-' or myCode[0] == '.':
			#Must be Morse Code
			morseLetter = ''
			
			#Print morse letter
			for position in range(0, len(myCode)):
				if myCode[position] == ' ':
					if myCode[position-1] != ' ':
						#space detected. Print morseLetter and reset.
						print(key[morseLetter]),
						morseLetter = ''
				else:
					#No space so build morseLetter
						morseLetter = morseLetter + myCode[position]
			#print final character that will otherwise be missed (skip if it is a space)
			if myCode[position] != ' ':
				print(key[morseLetter]),
				
		else: 
			#Must be alphabet
			for position in range(0, len(myCode)):
				letter = myCode[position]
				print(key[letter]),
				print(' '),



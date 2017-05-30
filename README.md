# What is this?
My first python script. Using inefficient python commands to automate the process of cracking a wifi-network. Very poorly and quickly made. I know this is quite bad and offers no additonal advantages to existing tools such as fluxion,etc, in-fact it is probably much worse, but it doesn't hurt to try, right? I made this mainly for simplicity and ease of use. It may be handy when someone less used to the aircrack-ng suite tries to use it or when someone is doing a demo.
# Requirements?
Really not much. I mean an x86/64 processor {until I port this to arm haha!} , a chipset that supports monitor-mode/packet-injection and some distro of linux that uses the apt package manager (kali/ubuntu/debian **_preferably Kali as it has drivers baked in_**). Did I mention it needs python3? I mean it should be good to go depending on the os. 
# Usage?
Usage is pretty much:
```bash
python3 aircrack-ng.py 
```
Alternatively if the file isn't executable: 
```
chmod +x new-build.py
./aircrack-ng.py
```
The rest is pretty much self explainatory.
## Upcoming
- [x] Make a basic python script
- [ ] Make and integrate similar script for reaver/other-tools
- [ ] {Ultimate} Design and build a Gtk/Qt or any type of GUI

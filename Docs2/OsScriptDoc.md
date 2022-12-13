# MacOS X and Linux Info

## Install Ubuntu 22 from a bootable usb drive from an ISO file

1. Download Rufus in  order to create a bootable disk drive
2. Download the ISO file of the version and style of Ubuntu you want
   1. <https://ubuntu.com/download/desktop>
3. Run the Rufus execute file and follow the instructions
   1. verify the SHA256 checksum
   2. May need to format HDD to convert to GPT and use UEFI (change in firmware)
      1. Can view in Computer Management & DISKPART

```bash
mbr2gpt /conver /$disk_name:0 /allowfullos
echo "$number *$ubuntu_version.iso" | shasum -a 256 --check
```

1. Restart device and edit UEFI/BIOS to edit boot order to start w/ USB
2. Follow prompts for installing Ubuntu
   1. Can elect to manually partition HDD
      1. EFI for GRUB loader (size.mb >= 35 and <= 500)
      2. ext4 mounted as "/" for root/home (most space)
      3. swap as logical partiton (size.gb >= 2*(RAM.size.gb))
         1. Don't really need swap in newer versions
         2. Make sure you have /, /boot, /home
3. Remove USB and allow device to restart
4. Navigate to GNU GRUB/GRUB2 menu (shift or esc) to adjust Linux bootloader
   1. Will vary depending on system and install location (dual boot, multi-boot, Windows MBR or GPT, etc.)
   2. edit grub, install drivers and apps

```bash
ubuntu-drivers devices
sudo gedit /etc/default/grub &
sudo update-grub
sudo ubuntu-drivers autoinstall
# or selectively update
sudo apt install $driver_name
sudo reboot
# apps
sudo apt install $app_name
```

___

## macOS X recovery info

- Hold power button down for 5-10 sec. Press power button and follow steps below, depending on the device and the mode you're trying to navigate to.
  - Intel: Cmnd + R
  - Hold shift
  - Continue holding power until startup option displays
    - choose startup disk
    - press and hold Shift while clicking "Continue in Safe Mode"
- macOS X uses local disk drive, whis is 1 or more volumes acting as a root of its own dir.
- Dir info is in Vol dir at root of local file sysstem
   1. /Volumes/Macintosh HD
   2. /Volumes/ macOS Base System
-

### Menu's

1. Time Machine
2. Reinstall OS
3. Disk Utility
4. Security
   1. change which OS's can be downloaded and allow from external source
5. startup disk settings

___

```sh
echo $BASH
/usr/bin/bash

init $PATH

. # current working dir
.. # parent dir
~ $HOME # home dir of user
ls -a -@ -l
ls -C -l

# remove dir & files
rm -r /folder/want-deleted # remove folders & content recursively
rm -rp # ignore permissions & errors
sudo rm -rf path/to/folder
su - user -c 'ls' #switch user and run cmd
mount -uw # mount with write permissions
mount -o update /
diskutil list
df -h
find / -size +50000 -print

whereis [exe,cmd]
whatis cmdname
uname -a # show system info
free -gh #show memory usage --lohi -l from /proc/meminfo
service ssh status # check service status
ssh -l username hostname
top -u ib-ub
ps -ef | more # view running processes
ps -ef grep code
kill -9 PID # killall, pkill, xkill to terminate unix process

grep -i "word" file.txt # find str in fi
find -iname "file.txt" # find fi
find /home/ib-ub -name *.md -type f

gzip file.md, gzip -d file.md # zip & unzip .gz fi
unzip fi.zip && unzip -l fi.zip #extract or view w/o unzipping fi
shutdown -h now #shutdown now or -r to restart now
cat -n /home/ib-ub/flow/work/Docs2/requirements3.txt # print file to stdout
chmod ug+rwx file.txt # change permissions of fi/dir [-R u-rwx ex. will remove access recursively]
chown ib-ub:group_name file.txt # change owner
passwd username # change password; use sudo to reset w/o old pass
man 3 free # bring up section 3 of free cmd
tail -n 10 file.txt # show last 10 lines of fi
less large_file.txt # efficient view of log fi (CTRL+F/B forward/backward 1 window)
diff -w file1.md file2.md # compare, ignore whitespace fi1 to fi2
ps top vmstat brk mmap wget, systemctl, init
```

### Disk

1. Unix systems show storage by local disks presented as a single tree descending from root dir
2. macOS X uses local disk drive, whis is 1 or more volumes acting as a root of its own dir.

### Shell command info

- ctrl + \ = Quit (SIGQUIT)
  - fquit a running instance
- open path/to/app.app
  - open an app from sh
- escape special chars:
  - prepending with \
  - wrapping it in single quotes

## PowerShell Info

___

## Mail info: Pop & iMAP

- POP setting
Server name: outlook.office365.com
Port: 995
Encryption method: TLS
IMAP setting
Server name: outlook.office365.com
Port: 993
Encryption method: TLS
SMTP setting
Server name: smtp.office365.com
Port: 587
Encryption method: STARTTLS

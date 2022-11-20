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

## Troubleshooting options

___

## Bash & Pwsh Info

```sh
# ha-ibalde@ITS-TH220-02 MINGW64 ~
echo $PATH
/c/Users/ha-ibalde/bin:/mingw64/bin:/usr/local/bin:/usr/bin:/bin:/mingw64/bin:/usr/bin:/c/Users/ha-ibalde/bin:/c/WINDOWS/system32:/c/WINDOWS:/c/WINDOWS/System32/Wbem:/c/WINDOWS/System32/WindowsPowerShell/v1.0:/c/WINDOWS/System32/OpenSSH:/c/Program Files/dotnet:/c/Users/Ibalde:/c/Users/ha-ibalde/Documents/PowerShell:/c/Users/ha-ibalde/Documents/PowerShell/Help/PowerShellGet:/c/Users/ha-ibalde/Documents/PowerShell:/c/Users/Ibalde/OneDrive - Point Park University/Ibrahima @ Point Park University:/c/Program Files/nodejs:/c/Users/ha-ibalde/AppData/Local/Microsoft/WindowsApps:/usr/bin/vendor_perl:/usr/bin/core_perl

# (.venv) ib-ub@ITS-TH220-02:moon2$
echo $PATH
/home/ib-ub/moon-ubu/moon2/.venv/bin:/home/ib-ub/.vscode-server/bin/6261075646f055b99068d3688932416f2346dd3b/bin/remote-cli:/home/ib-ub/.nvm/versions/node/v18.12.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Program Files/WindowsApps/CanonicalGroupLimited.Ubuntu20.04onWindows_2004.2022.8.0_x64__79rhkp1fndgsc:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/WINDOWS/System32/OpenSSH/:/mnt/c/Program Files/dotnet/:/mnt/c/Users/Ibalde:/mnt/c/Users/ha-ibalde/Documents/PowerShell:/mnt/c/Users/ha-ibalde/Documents/PowerShell/Help/PowerShellGet:/mnt/c/Users/ha-ibalde/Documents/PowerShell:/mnt/c/Users/Ibalde/OneDrive - Point Park University/Ibrahima @ Point Park University:/mnt/c/Users/Ibalde/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/Ibalde/AppData/Local/Programs/Microsoft VS Code/bin:/mnt/c/Users/Ibalde/AppData/Local/Programs/Git/cmd:/snap/bin

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

mount -uw # mount with write permissions
mount -o update /
diskutil list
df -h
find / -size +50000 -print
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

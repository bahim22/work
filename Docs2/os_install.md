# MacOS X and Linux Info

## Install Ubuntu 22 from a bootable usb drive => ISO file

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

### Disk

1. Unix systems show storage by local disks presented as a single tree descending from root dir
2. macOS X uses local disk drive, whis is 1 or more volumes acting as a root of its own dir.

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

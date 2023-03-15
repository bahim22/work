# MacOS, W10 and Linux Info

## Install Ubuntu 22 from a bootable usb drive => ISO file

1. Download Rufus in  order to create a bootable disk drive
2. Download the ISO file of the version and style of Ubuntu you want
   1. <[Ubuntu]> Link to download Ubuntu Desktop
3. Run the Rufus execute file and follow the instructions
   1. Verify the SHA256 checksum
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

## Convert disks in W10 cmd

```ps1
# convert disk to mbr
Diskpart
list disk
sel disk $disk_num
clean
convert gpt

# create pars on dsk
Diskpart
Create partition EFI size=1000`
offset=64
 #size = int in MB; offset = int in kb

mbr2gpt.exe /convert /allowFullOS # change an already booted MBR disk to GPT

list disk
choose disk * # the target dsk or par's num is indicated by *
list division
choose a partition
format fs=ntfs unit=64k # 4096 bytes = 4.096 kb, 4096 KB = 4 MB
```

# cluster size (allocation unit size)

- Cluster size represents the smallest amount of disk space that can be used to hold a file. When file sizes do not come out to an even multiple of the cluster size, additional space must be used to hold the file (up to the next multiple of the cluster size). On the typical hard disk partition, the average amount of space that is lost in this manner can be calculated by using the equation (cluster size)/2 * (number of files).
- The size of your allocation unit will be equal to the size of an empty file. If you have several small files but a large allocation size, every file on your drive will need to be at least this huge, which could consume a lot of space on your hard drive
- When you keep your allocation unit size small, a higher allocation time will be required, leading to a slower PC. However, it will take maximum disk space if it's too big.
- When you have different small files, it would be an amazing idea to maintain a minimum allocation size so that your hard drive space will stay manageable. On the other hand, when you possess several larger files, keeping the allocation size higher will boost the system's performance because there will be fewer blocks to aim for. However, if the allocation size is extremely big, it will consume the maximum of your PC's disk space.

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
- IMAP setting
Server name: outlook.office365.com
Port: 993
Encryption method: TLS
- SMTP setting
Server name: smtp.office365.com
Port: 587
Encryption method: STARTTLS

[Ubuntu]: https://ubuntu.com/download/desktop

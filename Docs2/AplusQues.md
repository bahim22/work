# Sample questions for Comptia A+

1. QoS = quality of service. In SOHO env, QoS set at router level. If you want to enforce it's policies on your net, you need to use a router equipped w/ QoS software
2. Consult manu docs before doing preventive maintenance, or cleaning ops to get proper methods and solvents
3. SMTP protocol can send emails from a client device (only for outgoing messages)
4. A multi-layer switch enables having both switching and routing functionality on the same device

## Network

1. If PCs can't connect to wired network due to not rec IP addresses from DHCP server the cause may be the DHCP IP pool is exhausted
2. IP addresses beginning w/ 169 are assigned auto if an IP address can't be received from a DHCP server
3. Avoid low RF signal issues by using non-overlapping channels (1,6,11)
4. CAT5 trasmits data >= 100 Mbps & distance of 100 meters
5. Crossover cable can be used to make connection from 2 hubs, 2 swtiches, 2 routers, hub to switch, or computer to router
6. Bluetooth: a discovery and authentication process that validates the communication link
7. Po

### Network Commands

1. `nslookup` cmd is used to query the DNS server to obtain a domain name or IP address mapping
2. ipconfig: checks the IP address of a system
3. netstat: displays TCP and UDP connections
4. traceert: tracks the pathway taken by a packet
5. ping: tests the reachability of a host
6. S/MIME protocol can encrypt and digitally sign e-mails
7. ipconfig /all cmd can check if PCs are getting a correct DNS IP
8. ifconfig cmd: checks a devices IP address and subnet mask on Linux OS's

## Shell info

- Available cmds for standard vs admin privilege
  - elevate (run CLI as admin to change sys)

### CMD

- ipconfig: displays config of net adapters
- ping: tests reachability of remote pc over net
- tracert: shows what network devices packet goes thru to reach remote pc
- netstat: show net stats on data transfers, ports, apps
- nslookup: resolve name to IP address for DNS TShoot

- shutdown: shut down or restart pc, w/ options/param
- command_name /?: param brings up help w/ list of cmd options/param & descriptions
- dism: Deployment image servicing & mngmnt tool => mount & service W image files
- sfc: System File checker tool, checks status/version of system files
- chkdsk: verifies FS of vol & fix logical FS corruption
- dispart: tool that manages disk, parts, vols
- taskkill: kills sys proc. given process ID # (PID)
- gpupdate: manual refresh domain grp policies applied to pc or user
- gpresult: display current group policies & status
- format: create a FS on storage device

| Cmd | desc. |
| :---: | :---: |
copy | copy >= 1 fi
xcopy | adv w/ > options
robocopy | replaces xcopy w/ > options
net use | connect/map net share
net user | manage users

## Memory

- ECC: can continue to work even if it has corrupt data
- Paging: a file that's used as virtual mmemory on the system
- RAM: short-term memory used to store working data
- Non-parity: doesn't maintain parity info and can't perform error checking.

## **Windows**

1. bootmgr prog is used to boot the OS in Windows
2. Tasklist cmd opens CLI v of task mngr
3. regsvr32 cmd used to register dynamic link library (DLL) files as cmd compos in Registry
4. Need to config objects and counters to track resource usage in Perf Monitor
5. Registry root keys are org. into subkeys & values
6. system's non-user-specific configs stored in HKEY_LOCAL_MACHINE root key of Registry
7. Component Services enables programmers to share objects between apps and computers
8. BIOS looks for the MBR, which finds the boot code to launch the OS, when booting Windows
9. open Registry Editor from cmd prompt w/ either regedit or regedt32
10. Task Manager tool used to force program closed in W10. Access via CTRL-SHIFT-ESC.
11. Task Scheduler (W mngmnt utility) allows config an app to run auto or at regular intervals
12. NTFS_FILE_SYSTEM error means that the HDD is corrupt. (may cause BSOD)
13. Win uses SMB to transfer files from one system to another

## **Users, Groups, Permissions**

1. auth thru NTFS defines res a user can access and what they're able to do
2. BitLocker Drive Encryption allows you to encrypt entire drive (files, other users dir's)
3. User Account Control (UAC) uses a consent prompt so standard users can input admin creds to complete various tasks
4. Take Ownership permission lets an admin change ownership of a file w/o knowing the user's creds
5. Copying files from an NTFS HDD to a FAT or FAT32 based partition on a USB drive creates 2 copies of the object, and the copy has no effective permissions at all
6. chmod cmd lets you change file permissions in Linux
7. In W8.1 the Settings charm lets you create a new user account based on a global MS account
8. Use Public Library to share files amongst multiple users of a single system
9. Encrypting File System (EFS) enables you to encrypt files, rendering them unviewable by other accts.

## OS maintainence and optimization

1. g
2. g

- CPU architecture were historically 8/16-bit & current 32/64-bit computers.
  - bit length refers to # of bits used for memory addresses.
  - 32 bit pc can use max memory size of 4 GB
    - 1111 1111 1111 1111 1111 1111 1111 1111 = 4,294,967,295
  - 64 bit can use 16 exabytes (18,446,744,073,709,551,616)
  - max memory supported by W10 workstation OS is 2 TB

- **Windows** is most used workstation OS for personal & corp.
  - *W7*: file mngmt via Windows Explorer, libraries showed files of specific type, even if stored in diff locations, default libs[docs, pictures, videos, music] => default location for Windows Explorer on Windows 7, Aero provided visual enhancements to desktop/GUI exp & required video card
  - *W8*: start screen (tiles for apps & sys menus) replaced start menu, Windows Store for download & purchasing software, sign-in w/ local & MS online accounts (enabled transfer appearance, sys settings btw pc's), Settings menu contained most-used user settings, Control Panel allowed more sys config, MS recommend. multi-touch display for advanced GUI interaction on tablets, [Docs, Pics, Vids, Music] become normal folders and libraries aren't enabled by default
  - *W8.1*: more refined & enhanced user interface, esp. on non-touch display PC's
  - *W10*: intro Cortana, Start menu is combo of W7 and panel similar to W8 start screen & doesn't obstruct entire screen & desktop.
- **Corp vs Personal needs**
  - Pro Editions: more efficient & secure use in corp. env. w/ add'l features.
  - domain access: registers pc on the domain & allows users to login; for conn to network domain
  - BitLocker: drive encryption utility. data on disk is encryptedd to prevent unauth access (useful for laptops that leave office env & can be lost/stolen)
  - Media Ctr: (on W7 Home Premium) player for slideshows, videos, optical drives, local net, streaming, music from files
  - BranchCache: useful in corp. env. w/ diff branch offices; creates local cache of files from file/web servers for quicker access
  - EFS: Encrypting File System; fs feat. that's config. to encrypt vol, dir, f; protects data from phyiscal attacker
  - all -v provide similar UX, w/ diff being Aero, Start menu vs. screen, Settings menu
  - diff interfaces: keyboard/mouse entry, touch screen, Cortana voice recognition

- **Mac** 2nd most used workstation OS
- **Linux** is a kernel (core of OS) that interfaces/apps can be added to (pre-config as distributions) in order to create various flavors of sys. Dist differ depending on req tasks
- f

- Windows phones are discontinued, but some tablets run full W10
- Android OS for phones/tablets, by Google, open source; most used mobile OS
- iOS only for iPhones/Pads
- Chrome OS usually on netbooks (lightweight/thin laptop for using services over internet & web browsing)
  - EOL don't get any updates, patches, tech support, app dev
  - limits on updates once unsupported can increase vulnerabilities and security risks
  - Compatibility across OS's and versions
    - apps use diff install files for similar software
    - new -v can cause issues w/ prev installed hardware & apps
- 

## Virtualization

1. PaaS is a complete cloud-based software dev. env.
2. SaaS is a cloud service that handles manage software, deployment and includes the platform and infrastructure
3. Measured service based on monitored use of resources like storage, netowrk bandwidth, CPU utilization.
4. Rapid elasticity allows computing resources to be auto allocated in response to demand
5. Resource pooling: cloud service provider provides all resources in a resource pool and gives you the option to select speciic resources
6. Hybrid cloud model: has benefits of both public and private clouds

## Hardware

1. onboard GPU uses RAM as storage medium
2. d
3. d
4. d
5. d

6. USB hub allows multiple USB devices to be connected to a PC
7. Remove USB drive correctly by clicking 'Safely Remove Hardware' icon in system tray, stopping the drive and then unplugging it.
8. AT style systems use 2 power connectors (P8 & P9) to connect to mobo. ATX uses one P1 connector.
9. inverter board: converts low volt DC power to high volt AC; lights up back-light bulb. If it's broken, LCD screen won't light up when laptop is powered, but you'll see a very dim image
10. l

### Troubleshoot

1. If pagination error is occuring and causing random **BSOD** crashes, but otherwise PC works then
   1. check for OS and hardware drivers; run CMDs to check HDD for errors and check system files; in advanced sys settings, disable auto manage paging files for all drives and set custom. Check RAM sticks and possible W10 reinstall.
2. An unset date/time may be due to drained BIOS battery; resolved by CMOS batter replacement
3. Startup repair can be used to prevent reinstalls and is designed to auto start if W10 detects issues.

## Disks

1. RAID 0 striped across drives to improve performance but w/ no redundancy
2. RAID 10 combines mirroring for data protection and striping for speed
3. SATA drive uses 15-pin connector
4. SSDs are non-volatile memory with fast performance and lower power consumption than HDD

5. Full backup: all chosen files are backed up and Archive bit is set to ON afterwards
6. Incremental backup: only edited/new files since last bakup are backedup
7. Differential backup: similar to incremental, except archive bit isn't set, which will cause the next diff backup to include files that were backed up during previous backups
8. d

### Tools

1. toner probe: 2-in-1 elec test tool that traces wires thru walls to determine which pair carried the signal induced by the tone generator
   1. used when you have access to both ends of cable at same time
2. cable tester: check a cable to verify intended connections exist and there's no uninteded ones
   1. missing intended connection: 'open'; existing unintended conn. ('short'); conn goes to wrong place ('miswired) conn has 2 faults: open to correct contact & shorted to incorrect one

# Comptia A+

- [Comptia A+](#comptia-a)

<details><summary>Table of contents</summary><p>

  - [Table of Contents](#table-of-contents)
  
  - [Network](#network)
    - [Networked Host Services](#networked-host-services)
    - [Ports](#ports)
    - [Ethernet | 802.11 wireless | Wi-Fi](#ethernet--80211-wireless--wi-fi)
    - [Network Questions](#network-questions)
  - [Shell](#shell)
    - [Network Commands](#network-commands)
    - [Cmd/Pwsh](#cmdpwsh)
    - [Bash cmds](#bash-cmds)
    - [Windows CMD](#windows-cmd)
  - [Operating Systems](#operating-systems)
    - [MacOS X](#macos-x)
    - [Windows](#windows)
    - [Users, Groups, Permissions](#users-groups-permissions)
    - [OS maintainence, optimization, general info](#os-maintainence-optimization-general-info)
  - [Virtualization](#virtualization)
  - [Hardware](#hardware)
    - [Cable Types](#cable-types)
      - [Network Cables](#network-cables)
      - [Connector types](#connector-types)
      - [Hard Drive Cables](#hard-drive-cables)
    - [RAID](#raid)
    - [Troubleshoot](#troubleshoot)
  - [Operational Procedures](#operational-procedures)
  - [Software Troubleshooting](#software-troubleshooting)
  - [Security](#security)
  - [Sample Ques](#sample-ques)

</p></details>

___

## Network

### Networked Host Services

<details>

<summary>Servers, Appliances, Ports</summary><p>

- client apps request services from server apps

<details><summary>Server Info</summary><p>

- Usually a process running in memory on networked system which sends out responses to requests made from a remote client system
  - can also be stand-alone hardware
- DNS: server that resolves hostnames to IP addresses.
  - 2 are needed for a company to host a website (1 for redundancy).
  - Hostname IP address set records are saved in zone files, and if not, they are requested from the root server (higher-level DNS server)
- DHCP: provides IP configuration information (address, subnet mast, default gateway, DNS server address) to clients, automatically. The scope determines what info is allowed to be shared with a client.
- Fileshare: (File Server) - central repo for storage, access and management of entwork files
  - NAS (network attached storage) can also be used for a file server
- Print Server: manages print requests and connects to network printers
- Mail: responsible for sending, receiving, managing emails.
  - Must run a specialized server package (Microsoft Exchange, Sendmail, Postfix, Exim) to be an actual mail server.
- Syslog: Collects info compiled through system monitoring when in a client-server model. (login events, errors, etc.)
  - messages include: facility code, severity level, logged event descriptions.
  - Made up of 3 main components: listener, database, management & filtering software.
- Web Server: listens for incoming requests, which it executes by responding w/ the requested content (text, images, video, running scripts)
  - examples: Microsoft Internet Information Services (IIS), Apache
- Authentication, Authorization & Accounting (Triple A or AAA)

</p></details>

- Internet Appliances
  - SPAM gateways
  - unified threat management (UTM)
  - load balancers
  - proxy servers

- Legacy system: systems that haven't been updated, usually due to an important app that can't run on an updated platform
- Supervisory Control and Data Acquisition (SCADA): high-level management system that controls manufacturing machines, processes, infrastructure settings, and building components.
  - type of critical legacy system category
- Embedded systems: non-computer devices that use computer technology, which can also become unable to update.
- IOT devices: internet of things device that connects to network via a central controller/coordinating device (smart devices: security devices, smart thermostats, home automation)

___

### Ports

| Protocol | IP protocol | Port Used |
| :--- | :---: | --- |
| FTP  (File Transfer Protocol) | TCP | 21 |
| SFTP  (Secure FTP) | SCTP,TCP | 22 |
| FTPS  (FTP Secure) | FTP | 443 |
| TFTP  (Trivial FTP)| UDP | 69 |
| Telnet |TCP | 23 |
| HTTP (Hyper Text Transfer Protocol) | TCP | 80 |
| HTTPS (HTTP Secure) |TCP | 443 |
| SCP (Secure Copy) SCTP, |TCP | 22 |
| SSH (Secure SHell) SCTP, |TCP| 22 |
| SMTP (Simple Mail Transfer Protocol) | TCP | 25 |
| DNS (Domain Name Service) | UDP | 53 |
| SNMP (Simple Network Management Protocol) | TCP, UDP | 161 |
| SNMP Trap (Simple Network Management Protocol Trap) | TCP, UDP| 162 |
| ISAKMP (VPN) – Internet Security Association & Key Management Protocol | UDP | 500 |
| TACACS (Terminal Access Controller Access-Control System)| TCP,UDP | 49 |
| POP3 ( Post Office Protocol version 3) | TCP | 110 |
| NNTP (Network News Transfer Protocol)| TCP | 119 |
| Kerberos | UDP | 88 |
| Syslog | TCP, UDP | 514 |
| L2TP (layer 2 tunneling protocol) | TCP | 1701 |
| PPTP (Point to point tunneling protocol) | TCP | 1723 |
| RDP (Remote Desktop Protocol) | TCP, UDP | 3389|

### Ethernet | 802.11 wireless | Wi-Fi

<details><summary> Types | Specs</summary><p>

- T568A & T568B
- `Plenum`: shielding used for any network cabling. Usually used where cables are around high heats due to its non-stick material
- IEEE 802.15.1 standard:
- Wi-Fi spec 802.11 is part of the IEEE 802 wireless networking standards, used for Wi-Fi communications. They use the ethernet protocol and carrier sense multiple access with collision avoidance (CSMA/CA) media access method. The differences in operating frequencies, theoretical maximum data speed, and throughput.
- `NFC`: near-field communication: very short range, used for contactless comms between devices (ex. contactless pay)
- `RFID`: radio-frequency identification - sends info from an RFID tag w/ identifying info by using radio signals. (ex. streamlines the inventory of tracking apps)

| `802.11 spec` | `data speed` | `throughput` |
| :---: | :---: | :---: |
| a -  5 GHz  | 54 Mbps | 120 meters |
| b -  2.4 GHz | 11 Mbps | 140 m |
| g -  2.4 GHz | 54 Mbps  | 140 m |
| n -  2.4/5 GHz|  600 Mbps | 250 m |
| ac (Wi-Fi 5) 5GHz | 6.5 Gbps | 140 m |
| ax (Wi-Fi 6) 2.4/5GHz| 9.6 Gbps | 140 m |

<details>
  <summary> Wireless range and power
  </summary>
  
  <p>

- Long-Range fixed wireless: point to point wireless tech; uses directional antennas to send or receive network signals (10-20 km)
  - `licensed`: use is granted by the FCC
  - `unlicensed`: anyone can use these frequencies (ex. 2.4-5 GHz)
    - causes interference and is susceptible to eavesdropping.
  - `power`: wireless power transfer - (WPT) transmitted via long-range fixed wireless and is generated by the transmitting station
    - sent via microwave or laser light to a receiver, that turns it back into electricity.
    - FCC regulates WPT tech in US.
</p></details>

___

<details><summary> Wi-Fi</summary><p>

- frequency of protocol refers to audio range that the tech broadcasts.
  - 2.4 GHz: relatively low, compared to 5, with greater transmission range (able to pass through objects), but has slower throughput and other devices use its open frequency range (ex. microwaves, cordless phones)
    - FCC identified 14 unique 22 MHz channels (11 in US): different freq that're used for communications between the WAP & end-user device, which are auto selected by devices, but can be manually configured.
  - 5 GHz: higher frequency with faster throughput, but shorter transmission range (signal is attenuated by objects)
    - also uses channels, but don't have to set due to the increased room in RF spectrum at this range
    - 25 defined 20 MHz channels (24 that can be used for Wi-Fi)
- Bluetooth connects devices in a short(10 m) PAN to enable communication, usually connecting peripherals (ex. headphones => laptop | phone)

- port replicator adds ports for connections to peripheral devices on laptops
- 3G cellular standards: Global System for Mobile Communication (GSM) (AT&T & T-mobile) and Code-Division Multiple Access (CDMA) (Sprint & Verizon)
- 4G
- 5G cellular connections and it's classifications
  - eMBB: Enhanced mobile broadband  for cell phone and mobile communication
  - mMTC: massive machine-type communications for sensors supporting IoT devices
  - URLLC: ultra-reliable low-latency communications for autonomous vehicles and industrial apps
- Nickel-cadmium (NiCd), lithium-ion (Li-ion), nickel-metal hydride (NiMH), and lithium-polymer (Li-poly) are all chemistry types used in batteries for laptop
- Bluetooth connection 5 steps
  - 1 enable Bluetooth, 2 enable pairing, 3 locate the pairing device, 4 enter  PIN, 5 check connection
- Commonly synchronized data: bookmarks, contacts, documents, applications, location data, email, social media data, pictures, e-books, music, videos, and passwords.
- Can utilize mobile application management (MAM) and mobile device management (MDM) to ensure mobile device security.
- Google Workspace (formerly G Suite) is a collection of applications, including Gmail, Hangouts, Docs, Sheet, etc.
- NFC: Near field Communications: tech used in mobile pay (Apple/Android Pay); short-range (2 inch) tech that enables wireless communication between two portable devices.

</p></details>

### Network Questions

1. You need to configure port forwaring on a SOHO router to host gaming server
2. If a computer can't connect to a wired network due to not receiving IP addresses from DHCP server the cause may be the DHCP IP pool is exhausted
3. IP addresses beginning w/ 169 are assigned automatically if an IP address can't be received from a DHCP server
    1. The DHCP client auto self-configures IP address & subnet mask if DHCP server isn't available by using APIPA (automatic private IP Addressing).
    1. Range from 169.254.0.1 - 169.254.255.254 & default class B subnet mask of 255.255.0.0. It then sends a broadcast to ensure that other PC's aren't using the address it chose.
4. Avoid low RF signal issues by using non-overlapping channels (1,6,11)
5. CAT5 trasmits data >= 100 Mbps at distances of 100 meters
6. Crossover cable can be used to make connection from 2 hubs, 2 swtiches, 2 routers, hub to switch, or computer to router
7. Bluetooth: a discovery and authentication process that validates the communication link
8. wake-on-LAN will allow sleeping computer to power on when job is sent
9. DHCP (Dynamic Host Config Protocol) server can auto configure parameters needed by NIC when computer first boots & enables central management of IP address allocation
10. non-shining link integrity indicator when cable is plugged in means there's no connection to rest of the LAN
11. link status indicator is small LED next to RJ45 connector that will shine when there's proper electrical conn
12. Default gateway being down won't affect LAN & it's devices; but user won't be able to access internet
13. RDP uses port 3389, which has to be pre-configured on each firewall end to allow access thru that port
    1. Remote that lets you use the GUI the user is using, not just CLI
14. SSH needs port 22 opened to allow access
15. The `MAC` (Media Access Control) address: 48-bit # (written as six 2-digit hexadecimal numbers) that uniquely ID's a device on a LAN
    1. IP address used to locate the proper network (layer 3)
    2. MAC address is used to locate the device on the local area network (layer 2)
16. `socket number` uniquely IDs one end of a communication session running on a network. A socket number shows the IP address & port number of one end of a session.
    1. ex. 66.83.10.24:443 is a socket number that shows a connection est. over HTTPS to the IP address.
17. HTTP uses port 80
18. The subnet mask that defines a full class C network is 255.255.255.0, while a full class B subnet mask would be 255.255.0.0.
19. enabling MAC filtering only allows access to devices listed in the routers filtering table
20. `RJ11/45` are common for phone lines & ethernet & use tristed pair cabling
21. `RFC1918` private address sets for IP addresses start with 192.168 (v4)
22. default gateway address is address that computer would send traffic to
    1. default gateway would be a router for SOHO network & sends traffic out to internet
23. Static address: manually assigning/entering IP address
    1. sometimes recommended in order to reserve the addresses in DHCP pool to prevent other devices from leasing the address
24. `LDAP` is successor to DAP and works w/ AD for user authentication and management within a network
25. `NAT` (Network Address Translation) enables the translation of private local network IPv4 addresses into a public addresses in order for them to connect over the Internet.
26. `DMZ` (demilitarized zone) sets up separate network that can be accessed from internet, making specific services reachable by external users, but not allowing access to remainder of network (ex. email/web/FTP servers)
27. `DSL` makes use of phone lines that already exist & are limited by dist. from central office
28. `ISDN`: integrated services digital network supports use of bearer (B) channels for sending data & D chan. for signal/control

## Shell

> Network commands, Windows CMD, Powershell, Bash

<details><summary>Network, CMD, Bash</summary><p>

### Network Commands

1. `nslookup` cmd is used to query the DNS server to obtain a domain name or IP address mapping
2. `ipconfig`: checks the IP address of a system
3. `netstat`: displays TCP and UDP connections
   1. displays current state of network connections (IP add, port #, conn state)
4. `traceert`: tracks the pathway taken by a packet
5. `ping`: tests the reachability of a host
6. `ipconfig` /all cmd can check if computers are getting a correct DNS IP
7. `ifconfig` cmd: checks a devices IP address and subnet mask on Linux OS's
8. `S/MIME` protocol can encrypt and digitally sign e-mails

> Some cmds are only available w/ admin priviledge enabled by elevating or running the CLI as admin

### Cmd/Pwsh

```ps1
nbtstat
<# Displays protocol statistics and current TCP/IP connections using NBT
(NetBIOS over TCP/IP). #>
ipconfig
# displays config of net adapters
ipconfig /all /release /renew # show full config, release or renew IPv4 addr for specified adapter
ipconfig /flushdns /registerdns displaydns # purge DNS resolver cache, refresh DCHP leases and re-register DNS names, display DNS cache contents. add 6 at end of cmd to show IPv6 instead
ipconfig /showclassid /setclassid # show/modify dhcp class IDs allowed for adapter
ping:
# tests reachability of remote computer over net
tracert
# shows what network devices packet goes thru to reach remote computer
netstat
# show network stats on data transfers, ports, apps
nslookup
# resolve name to IP address for DNS TShoot
shutdown
# shut down or restart computer, w/ options/param
command_name /?
# param brings up help w/ list of cmd options/param & descriptions
dism
# Deployment image servicing & mngmnt tool => mount & service W image files
sfc
# System File checker tool, checks status/version of system files
chkdsk
<# verifies FS of vol & fix logical FS corruption
  - system tool for verifying disk integrity; run w/ no param shows dsk status, /r locates bad sectors & tries recover lost data #>
dispart
# tool that manages disk, parts, vols
taskkill
# kills sys proc. given process ID # (PID)
gpupdate
# manual refresh domain grp policies applied to computer or user
gpresult
# display current group policies & status
format
# create a FS on storage device
```

### Bash cmds

```sh
ls -l # list dir w/ long list option for fi & dir attributes
pwd # print working dir
passwd # changes password if followed by username or of current user
apt-get # install new software packs
tar -czvf archive.tar.gzip /dir/path_to_files
# -c creates archive, -z compress, -v display process (verbose mode), -f specify filename of archive
ifconfig # interface config; displays IP info
ip addr # iproute2 toolset that replaced ifconfig
kill <pid || name> # terminate process using name or PID
```

| Cmd / Linux cmd | desc. |
| :---: | :---: |
copy | copy >= 1 fi
xcopy | adv w/ > options
robocopy | replaces xcopy w/ > options
net use | connect/map net share
net user | manage users
MD / `MKDIR` | create new dir
RD / `RMDIR` | delete dir

### Windows CMD

| Command | Description |
| :---: | :---: |
| `BCDEDIT`| Sets properties in boot database to control boot loading.|
| `CACLS` | Displays or modifies access control lists (ACLs) of files |
| `CD` | Displays the name of or changes the current directory.|
| `CHDIR`  | Displays the name of or changes the current directory.|
| `CHKDSK` | Checks a disk and displays a status report.|
| `CLS` | Clears the screen.|
| `CONVERT` | Converts FAT volumes to NTFS. Can't convert current drive |
| `COPY` | Copies one or more files to another location. |
| `DATE` | Displays or sets the date.|
| `DEL` | Deletes one or more files.|
| `DIR` | Displays a list of files and subdirectories in a directory.|
| `DISKPART`  | Displays or configures Disk Partition properties.|
| `ECHO` | Displays messages, or turns command echoing on or off.|
| `ERASE` | Deletes one or more files.|
| `FIND` | Searches for a text string in a file or files.|
| `FINDSTR`   | Searches for strings in files.|
| `FORMAT`    | Formats a disk for use with Windows.|
| `FSUTIL` | Displays or configures the file system properties.|
| `FTYPE` | Displays/modifies file types used in file ext assoc.|
| `GPRESULT`  | Displays Group Policy information for machine or user. |
| `HELP` | Provides Help information for Windows commands.|
| `ICACLS` | Display, modify, backup, or restore ACLs for files and dir.|
| `MD` | Creates a directory.|
| `MKDIR` |   Creates a directory.|
| `MKLINK` | Creates Symbolic Links & Hard Links|
| `MODE` |Configures a system device.|
| `MOVE` |     Moves one or more files from one directory to another dir.|
| `PRINT` | Prints a text file.|
| `RD` | Removes a directory.|
| `RECOVER` | Recovers readable info from a bad or defective disk.|
| `REN` | Renames a file or files.|
| `RENAME` | Renames a file or files.|
| `RMDIR` | Removes a directory.|
| `ROBOCOPY`  | Advanced utility to copy files and directory trees|
| `SCHTASKS` | Schedules commands & programs to run on a computer.|
| `SHUTDOWN`  | Allows proper local or remote shutdown of machine.|
| `SYSTEMINFO`| Displays machine specific properties and configuration.|
| `TASKLIST`  | Displays all currently running tasks including services.|
| `TASKKILL`  | Kill or stop a running process or application.|
| `TREE` | Graphically displays the dir structure of a drive or path |
| `VOL` | Displays a disk volume label and serial number.|
| `XCOPY` |   Copies files and directory trees.|

</p></details>

## Operating Systems

<details><summary>Mac, Windows, Linux + General Use</summary><p>

### MacOS X

1. **MacOS** X Time Machine requires external storage media (ext HDD or Time Capsule) & does incremental/historical backups & del oldest backups when storage fills
2. Time Machine runs: hourly for 24 hrs; daily for past month, weekly for all prev mo.
3. Disk Utility lets you run first aid, partition, erase, unmount dsk, get dsk info
4. manage updates in App Store & go to Sys Pref => Software Updates for OS Updates
5. Force Quit (Cmd+Option+Ext) to individually halt running or hung apps
6. Run terminal session by opening `Finder` then `/Apps/Utilities` dir.
7. Keychain feature in MacOS stores passwords, private keys, certs, secure notes

- **Thunderbolt cables**: 4 standards
  - 1 & 2 terminate in Mini DisplayPort connector
  - 3 & 4 termiante in USB-C connector

### Windows

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

### Users, Groups, Permissions

1. auth thru NTFS defines res a user can access and what they're able to do
2. BitLocker Drive Encryption allows you to encrypt entire drive (files, other users dir's)
3. User Account Control (UAC) uses a consent prompt so standard users can input admin creds to complete various tasks
4. Take Ownership permission lets an admin change ownership of a file w/o knowing the user's creds
5. Copying files from an NTFS HDD to a FAT or FAT32 based partition on a USB drive creates 2 copies of the object, and the copy has no effective permissions at all
6. chmod cmd lets you change file permissions in Linux
7. In W8.1 the Settings charm lets you create a new user account based on a global MS account
8. Use Public Library to share files amongst multiple users of a single system
9. Encrypting File System (EFS) enables you to encrypt files, rendering them unviewable by other accts.

### OS maintainence, optimization, general info

- CPU architecture were historically 8/16-bit & current 32/64-bit computers.
  - bit length refers to # of bits used for memory addresses.
  - 32 bit computer can use max memory size of 4 GB
    - 1111 1111 1111 1111 1111 1111 1111 1111 = 4,294,967,295
  - 64 bit can use 16 exabytes (18,446,744,073,709,551,616)
  - max memory supported by W10 workstation OS is 2 TB

- **Windows** is most used workstation OS for personal & corp.
  - *W7*: file mngmt via Windows Explorer, libraries showed files of specific type, even if stored in diff locations, default libs(docs, pictures, videos, music) => default location for Windows Explorer on Windows 7, Aero provided visual enhancements to desktop/GUI exp & required video card
  - *W8*: start screen (tiles for apps & sys menus) replaced start menu, Windows Store for download & purchasing software, sign-in w/ local & MS online accounts (enabled transfer appearance, sys settings btw computer's), Settings menu contained most-used user settings, Control Panel allowed more sys config, MS recommend. multi-touch display for advanced GUI interaction on tablets, (Docs, Pics, Vids, Music) become normal folders and libraries aren't enabled by default
  - *W8.1*: more refined & enhanced user interface, esp. on non-touch display computer's
  - *W10*: intro Cortana, Start menu is combo of W7 and panel similar to W8 start screen & doesn't obstruct entire screen & desktop.
- **Corp vs Personal needs**
  - Pro Editions: more efficient & secure use in corp. env. w/ add'l features.
  - domain access: registers computer on the domain & allows users to login; for conn to network domain
  - BitLocker: drive encryption utility. data on disk is encryptedd to prevent unauth access (useful for laptops that leave office env & can be lost/stolen)
  - Media Ctr: (on W7 Home Premium) player for slideshows, videos, optical drives, local net, streaming, music from files
  - BranchCache: useful in corp. env. w/ diff branch offices; creates local cache of files from file/web servers for quicker access
  - EFS: Encrypting File System; fs feat. that's config. to encrypt vol, dir, fi
    - protects data from phyiscal attacker
  - all -v provide similar UX, w/ diff being Aero, Start menu vs. screen, Settings menu
  - diff interfaces: keyboard/mouse entry, touch screen, Cortana voice recognition

- **Mac** 2nd most used workstation OS
- **Linux** is a kernel (core of OS) that interfaces/apps can be added to (pre-config as distributions) in order to create various flavors of sys. Dist differ depending on req tasks

- Windows phones are discontinued, but some tablets run full W10
- Android OS for phones/tablets, by Google, open source; most used mobile OS
- iOS only for iPhones/Pads
- Chrome OS usually on netbooks (lightweight/thin laptop for using services over internet & web browsing)
  - EOL don't get any updates, patches, tech support, app dev
  - limits on updates once unsupported can increase vulnerabilities and security risks
  - Compatibility across OS's and versions
    - apps use diff install files for similar software
    - new -v can cause issues w/ prev installed hardware & apps
- GPS nav system that uses satellites to get pinpoint position has 3 primary compoonents
  - satellite constellation, ground control network, and receiver
- The reference guide is updated by the preferred roaming list (PRL) updates. These updates ensure mobile devices connect to the correct cell phone tower when roaming

</p></details>

## Virtualization

1. **PaaS** is a complete cloud-based software dev. env.
2. **SaaS** is a cloud service that handles manage software, deployment and includes the platform and infrastructure
3. Measured service based on monitored use of resources like storage, netowrk bandwidth, CPU utilization.
4. Rapid elasticity allows computing resources to be auto allocated in response to demand
5. Resource pooling: cloud service provider provides all resources in a resource pool and gives you the option to select speciic resources
6. Hybrid cloud model: has benefits of both public and private clouds

## Hardware

1. onboard GPU uses RAM as storage medium
2. USB hub allows multiple USB devices to be connected to a computer
3. Remove USB drive correctly by clicking 'Safely Remove Hardware' icon in system tray, stopping the drive and then unplugging it.
4. AT style systems use 2 power connectors (P8 & P9) to connect to mobo. ATX uses one P1 connector.
5. inverter board: converts low volt DC power to high volt AC; lights up back-light bulb. If it's broken, LCD screen won't light up when laptop is powered, but you'll see a very dim image

### Cable Types

#### Network Cables

- 3 primary types: **coaxial**, **twisted pair**, **fiber**
- used for connecting devices to networking equipment
- cable: medium (usually copper) where the data is transferred from devices
  - composed of four pairs of twisted-pairs (8 total) individual cables in one sheath

| Cat Cables | | |
| :---: | --- | --- |
| Name | Speed | Distance |
| 5 | 100 Mbps | 100 m |
| 5e | 1000 Mbps (1Gbps) | 100 m |
| 6 | 10 Gbps | 55 m |
| 6a | 10 Gbps | 100 m |
| 7, 8, 9 + | => | => |

1. 5e has less interference due to separation of the four twisted pairs sets & increase in number of twists in each cable pairs
2. **Coaxial cable**: single copper-cored cable contained in an inner insulation layer, which is contained in a wire mesh conductor, then placed w/in an outer insulation layer. Specification by the RG system (Radio Guide)
   1. RG-6: solid copper core used for satellite/cable modems
   2. RG-59: solid copper core used for cable TV
3. **Twisted copper pair**: pairs of individual wires twisted into pairs and then twisted together, contained w/in an insulated jacket
   1. unshielded twisted pair (UTP): 2-4 pairs of twisted wires, where the pairs are twisted in direct contact w/ each other and contained w/in an insulating layer so the copper doesn't directly touch the other copper wire
   2. shielded twisted pair (STP): 2-4 twisted wires, and each pair is contained in a braided foil sheathing layer, prior to being twisted w/ the other cable pairs, which reduces electrical interference. (used in Cat 7-8 cables)
   3. Color coded for reference:
      1. T568A (green/white, green, orange/white, blue, blue/white, orange, brown/white, brown) & T568B (orange/white, orange, green/white, blue, blue/white, brown)
         1. standards for RJ-45 wiring connectors
4. Direct burial is where the cables are buried underground and should contain STP cables w/ add'l waterproof sheathing. Should be 6-8 inch underground in protective PVC piping and away from other lines that have electrical currents
5. Plenum: teflon type covering used in cables exposed to heat or that may release gasses into vent system.
6. Optical is a transmission method that uses light pulses to transfer data
7. **Fiber optic cables**: fiber (small strings of flexible glass) is surrounded by rubberized coating w/ transmission speeds of 100 Mbps - 10 Gbps over several miles. (optical data transmission)
   1. immune to electrical interference & wiretapping
   2. Two types: *single-mode*: carries one light path, sourced from a laser (much longer distance than multi) and *multimode*: carries multiple light paths sourced by an LED.

#### Connector types

- installed at terminating pt. of cable; allows components & peripherals to connect; type used depends on the cable and what receptable it needs connected to.

1. RJ11: registered jack; telecomm net interface standard for voice/data equipment connection to service providers/carriers.
   1. used w/ twisted pair cables & connects 4-6 wires to phone lines or modems
2. RJ45: ethernet cable
3. F-type: F connector; used w/ coaxial cables for cable/satellite data connections
4. Fiber optic cable connectors
   1. ST: straight tip; bayonet style
   2. SC:subscriber connector; push/pull style
   3. LC: lucent connector; push/pull; half the size of the SC; good fit for office/data center usage
5. Punchdown block: elec connection device that inserts multiple copper wires into a slot for added insulation and electrical connection to attached wires.
6. USB: universal serial bus (attach peripheral devices to computing devices) (Peripheral cable)
   1. 2.0 standard has max speed of 480 Mbps (hi-speed) & 3.0 has max speed of 5 Gbps (Supper Speed)
   2. `Micro` (smallest) & `Mini` (2nd smallest) direction dependent connectors containing 5 pins
   3. `USB-C`: most recent connector type w/ 24 pins, an oval shape, and capable of reversible connection
7. Molex: older interconnection type for drive connections that used a two-piece pin & socket
8. Lightning Port: Apple proprietary connector featuring 8 pins and reversible orientation
9. DB9: Used for serial connections to network device consoles & management ports. 9 pins (2 rows of 4 & 5 pins),trapezoid shaped connector
   1. serial cable used for serial comms w/ a matching serial connector at the end

#### Hard Drive Cables

- Connections (drive interfaces), can be on or off-board and are used to connect internal components to mobo
- attachment standard depends on HDD requirements and features circuitry and a header (port)

1. SATA: serial advanced tech attachment
   1. most common and features a flat, internal cable that has a terminating connector that only fits the mobo connection port in one way.
   2. data cable: 7 pins, power cable: 15 pins
   3. revisions = {'1.0': '1.5Gbps', '2.0': '3Gbps','3.0': '6Gbps', '3.2': '16Gbps'}
2. SCSI: small computer system interface: hard drive connector (usually for storage device connection)
   1. ribbon cables or round cables w/ 50, 68, or 80 wires
   2. One SCSI cable is able to connect up to 16 devices (including MoBo & SCSI controller card)
3. eSATA: external SATA cable, used for data transmission (doesn't provide power)
   1. Power over eSATA, eSATA+, eSATAp, eSATA/USB versions provide power
4. IDE: Integrated drive electronics cables (PATA, parallel advanced tech attachment)
   1. 40-pin flat data cables w/ colored strip on one edge to show the location of pin 1
   2. composed of 3 separate connectors, 2 for drives and 1 for power

### RAID

1. RAID 0 striped across drives to improve performance but w/ no redundancy
2. RAID 10 combines mirroring for data protection and striping for speed
   1. provides full redundancy via mirroring and stripping all info stored w/in the drives
   2. requires atleast 4 drives
3. SATA drive uses 15-pin connector
4. SSDs are non-volatile memory with fast performance and lower power consumption than HDD
5. `Backup Types`
   1. Full backup: all chosen files are backed up and Archive bit is set to ON afterwards
   2. Incremental backup: only edited/new files since last bakup are backed up
   3. Differential backup: similar to incremental, except archive bit isn't set, which will cause the next diff backup to include files that were backed up during previous backups
6. `Blu-ray discs` can be single or multiple-use and split into categories based on 3 factors
   1. Functionality: BD-R single use, BD-RE/RW multi-use (RE-recordable erasable is newer)
   2. Capacity: BD-SL(25gb), DL(50gb), BD-XL = TL(100gb) & QL(128gb)
   3. Content quality: regular(1080p high def vid) and ultra HD(4k ultra HD, better colour depth; region-free, but need 4k Blu-R player)

### Troubleshoot

1. If pagination error is occuring and causing random **BSOD** crashes, but otherwise computer works then
   1. check for OS and hardware drivers; run CMDs to check HDD for errors and check system files; in advanced sys settings, disable auto manage paging files for all drives and set custom. Check RAM sticks and possible W10 reinstall.
2. An unset date/time may be due to drained BIOS battery; resolved by CMOS batter replacement
3. Startup repair can be used to prevent reinstalls and is designed to auto start if W10 detects issues.

## Operational Procedures

- grounding diverts excess electrical charges from the device and can decrease chance of damage from electrical spike
- ESD mats/straps lower risk of ESD by balancing the static electricity between the tech and device/component

## Software Troubleshooting

1. NIC allows for wireless comms between laptop and wireless access points.
2. physical privacy and sec comp are designed to prevent the loss of info thru physical means such as shoulder sufting/theft

## Security

1. Adware: malicious software that displays advertising banners when run
2. Malware removal
   1. identify and research malware symptoms
   2. quarantine infected system
   3. disable system restore
   4. remediate infected ssytems
   5. schedule scans and run updates
   6. enable system restore
   7. educate end-user

## Sample Ques

1. QoS = quality of service. In a SOHO env, QoS set at router level. If you want to enforce it's policies on your network, you need to use a router equipped w/ QoS software
2. Consult manual docs before doing preventive maintenance, or cleaning operations to get proper methods and solvents
3. SMTP protocol can send emails from a client device (only for outgoing messages)
4. A multi-layer switch enables having both switching and routing functionality on the same device
5. ST is a type of fiber connector
6. Port 443 (HTTPS) used when using SSL encryption to access a website
7. Light emitting diode and in-plane switching monitor technology have widest viewing angle w/ rich color & consistent backlighting
8. Enable device pairing to use hands-free for a smartphone to car
9. Can connect a tone generator to an RJ-45 drop to locate the position of the cable on a patch panel
10. Check case for overheating and mobo for swollen capacitors if computer reboots at random intervals multiple times/day
11. check fuser if printer is smudging toner on the paper after printing
12. computer may have incorrect drivers installed if print jobs are printed as garbled text
13. Startup tab in Task Manager utility shows proccesses. initialized at startup
    1. earlier Windows versions used MSConfig
14. Disk cleanup utility deletes temp fi from HDD
15. `WinRE` helps recover a sys that won't boot. It auto starts and can be manually started via Windows Recovery settings in Advanced startup menu


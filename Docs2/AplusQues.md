# Comptia A+

## Sample Ques

1. QoS = quality of service. In SOHO env, QoS set at router level. If you want to enforce it's policies on your net, you need to use a router equipped w/ QoS software
2. Consult manu docs before doing preventive maintenance, or cleaning ops to get proper methods and solvents
3. SMTP protocol can send emails from a client device (only for outgoing messages)
4. A multi-layer switch enables having both switching and routing functionality on the same device
5. ST is a type of fiber connector
6. port 443 used when using SSL encrypt. to access a website
7. Light emitting diode and in-plane switching monitor tech have widest viewing angle w/ rich color & consistent backlighting
8. enable device pairing to use hands-free for a smartphone to car
9. Can connect a tone generator to an RJ-45 drop to locate the position of the cable on a patch panel
10. check case for overheating and mobo for swollen capacitors if computer reboots at random intervals multiple times/day
11. check fuser if printer is smudging toner on the paper after printing
12. computer may have incorrect drivers installed if print jobs are printed as garbled text
13. Startup tab in Task Mngr utility shows proc. init at startup
    1. (earlier Windows versions used MSConfig)
14. disk cleanup utility deletes temp fi from HDD
15. `WinRE` helps recover a sys that won't boot. It auto starts and can be manually started via Windows Recovery settings in Advanced startup menu
16. need to configure port forwaring on a SOHO router to host gaming server

## MacOS X

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

## Network

1. If computer can't connect to wired network due to not rec IP addresses from DHCP server the cause may be the DHCP IP pool is exhausted
2. IP addresses beginning w/ 169 are assigned auto if an IP address can't be received from a DHCP server
   1. "system will assign itself an APIPA address in the range of 169.254.0.1 through 169.254.255.254, then sends a broadcast to ensure no other computer is currently using that add"
3. Avoid low RF signal issues by using non-overlapping channels (1,6,11)
4. CAT5 trasmits data >= 100 Mbps & distance of 100 meters
5. Crossover cable can be used to make connection from 2 hubs, 2 swtiches, 2 routers, hub to switch, or computer to router
6. Bluetooth: a discovery and authentication process that validates the communication link
7. wake-on-LAN will allow sleeping computer to power on when job is sent
8. DHCP(Dynamic Host Config Protocol) server can auto config param needed by NIC when computer first boots & enables central management of IP address allocation
9. non-shining link integrity indicator when cable is plugged in means there's no connection to rest of the LAN
   1. link status indicator is small LED next to RJ45 connector that will shine when there's proper electrical conn
10. Default gateway being down won't affect LAN & it's devices; but user won't be able to access internet
11. RDP uses port 3389, which has to be config on each firewall end to allow access thru that port. Remote that lets you use the GUI the user is using, not just CLI
12. SSH needs port 22 opened to allow access
13. The `MAC` (Media Access Control) address: 48-bit # (written as six 2-digit hexadecimal numbers) that uniquely ID's a device on a local area network
    1. IP address is used to locate the proper network (layer 3)
    2. MAC address is used to locate the device on the local area network (layer 2)
14. `socket number` uniquely IDs one end of a communication session running on a network. A socket number shows the IP address & port number of one end of a session.
    1. ex. 66.83.10.24:443 is a socket number that shows a connection est. over HTTPS to the IP address.
15. HTTP uses port 80
16. The subnet mask that defines a full class C network is 255.255.255.0, while a full class B subnet mask would be 255.255.0.0.
17. enabling MAC filtering only allows devices listed in routers filtering table access
18. `RJ11/45` are common for phone lines & ethernet & use tristed pair cabling
19. RFC1918 private address sets for IP addresses start w/ 192.168 (v4)
20. default gateway address is add that computer would send traffic to
    1. default gateway would be a router for SOHO net & sends traffic out to internet.
21. Static address: manually assigning/entering IP address. recomm to reserve the add in DHCP pool to prevent from being leased again on diff device
22. `LDAP` is successor to DAP and works w/ AD for user auth and mngmnt w/in a network
23. "`NAT` (Network Address Translation) allows our private local network IPv4 addresses to be translated into a public IP address capable of connecting over the Internet."
24. `DMZ` (demilitarized zone) sets up separate network that can be accessed from internet, making specific services reachable by external users, but not allowing access to remainder of network (ex. email/web/FTP servers)
25. `DSL` makes use of phone lines that already exist & are limited by dist. from central office
26. `ISDN`: integrated services digital network supports use of bearer (B) channels for sending data & D chan. for signal/control

- a `repeater` re-sends wireless signal to areas that the access point can't cover.
- A Layer 3 switch is config to participate in routing decisions
  - routing decisions work on Layer 3 of OSI model (network layer)
  - standard switches usually refferred at as Layer 2 devices, working as PnP w/o ability to adjust settings (aka unmanaged switch)
- A `crimper` is used to crimp a connector (usually last step in making an ethernet cable) to tighten the wiring to right spots in connector so electrical signals pass thru properly.
- Plug `tone generator` at jack end of cable and wave toner probe around suspected area to find other end of cable

### Ethernet, 802.11 wireless standards, ecryption info

- b/g operate at 2.4 GHz
- n operates at either 2.4 or 5 GHz with max speed of 600 Mbps

- T568A & T568B
- **Plenum**: shielding used for any network cabling. Usually used where cables are around high heats due to its non-stick material

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

## Shell info

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

#### Bash cmds

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

## Memory

- ECC: can continue to work even if it has corrupt data
- Paging: a file that's used as virtual mmemory on the system
- RAM: short-term memory used to store working data
- Non-parity: doesn't maintain parity info and can't perform error checking.

## Operating Systems

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

## OS maintainence, optimization, general info

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
- GPS nav system that uses satellites to get pinpoint position has 3 primary compoonents
  - satellite constellation, ground control network, and receiver
- The reference guide is updated by the preferred roaming list (PRL) updates. These updates ensure mobile devices connect to the correct cell phone tower when roaming

## Mobile

- **OLED**: structure provides flexibility for curved displays
  - contain the image producing components and light source in one panel. organic light emitting compound is set between an anode and cathode producing a current. the current runs thru the electroluminescent compund producing light consumes less power than LCD, with higher contrast ratio resulting in sharper images. common in high end monitors and phones.
- **LCD**: liquid crystal displays: shines a backlight through liquid crystals, creating the image on the screen
- **IPS** In plan switching, offers the widest viewing angle and the best color reproduction. ideal for vertical mounting and those needing high quality color (graphic/video artists)
- **twisted nematic**: TN, oldest LCD tech, limited viewing angles and washed out/blended color reproduction. minimal lag time makes them ideal for gamers and are inexpensive options for office use
- vertical alighnment (VA), offers best contrast ratio of the three technologies and is solid middle ground choice with decent color reproduction w/ slight lag
- The inverter is located behind the LCD panel and converts DC current into AC current
  - flickering/dim screen may be due to faulty inverter
- NFC: Near field Comms: tech used in mobile pay (Apple/Android Pay); short-range (2 in) tech wirelessly comm, allowing two portable deives to comm.
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
- mobile application management (MAM) and mobile device management (MDM) to ensure mobile device security.
- Google Workspace (formerly G Suite) collection of applications, including Gmail, Hangouts, Docs, Sheet, etc.

## Virtualization

1. PaaS is a complete cloud-based software dev. env.
2. SaaS is a cloud service that handles manage software, deployment and includes the platform and infrastructure
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
6. v

### Laser, Thermal, Ink Printers

- Steps for laser printing:
  - process, clean, charge, expose, dev, tran, fuse

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
| --- | --- | --- |

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

#### Display: Video Cables

1. **VGA**: video graphics array: legacy cable; only transmits analog signal; blue
2. **DVI** digital visual interface: addressed analog video transmission issues. Able to transmit digital video signals to display units
   1. 3 standards: DVI-A analog only, D digital only, I: analog & digital; white
3. **HDMI**: high-def multimedia interface: higher motion-picture fram rates and digital audio w/ single cable.
   1. Common connector type: Standard A HDMI (19 pins)
4. **DisplayPort**: DP: uses less power and is backward compatible w/ VGA & DVI. transmits video & audio signals.
   1. DP standard features 2 hooks to lock the cable in place
   2. Can use adaptors to convert one type of connection/cable tech to a different one

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

### Troubleshoot

1. If pagination error is occuring and causing random **BSOD** crashes, but otherwise computer works then
   1. check for OS and hardware drivers; run CMDs to check HDD for errors and check system files; in advanced sys settings, disable auto manage paging files for all drives and set custom. Check RAM sticks and possible W10 reinstall.
2. An unset date/time may be due to drained BIOS battery; resolved by CMOS batter replacement
3. Startup repair can be used to prevent reinstalls and is designed to auto start if W10 detects issues.

## Disks

1. RAID 0 striped across drives to improve performance but w/ no redundancy
2. RAID 10 combines mirroring for data protection and striping for speed
   1. provides full redundancy via mirroring and stripping all info stored w/in the drives
   2. requires atleast 4 drives
3. SATA drive uses 15-pin connector
4. SSDs are non-volatile memory with fast performance and lower power consumption than HDD
5. Full backup: all chosen files are backed up and Archive bit is set to ON afterwards
6. Incremental backup: only edited/new files since last bakup are backedup
7. Differential backup: similar to incremental, except archive bit isn't set, which will cause the next diff backup to include files that were backed up during previous backups
8. d
9. Blu-ray discs can be single or multiple-use and split into categories based on 3 factors
   1. functionality: BD-R single use, BD-RE/RW multi-use (RE-recordable erasable is newer)
   2. Capacity: BD-SL(25gb), DL(50gb), BD-XL = TL(100gb) & QL(128gb)
   3. content quality: regular(1080p high def vid) and ultra HD(4k ultra HD, better colour depth; region-free, but need 4k Blu-R player)
10. d

### Tools

1. toner probe: 2-in-1 elec test tool that traces wires thru walls to determine which pair carried the signal induced by the tone generator
   1. used when you have access to both ends of cable at same time
2. cable tester: check a cable to verify intended connections exist and there's no uninteded ones
   1. missing intended connection: 'open'; existing unintended conn. ('short'); conn goes to wrong place ('miswired) conn has 2 faults: open to correct contact & shorted to incorrect one

### Operational Procedures

- grounding diverts excess electrical charges from the device and can decrease chance of damage from electrical spike
- ESD mats/straps lower risk of ESD by balancing the static electricity between the tech and device/component
- f

## Software Troubleshooting

1. NIC allows for wireless comms between laptop and wireless access points.
2. physical privacy and sec comp are designed to prevent the loss of info thru physical means such as shoulder sufting/theft
3. d
4. d
5. d
6. d

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
3. d
4. d
5. d
6. d

<!-- /* cspell: enableCompoundWords */ -->
<!-- cSpell:ignoreRegExp /[^\s]{40,}/  -->

# A+ Practice & Notes 4

# Table of Contents

- [A+ Practice \& Notes 4](#a-practice--notes-4)
- [Table of Contents](#table-of-contents)
  - [Sections 220-1101](#sections-220-1101)
  - [Hardware 1101](#hardware-1101)
    - [Network hardware](#network-hardware)
    - [Peripheral Cables](#peripheral-cables)
  - [Mobile Devices 1101](#mobile-devices-1101)
  - [Hardware \& Network Troubleshooting 1101](#hardware--network-troubleshooting-1101)
  - [Backup and Recovery](#backup-and-recovery)
  - [Virtualization \& Cloud Computing 1101](#virtualization--cloud-computing-1101)
  - [Networking 1101](#networking-1101)
  - [Sections 220-1102](#sections-220-1102)
  - [Security 1102](#security-1102)
  - [Operating System 1102](#operating-system-1102)
    - [OS Install, maintenance, overall information](#os-install-maintenance-overall-information)
    - [Windows](#windows)
    - [macOS, Linux, Mobile](#macos-linux-mobile)
  - [Software Troubleshooting 1102](#software-troubleshooting-1102)
  - [Operational Procedures 1102](#operational-procedures-1102)
    - [Safety and Professionalism 1102](#safety-and-professionalism-1102)
  - [References and Resources](#references-and-resources)

## Sections 220-1101

- **Hardware**
  - cabling
  - connectors
  - RAM
  - storage devices
  - motherboard
  - BIOS
  - CPU
  - PSU
  - printer

- **Devices**
  - Laptop
  - Display devices
  - mobile devices
  - printers

- **Cloud**
  - Cloud computing
  - virtualization
  - troubleshooting methodology

- **Network**
  - protocols
  - TCP & UDP Ports
  - IP Addressing
  - internet connection types
  - services
  - wireless
  - hardware
  - types
  - tools

----------

## Hardware 1101

### Network hardware

**Cable Types**

1. Three primary types include _coaxial_, _twisted pair_, and _fiber_
   1. Network cables connect devices to networking equipment and the cable is the medium used to transfer data between devices.
2. twisted pair copper cabling: balanced pair operations: the twist keeps a single wire moving away from the interference and the opposite signals are compared on the other end. Each pair in same cable also have different twist rates
   1. two wires with equal and opposite signals
      1. transmit+, transmit- / receive+, receive-
3. Ethernet standards:
   1. 1000BASE-T: min of CAT-5 at max distance of 100 m and max of CAT 5E at 100 m
   2. 10GBASE-T: min of CAT 6 at 55 m (unshielded) and 100 m (shielded). Max of CAT 6A at max distance of 100 meters
4. Coaxial calbes: 2 or more forms share common axis. RG-6 used in TV/digital cable, and high-speed internet over cable
   1. wire conductor surrounded by dielectric insulator, then metal shielding and plastic jacket on outside.
5. Drop ceilings have ducts that suppply cold air and remove warm air, that's pushed to the air conditioner (with non-circulating air between the ducts). Alternatively, it can have a plenum that forces cold air in, and the pushed warm air (forced-air return) into a shared area where network cables are.
   1. Plenums cables need coated with special material (making them less flexible with a different bend radius) due to concerns of smoke and toxic fumes during a fire.
   2. Traditional cable jackets are PVC polyvinyl chloride, while fire-rated use flourinated ethylene polymer (FEP), or low-smoke polyvinyl chloride (PVC).
6. Most calbes use UTP, unshielded twisted pair with no additional shielding and most common. STP have more shielding which helps against interference. They can shield each pair or the whole cable, and requires the cable to be grounded. U unshielded, S braided, F foil shielding
   1. ex. abbrev. overall cable / individual pairs S/FTP.
7. Direct burial (STP) are designed to be outside, underground, waterproof, and possibly filled with gel to repel water. Usually are STP which adds strength, provides grounding and strength. May not need to be incased in a conduit.
8. Fiber communication is data transmitted via light and are hard to monitor/tap due to having no RF signal and being immune to radio interference. The signal can go long distances and are slow to degrade.
9. LED sends light ray to receiver, and are surrounded by a high reflective index Core, covered by low reflective index cladding, with an outer edge of mechanical protection buffer coating.
10. Fiber core surrounded by a Ferrule (large ceramic protector at the end of cable).
11. multimode fiber used for short-range communication (up to 2 km), cheaper light source. multiple reflections are bounced through the core and collected on other end.
12. Single-mode can go longer ranges (100km) and uses expensive light source such as lasers, and has a more narrow reflection.
13. Twisted pair wires use color coding as standards to ensure proper referencing. It's used with RJ-45 wiring connectors.
    1. T568A: green/white, green, orange/white, blue, blue/white, orange, brown/white, and brown
    2. T568B: orange/white, orange, green/white, blue, blue/white, green, brown/white, and brown

### Peripheral Cables

1. g
2. f
3. f

**Memory**

**Storage**

**Motherboard**

- d
- g

----------

- Computers are composed of the hardware, OS and Applications
- Computing process stages: Input, processing, output
  - modern PC's also have stages for Data storage and network connection

## Mobile Devices 1101

- battery usually made of: nickel-cadmium, nickel-metal hydride, lithium-ion, lithium-polymer
  - (Li-ion & LiPo are newer & used in modern devices)
- Fn key helps overcome small keyboard sizes. Difficult to replace integrated GPU.
- SO-DIMM is most common memory module form factor
  - use magnetic disks and SSDs for internal data storage device type
  - 2.5 inch HDD form factors
  - 1.8 & 2.5 inch SSD form factors
  - M.2
  - located in bottom of clamshell
  - 200-pin DDr & DDR2, 204-pin DDR3, 260-pin DDR4, 262-pin DDR5
- Laptop cards:
  - WLAN expansion card allows communications in 802.11 networks
  - WPAN: bluetooth module
  - NFC tech enables data transfer and authentication for laptops and other devices within range
  - Wi-Fi antenna is located near the top, inside display case
- mobile device accessories enable enhanced UI and feature touch pens, headsets, drawing pads, webcams, etc.
- LCD display tech is common in modern laptops. LED (backlight display tech) is also common.
- the inverter convets DC power into AC power and supplies voltage to backlights in older LCD panels
- docking stations usually work with specific laptop make and models (proprietary design) and offer additional ports & capabilities compared to port replicators
  - allows conenctin of laptop to an increased bank of expansion capabilities
  - ex. ports, drive bays, expansion bus slots, memory card slots, optical drives
- port replicator: peripheral device that connects a laptop to additional ports, ex. ones on mobile devices.
  - used to connect keyboards, mouse, printers etc.
  - allows for the continual connection of peripheral devices, that you can use whenever the mobile device is connected
- `digitizer` is a device that takes analog input in the form of written or drawn content, such as by a finger or stylus, and converts it into digital images (touchscreen)
  - input device that translates analog data into format that a pc can process. It's part of a mobile devices screen that enables controlling the device w/ stylus, touchpen, finger
- `inverter`: small circuit board behind LCD panel that converts DC current into AC current
- top part of the clamshell include the backlight, inverter (for LCDs), screen, digitizer, webcam, mic and Wi-Fi antenna (connected to mobo by a wire running through the top to bottom of clamshell)
- mobile display units:
  - `LCD`: liquid crystal display: uses a current passed through a semi-crystalline liquid to create images. The crystals can't make the light and require the backlight (lightsource) to display images.
    - `IPS`: In-plane switching - has widest viewing angle and best color reproduction. Ideal for graphic/video artists and good for vertical mounting.
    - `TN`: twisted nematic - oldest LCD tech. color reproduction is washed/blended with limited viewing angles, but has minimal lag time and is a cheap option for offices & gamers.
    - `VAs`: Vertical alignment - has best contrast ratio, with decent color repro. & minimal lag.
    - IPS = high color quality, wide viewing angles, slow response time
    - TN = low color quality, low viewing angles, fast response time
    - Va = high contrast ratios, good color and viewing angles
    - OLED = no backlight, lowerlight output (brightness), better contrast and color than LCD
  - `OLED`: organic light-emitting diode: displays with both the image-producing components and light source within a single panel.
- burn-in occurs when a screen shows discoloration from displaying the same image for long periods of time
- dead pixels are small spots on LCD monitors that remain black
- dim displays can signify issues with LCD backlight or inverter.

1. Mobile Device management (`MDM`) and Mobile Application management (`MAM`): allows businesses to secure mobile devices
   1. uses the MDM software to enroll corp devices into security policies and allow remote tracking, locking, encryption and wiping of mobile devices.
   2. MAM software ensures that software that's remotely installed, deleted, encrypted and wiped are secure and enables wiping of corp. apps and data.
   3. iOS: Settings -> Mail -> Accounts -> Add Accounts: Choose or add a provider, provide credentials, choose IMAP or POP, configure incoming & outgoing mail server names, and verify uname and passwd.
   4. Android: Settings -> Accounts & Backup -> Manage Accounts -> Add Account: Choose account type (IMAP, SMTP, POP3), enter email and passwd, and validate setup.
2. Mobile Device Synchronization: mirroring changes from all devices to enable the mobile device to be an extension of one's main device.
   1. Microsoft 365 sync via Start -> Settings -> Accounts -> Sync
   2. Android uses Google Drive and Workspace via Settings -> Accounts & Backup -> Backup Data
   3. iCloud: Settings -> Apple ID, iCloud
   4. Can sync mail, photos, calendars, contacts, as well as apps, videos, bookmarks, docs, location & social media data, e-books, passwords

## Hardware & Network Troubleshooting 1101

## Backup and Recovery

1. Restoring data from incremental backups require:
   1. All copies of incremental backups made since last full backup
   2. Copy of the last full back up
2. Synthetic Full back up copy: up-to-date full backup copy composed of the last full back up and subsequent incremental, and/or differential back ups
3. On site backups are advantageous due to:
   1. No subscription fee, Control over backup media and process, and faster data access
4. Off site backups are better due to:
   1. Improved security, Scalability, and Geo redundancy
5. Grandfather-father-son: back up rotations scheme
   1. backups are perform daily to create weekly back ups and back ups created at the end of each week are used to create a monthly back up
6. 3-2-1 backup strategy
   1. Keep at least 1 backup copy offsite
   2. Create 1 primary backup file, then 2 copies of the primary backup file
   3. Save backups to 2 different storage media types

## Virtualization & Cloud Computing 1101

**Cloud Models and features**

Cloud structures and services available in cloud environment

1. Private: Virtualization resources are less flexible and more costly, but are highly secure. Purchased and used only by a single organization (user).
2. Public: cloud resources that are shared across the open internet and provisioned for open use by general public.
   1. All user data is housed in same server, which is less secure. (ex. iCloud, Dropbox)
3. Hybrid: Delivery models composed of two or more interlinked cloud infrastructures
4. Community: cloud shared by specific set of users, increased security. (ex. group of orgs sharing common interests)
5. `IaaS`: Infrastructure - virtual data center that allows clients to house all resources in the cloud. The client is responsible for OS & app patching, management, maintenance. Resources can include servers, firewalls, routers, switches, etc.
6. `PaaS`: Platform - allows developers to focus on creating, managing and building their own apps. The provider handles back-end (servers, OS, dev tools).
7. `SaaS`: web-based programs accessed on the web, whereever an internet connection is, instead of locally.
8. Cloud Features and Characteristics
   1. `shared resources` (resource pooling): The provider divides resources among clients by sharing the resources of one physical host machine between multiple VM's.
   2. `metered utilization` (measured/metered service): the auto control and optimization of resources by tracking client's usage and only charging for services used, thus providing transparency for the provider and client.
   3. `rapid elasticity` enables organizations to increase virtual resources automatically, as needed, based on growth and demand.
   4. `high availability` is a service that's highly responsive and uninterrupted, with uptime measured in nines (ex. 99.99% (4 nines))
   5. File synchronization enables the most recent data to be available both locally and in the cloud.

-----

**Virtualization**

1. A local server hosting a virtualized OS is example of `on-premise VDI` solution
2. `Persistent VDI` features users running their own virtual desktop copy, and their data being saved when the session ends.
   1. non-persistent VDI sessions revert back to original state and are shared between many users.
3. `PaaS`: complete software and/or VDI service that's fully cloud based
4. `Saas`: cloud service that includes the platform, infrastructure, and managed software & deployment
5. `Virtualization` allows multiple OS to work simultaneously on one hardware device.
   1. Disadvantages include: degrading performance due to the VM's sharing the resources of one host's hardware, which also becomes a single point of failure
   2. Workstations used for virtualization should have maxed out RAM and CPU cores, and large/fast HDD's.
6. `Hypervisor` is a program for manageing multiple OS's and/or instances of an OS on one computer.
7. `CPU HAV` enhancements: VT-x for Intel and AMD-V for AMD
8. `VM sprawl`: multiple VM's that're deployed don't have proper admin controls.
   1. Security measures that can prevent VM sprawl: running usage audits and documenting assets
9. `VM escape`: Accessing primary hypervisor running on the host machine controlling the VM's, by breaking out the boundaries of the guest OS installation
   1. Sandboxing and patch management can guard against VM escape.

- VDI manage virtual desktops via on premise or cloud versions.
  - On premise: VM that's running the VD is at same location as user. It removes the physical hardware used for networking and replaces them with virtual hardware contained on one on-site machine.
  - Cloud: VM is located in a cloud environment, run through the provider, thus taking responsibility of the hardware running the VDI away from the user, and to the cloud provider.
- Client-side virtualization: running the virtual env. on a device located on premise, and running the software on client machine, instead of the cloud. Client device hosts the hypervisor and must consider CPU, RAM, HDD's and network capabilities.
- VM's maximize resources by removing hardware & software barriers. They can run multiple OS's on one device, or pool resources from multiple servers to create one powerful system.
  - Also used to protect the host system by separating the VM's from one another
- Sandbox - A temporary, isolated venv used for testing & quarantining. This prevents the host from becoming contaminated because the env. is virtually separated, the data isn't saved to the host, and data is removed when the sandbox is terminated.
- Venv's & OS's can be made to test and develop apps
- App virtualization: can be used with legacy software & OS, and cross-platform functionality.
  - Process of making virtual OS of one platform on another platform.
    - An app designed for Windows can be tested for macOS devices by creating a macOS VM on the Windows device.
  - Legacy Software/OS: outdated software/OS that're incompatible with current systems.
- VDI's must implement security controls similar to physical ones
  - strong passwords, account lockout policies, MFA's

## Networking 1101

_DNS database records_

1. `A` record returns a 32-bit IP address.
2. `AAAA` record creates a pointer that maps a hostname to an IPv6 address.
3. `MX` record maps a domain name to a list of mail servers for that specific domain.
4. `TXT` records don't direct any traffic, but provides more info about a domain to outside services
   1. `TXT` records used for spam management:
      1. `SPF` - open standard that defines a method to prevent email sender address forgery. It allows the domain owner to list the servers that are allowed to send mail from the domain.
      2. `DKIM` - allows an email receiver to verify that an email claiming to come from a specific domain was actually authorized by the domain owner. It's an authentication method that allows using digital signature to sign outbound emails
      3. `DMARC` - has instructions for email recipient on how to handle emails that don't meet the sender's mail policies

_IP Address & Network Types_

1. `Lease` - the amount of time a DHCP client can use a dynamically assigned IP address from the DHCP server
2. `Reservation` - permanent IP address assignment from DHCP server
3. `Scope` - IP address range that the server can lease out to clients
4. `VLAN` - logical group of PC's that lets computer hosts appear attached to the same broadcast domain, even if they're not in the same physical location
5. `VPN` create private encrypted connections between remote locations, using public networks (internet)

- satellite internet connections
  - high signal latency
  - susceptible to interference (ex. weather, line-of-sight)
  - higher cost compared to terrestrial links
- `Fiber` connection is the fastest
- Cable broadband use cable modems to access the internet w/in a standard cable tv infrastructure
- `ADSL` is the most common type of DSL internet access

- `WWAN` use cell towers that provide wireless signal coverage to mobile devices
- `WISP` an ISP that offers subscribers internet access at certain wireless hotspots
- `LAN` network type comprised of connected computers located within a small area (ex. 1 building or several building)
- `WAN` computer network that connects several smaller networks across a large area
- `PAN` network with a limited-range, used to transmit data between different types of personal devices

**Wireless/Cell Data Network**

1. 2G: max data rate of 64 Kbps and 3G, 200 Kbps, had limited network range and both used traditional telephone circuits
   1. GSM: global system for mobile communication, AT&T & T-Mobile & CDMA: Code-division multiple Access, Sprint & Verizon were incompatible cell connection standards used in 3G tech.
2. 4G: uses IP enabling faster download/upload speeds and higher range
   1. 2 versions: WiMax and Long-term Evolution (LTE)
3. 5G: separated into 3 classes and setup in 2018
   1. eMBB: enhanced mobile broadband used for phone & mobile communication
   2. URLLC: ultra-reliable low-latency comm., used in auto cars and industrial apps
   3. mMTC: massive machine-type comm: sensors used in tech that support IoT capable devices
4. Cellular is largest & farthest-reaching method
5. Hotspot: enables Wi-Fi capable devices to share their cell internet connection wirelessly.
   1. iOS: Settings -> Personal Hotspot
   2. Android: Settings -> Connections -> Mobile Hotspot -> Tethering
6. PRL Updates: preferred roaming list are updates to reference guides used to connect to cell towers during roaming and are updates with phones OS update

----------

1. Bluetooth: Enable bluetooh -> enable pairing -> locate device for pairing -> enter PIN code -> test connection
   1. based on IEEE 802.15 standards for WPAN using bluetooth for data-link transport
   2. Windows: setting -> devices, Android -> Setting -> connections, Setting -> Bluetooth
2. Location Services: iOS: settings -> Privacy -> Location Services, Android: Settings -> Location
   1. GPS: global positioning system services: satellite-based nav system that shows locale and tracking on devices by using triangulation between receivers and satellites. Uses 3 components: satellite, ground control network, receiver.
   2. cell location services: Carrier-based with limited ranges based on the cell towers it uses.

----------

## Sections 220-1102

- **OS**
- `Microsoft Windows`
  - editions
  - command-line
  - features and tools
  - control panel utilities
  - settings app
  - security settings
  - networking features
  - troubleshooting
- `common OS types`
  - MacOS
  - Linux
  - mobile
    - apps and troubleshooting
- installation and upgrade

- **Security**
- physical
- logical
- wireless
- malware
- malware removal
- social engineering
- threats & vulnerabilities
- SOHO security settings
- workstation security

- **Data & Remote Info**
- data destruction and disposal
- backup and recovery methods
- script files
- remote access tech

## Security 1102

## Operating System 1102

1. Metro UI introduced with Windows 8
2. Charms bar wasn't included in Windows 10
3. macOS uses the term Spaces for multiple Desktops, Terminal for command-line interface & Finder for File Explorer
4. KDE desktops use the term Kickoff for Start button
5. default download location C:\Users\<uname>\Downloads
6. 32-bit apps install in C:\Program Files(x86)\
7. Open Admin Tools by right-clicking Start button and selecting Admin Tools
8. Windows 10 Settings app has multiple utilities in a unified interface

### OS Install, maintenance, overall information

- in-place upgrade: install type that keeps system settings, personal files, and apps from the older OS version
  - available in Windows 7 and 8.1

### Windows

1. Windows `Home` edition:
   1. Does not allow: Assigned Access, Remote Desktop server component, local group policy editor (gpedit.msc)
   2. k
2. `Pro`
   1. 2 TB memory limit
   2. joining a domain
   3. BitLocker Drive Encryption
3. `Pro for Workstations`
   1. 6 TB RAM limit
   2. joining a domain
   3. BitLocker Drive Encryption
4. `Enterprise`
   1. 6 TB RAM limit
   2. allow joining a domain
   3. BitLocker Drive Encryption
5. 32-bit (x86) has 4GB physical memory limit, while the 64-bit (x64) version supports 128GB or RAM.

----------

**MS Windows 10 Features & Tools**

1. `Task manager` (taskmgr.exe): Close non-responsive apps; show info of running programs, processes and services
   1. management of logged-in users by a System Admin; usage reports of system resources (RAM/CPU/GPU/Disk/Network)
   2. Launch Task manager:
      1. `Ctrl+Alt+Del` | `Ctrl+Shift+Esc` | `Right-click`: TaskBar || Start button
      2. CMD prompt ||  Windows + R key (Run Window) ➡ type taskmgr.exe
   3. `Services` tab used for managing background processes
   4. `Startup` tab let's user adjust apps that auto launch on sign in
   5. `Performance` tab provides access to graphs detailing resource usage (CPU, memory, disk, network, GPU)
   6. `Processes` tab: info on system resources that running apps and background processes are using
   7. Close non-responsive apps in Processes tab by right-clicking the app, then end task or left-click the app and select End task button in bottom right corner.
2. Microsoft Management Consol (MMC): customizable system utilities framework composed of snap-ins to manage networks, PC's, services and other components.
3. Event Viewer (`eventvwr.msc`): Windows admin utility for monitoring system health and troubleshooting apps, OS, and hardware issues.
   1. can view event logs: Apps, System, and Security (audits) that're categorized as either Info, Warn, Error events.
4. `diskmgmt.msc`: system utility for managing storage media
5. `taskschd.msc`: admin tool for scheduling program launches, and scripts set to run at specific times or intervals.
6. `devmgmt.msc`: componet for viewing/managing hardware components and device drivers
7. Windows Certificate Manager snap-in (`certmgr.msc`): manage (view/export/import/delete) current user's digital certificates

### macOS, Linux, Mobile

## Software Troubleshooting 1102

## Operational Procedures 1102

### Safety and Professionalism 1102

Troubleshooting Method

1. Identify the problem
2. establish theory of probable cause
3. test theory to determin cause
4. establish a plan of action to resolve the problem and implement solution
5. verify full system functionality and implement preventive measures
6. document finding, actions and outcomes

- ESD is type of EMP and can damage PC's. Prevent this by using antistatic tools, disconnecting PC from power
- EMI - electromagnetic interference
- RFI: radio frequency interference; prevent by keeping devices away from one another

- Try to implement simple answers/solutions first.
- toolkit should have at least a Phillips-head screwdriver.
- create temporary passwords when working w/ clients, if you need to access their account, then change it afterwards.
- Follow up with clients after completing ticket
- antistatic straps keeps you at same electrical potential as the PC
- Backup data before working on client PC's and document findings

----------

## References and Resources

<ul>
<li>

 [A+ Docs 2][A+ Documentation 1]
</li>
<li>

[ExamCompass][exam_compass]
</li>
<li>

[Union Test Prep][Union_test_prep]
</li>
</ul>

<a href='https://github.com/bahim22'>
<h3>Hima Portfolio</h3>
<img src='https://raw.githubusercontent.com/bahim22/work/ppu/py-prac/QRCodes/qr_blue.png' width=50 height=50 align=center alt='qr_code for profile'>
</a>

<!-- ![QR_Code](https://github.com/bahim22/work/blob/ppu/py-prac/QRCodes/qr_blue.png) -->

<!-- <img src='https://raw.githubusercontent.com/bahim22/work/ppu/py-prac/QRCodes/qr_blue.png' width=100 alt='qr_code for profile' align='center'> -->
[exam_compass]: https://www.examcompass.com/comptia-a-plus-220-1101-exam-acronyms-quiz
[A+ Documentation 1]: https://github.com/bahim22/work/blob/ppu/Docs2/AplusDoc.md
[Union_test_prep]: https://uniontestprep.com/comptia-a-core-series-exam/study-guide

<!-- /* cspell: enableCompoundWords */ -->
<!-- cSpell:ignoreRegExp /[^\s]{40,}/  -->

# A+ Practice & Notes 4

- [A+ Practice \& Notes 4](#a-practice--notes-4)
  - [Sections 220-1101](#sections-220-1101)
  - [Sections 220-1102](#sections-220-1102)
  - [Safety and Professionalism](#safety-and-professionalism)
  - [Hardware 1101: Main overview](#hardware-1101-main-overview)
    - [Mobile Devices 1101](#mobile-devices-1101)
  - [Virtualization and Cloud Computing](#virtualization-and-cloud-computing)
    - [Backup and Recovery](#backup-and-recovery)
  - [Networks](#networks)
  - [References and Resources](#references-and-resources)

## Sections 220-1101

- **Cloud**
- Cloud computing
- virtualization
- troubleshooting methodology

- **Devices**
- Laptop
- Display devices
- mobile devices
- printers

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

----------

## Sections 220-1102

- **OS**
- Microsoft Windows
  - editions
  - command-line
  - features and tools
  - control panel utilities
  - settings app
  - security settings
  - networking features
  - troubleshooting
- common OS types
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

----------

## Safety and Professionalism

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

## Hardware 1101: Main overview

1. Metro UI introduced with Windows 8
2. Charms bar wasn't included in Windows 10
3. macOS uses the term Spaces for multiple Desktops, Terminal for command-line interface & Finder for File Explorer
4. KDE desktops use the term Kickoff for Start button
5. default download location C:\Users\<uname>\Downloads
6. 32-bit apps install in C:\Program Files(x86)\
7. Open Admin Tools by right-clicking Start button and selecting Admin Tools
8. Windows 10 Settings app has multiple utilities in a unified interface

- Computers are composed of the hardware, OS and Applications
- Computing process stages: Input, processing, output
  - modern PC's also have stages for Data storage and network connection

### Mobile Devices 1101

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

1. Mobile Device management(MDM) and Mobile Application management (MAM): allows businesses to secure mobile devices by using the MDM software
2. Mobile Device Synchronization: mirroring changes from all devices to enable the mobile device to be an extension of one's main device.
   1. Microsoft 365 sync via Start -> Settings -> Accounts -> Sync
   2. Android uses Google Drive and Workspace via Settings -> Accounts & Backup -> Backup Data
   3. iCloud: Settings -> Apple ID, iCloud
   4. Can sync mail, photos, calendars, contacts, as well as apps, videos, bookmarks, docs, location & social media data, e-books, passwords

## Virtualization and Cloud Computing

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

### Backup and Recovery

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

## Networks

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

## References and Resources

!['./AplusDoc.md'][A+ Documentation 1]
[ExamCompass][exam_compass]

[exam_compass]: https://www.examcompass.com/comptia-a-plus-220-1101-exam-acronyms-quiz
[A+ Documentation 1]: https://github.com/bahim22/work/blob/ppu/Docs2/AplusDoc.md

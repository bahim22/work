# CompTIA A+ Docs

| Hima Balde | PPU | 06-10 of 2022 |
| ---------- | --- | ------------- |

## Table of Contents

- [CompTIA A+ Docs](#comptia-a-docs)
  - [Table of Contents](#table-of-contents)
  - [Troubleshooting Steps](#troubleshooting-steps)
  - [Seconday Skills](#seconday-skills)
  - [Tools and Safety](#tools-and-safety)
  - [Computer Parts](#computer-parts)
    - [Motherboard](#motherboard)
    - [Processor, CPU](#processor-cpu)
    - [Power supplies](#power-supplies)
    - [Adapter Cards](#adapter-cards)
    - [BIOS/CMOS/UEFI](#bioscmosuefi)
  - [OS Install, Upgrade, Boot](#os-install-upgrade-boot)
    - [_Boot methods_: user selects how to boot pc \& w/ what media](#boot-methods-user-selects-how-to-boot-pc--w-what-media)
    - [Misc OS info](#misc-os-info)
  - [`Network`](#network)
    - [Rules governing the transmission specified by the protocol](#rules-governing-the-transmission-specified-by-the-protocol)
    - [Common Internet Protocols, Data and File Sharing](#common-internet-protocols-data-and-file-sharing)
    - [`TCP/IP`](#tcpip)
    - [TCP/IP Abstraction Layers](#tcpip-abstraction-layers)
    - [**Ports** and **Protocols**](#ports-and-protocols)
    - [`UDP`: user datagram protocol - datagram oriented protocol](#udp-user-datagram-protocol---datagram-oriented-protocol)
    - [OSI model (Open systems interconnection)](#osi-model-open-systems-interconnection)
  - [`Hardware`](#hardware)
    - [Memory](#memory)
    - [Storage and Peripherals](#storage-and-peripherals)
      - [RAID](#raid)
  - [`Software`](#software)
    - [Windows Admin Tools](#windows-admin-tools)
    - [Windows Management Framework](#windows-management-framework)
    - [Windows naming](#windows-naming)
    - [Displays](#displays)
  - [Mobile Devices](#mobile-devices)
  - [References](#references)

## Troubleshooting Steps

1. Identify the problem
2. establish a probable cause
3. testing to determine cause
4. establish plan to resolve issue
5. implement solution
6. verify functionality and implement preventive measures
7. document resuts and steps

- Identify the problem
  - Question the user and identify user changes to computer and perform backups before making changes
  - Inquire regarding environmental or infrastructure changesReview system and application logs
- Establish a theory of probable cause (question the obvious)If necessary, conduct external or internal research based on symptoms
- Test the theory to determine causeOnce the theory is confirmed, determine the next steps to resolve problemIf theory is not confirmed reestablish
new theory or escalate
- Establish a plan of action to resolve the problem and implement the solution
- Verify full system functionality and, if applicable, implement preventive measures
- Document findings, actions, and outcomes

## Seconday Skills

> soft skills, professional communication/attire, layterm usage, keep info on drivers, routers, chips, etc., accessible; always backup client data prior to troubleshooting

___

## Tools and Safety

- multihead screwdrivers, tweezers, multimeters (verifies power volts & connection)
- chip extractors, storage canisters, software toools (on zip & thumb drives)
- chips get affected @ 200v from electrostatic discharge
- humidifiers: ~ 50%; too low causes static from dry or corrosion from wet;
- compressed air cannister; remove jewelry
- use antistatic bands when moving PC parts; ESD mats/straps to eliminate static
- equipment & self grounding: equalize charge; clamp to metal on PC case
- high volatage safety: 120v => 3.3-5 or 12v conversion (power supply)
  - 85-110 decibals = start of damage to hearing
- `Ergonomics`: design to prevent discomfort/injury due to repetitive use
  - eye care, good posture, focus on distant object every 15 min; take breaks; where gloves, mass, eye shields when applicable
  - dispose of waste appropriately (hazaardeous and environmental)
    - batteires, CRTs, printer carts/toners
- `Safety rules and regulations`:
  - Environment, Hazards, Prevention, PPE
  - UL: Underwriters lab | CSA Inter'l: safety check organizations
  - OSHA (occupation safety and health org.)
  - NEC - nat'l electric code
  - CFR - code of federal regulations
  - material safety sheets come w/ any hardware that has chemicals
  - `Check` conditions and grounding prongs; electricity is off and unplugged
  - `review` lockout/tagout policies

___

## Computer Parts

1. `CPU`(The Central Processing Unit) is the part of the computer that asks, "what's next"
2. `Main Memory`: stores prog. & data that CPU uses quickly and isn't saved on power off
3. `Secondary Memory`: also stores info; but is slower; keeps info even if PC has no power
   1. (ex. disk drives, flash memory - USBs)
4. `I/O devices`: input and output devices used to interact w/ the computer
5. `network connection`: get info over network; store/retrieve data (similar to secondary mem.)

### Motherboard

- `Power connectors` – Any component cannot operate without power and the same goes for a motherboard. The power connector is a 20/24-pin connector that sits near to the processor socket on some hardware while is present beside the right edge in others. It’s the area where the main connector attaches and thus, supplies power to all components.
- `Processor socket` – It is a central unit present on the motherboard located on the center and the main function of it is to hold the entire processor.
  - CPU is the brain of a computer.
- `Video card slot` – attaches video card, usually with a PCI-Express slot. Gaming PC's can have multiple slots for video cards.
- `Memory slots` – Usually in upper right-hand side of MoBo and carry a computer’s memory modules. Slots differ depending on the Mobo and can range from 2 to 8+ slots (on gaming PC's). Industry standard is DDR3 memory. The memory capacity of the motherboard depends on the # of slots.
- `IDE & SATA ports` – Ports used to allow connectivity for storage devices & optical drives. IDE is outdated and was replaced by SATA interface, which is smaller and faster(speeds up to 600 MB/s)
- `Expansion slots` – Enables additional hardware to be installed in order to optimize computer performance.
- `Northbridge & Southbridge` – the bottom right area of motherboard houses a square and metallic component, used for the evacuation of heat produced by the computer, providing thermal protection for the Northbridge.
  - `Northbridge`: coordinates data flow between video card, memory, and the processor.
  - `Southbridge`: coordinates data flow between soundcards and processor.
- `BIOS Chip & Battery` – The BIOS chip is a component which consists of a basic code required to carry out the boot process on a computer.
  - Chip component with code that's responsible for carrying out the computer's boot process, until the OS takes control.
  - Housed on a memory chip that requires steady power supply to execute its function.
  - Battery supplies power when the power supply is unplugged, to keep it running.
- `Front Panel Connectors`, USB & Audio Headers – Front Panel connectors is a place where all the elements on the front are connected. It comprises of USB connectors, power button, power LED, audio connectors, and the reset buttons.
- `Rear Panel Connectors` – Rear Panel Connectors act as a bridge between the inside and outside of a computer. These connectors are situated on the left edge of a motherboard, so it is pretty confusion what the name suggests. However, these connectors can be accessed from the outside, so their name simply tells where they can be accessed from. These connectors power all external hardware which include a mouse, keyboard, speakers, monitor, etc.
- form factors: ATX, microATX, ITX
- expansion buses: PCIe and PCI
- CPU info
  - intel chipsets connect to CPU via DMI or QPI
    - LGA775, 1150, 1155, 1156, 1366, 2011 sockets
  - AMD CPU-to-chipset is HyperTransport
    - AM3, AM3+, FM1, FM2, FM2+ sockets

<!-- ![mobo](/assets/MoBoOld.jpg)
![moboParts](/assets/moboParts.jpg) -->

### Processor, CPU

- brains of the computer
- processor performs calculations based on requests from the OS
- controls the access to system memory
- proc. speed measures how fast it can handle tasks
  - Mhz, Ghz
  - millions of interactions/s
- OS & Processor
  - data input: from input device such as keyboard, mouse, card reader => processing input => data output (to ouput drivers {monitors, printers}) => storage via storage devices {hard drive {HDD, SSD}, RAM}

### Power supplies

- take 120v of alternating current (AC) and convert to the volt required by the PC (usually 12v || 3.3v, 5v)
  - different volts for HDD or PCIe cards

### Adapter Cards

### BIOS/CMOS/UEFI

1. IDs, test, init compos and boots to drive, optical disk,  USB flash drive or network (PXE)
2. can update by flashing it w/ new firmware

- _BIOS_: Basic input/ouput system; chip on mobo w/ in ROM or w/in flash memory (aka firmware)
- _CMOS_: stores time/date, passwords, CR2032 lithium battery provides power
- _POST_: power on self test: mobo ini hardware, runs POST, boots & loads OS (BIOS info found by run msinfo32 -> system summary)
  - system startup: computer searches nonvolatile data stores device in order defined in boot seq.; then CPU takes control and loads OS into system membory
  - setup utility stored in BIOS flash memory (in battery-backed CMOS RAM)
- _UEFI_: Unified Extensible Firmware Interface: spec that defines a software interface between OS & platform firmware.
  - Boot process: UEFI -> GPT (EFI boot loader) -> Kernel -> OS
- _CSM_: Compatibility support module: EFI support of booting in legacy BIOS mode from MBR-part disks
- _PXE_: Preboot execution env: standardized client–server env. that boots a software assembly, retrieved from a network, on PXE-enabled clients.
  - forms part of the UEFI standard
  - PXE-capable network interface controller (NIC) required on client side
  - uses industry-standard network protocols such as _DHCP_ and _TFTP_
- ACPI: advanced config and power management interface: defines working interfaces between the OS, BIOS, and hardware
  - can allow the OS to control power management
  -

## OS Install, Upgrade, Boot

### _Boot methods_: user selects how to boot pc & w/ what media

1. optical disc (CD-ROM, DVD, Blu-ray): pc will prob have built-in drive to read them; very common way to install OS on a pc
2. external/flash drive (interfaces: USB, eSATA): ext optical/hard/flash drives, USB is common
3. Network boot (PXE): preboot eXecution Env.; boot from network resources; net & remote server hosting the bootable image need config.
   1. common in corp. env. where net & server resources are availalbe; allows setting up multiple pc's w/ similar images
4. internal fixed disk (HDD/SSD) & internal Hard Drive (Partition)
   1. disk can have OS install image or OS already installed. Most common way to boot PC after OS install completed
   2. simple configs have one bootable par on a disk, but a disk can have > 1 par to multiboot diff OS. One logical par can span multiple physical hard disks

| Install Types           |   |
| :------------------- | -------------- |
|  _Type_     |  _Description_ |
|   💻    | 📕 |
|    unattended     | pre-config., need special server w/ install image/script & good for many PC's w/ same config |
|   in-place upgrade  | installs newer OS over older one; may preserve settings, fi, apps  |
|    clean| disregards previous data; used for PC w/o an OS or to intentionally delete old data |
| repair | boot w/ same -v OS & select repair; rewrites SF & settings, retains user fi; can repair OS that's unbootable or w/ issues unfixable by other methods |
|     multiboot             | uses boot mngr that maintains boot config; user sel OS to boot; recommend install OS's to diff HDD or separate logical pars  |
|   remote net      | PXE net boot using remote server; may require choosing install options or be unattended |
|         image deployment         | used for PC's w/ == hardware that need == OS/settings/apps. Diff software tools can do this. Steps involve sel one PC => clean install, config, app install => create image from that PC & make available on network or portable media => copy image to other PC's |
|   recovery par  | create rec par during install that is a bootable par for later or repair install; contains diagnostic/repair tools |
| |
| **Partitioning** |
| |
| _Type_ | _Description_ |
|   ---     | --- |
|  _Info_ | creates >= 1 logical drives; can be formatted separately & have separate FS. W10 allows each par to have diff drive letter |
|    Dynamic  | more complex config & less limits than basic dsk. Can create pars spanning many physical HDD's (software RAID) |
| Basic | most common; separated into logical pars  |
| Primary | can have only one logical drive; W10 only boots from primary par |
| Extended | enables >= 1 logical drive  |
| logical | rep by a drive letter in W10; recomm. distinguishing btw dsk, par & logical drive; can be assigned 1:1 but aren't limited to 1   |
| GPT | GUID Par Table: has info on how dsk is partitioned. supports larger drives & more pars/drive than MBR  |
| |
| **File System Types/Formatting** |
| _Type_ | _Description_ |
| Info | Fs enables storing/managing/accessing fi on a par. OS's support diff FS & pars are formatted w/ specific FS before use |
| ExFAT | designed for small flash & SSD drives, good for perf & media fi storage |
| FAT32 | supported by many OS & provides basic features. pars can be >= 2 TB |
| NTFS | more advanced & supported by modern W --v. user can set/manage permissions for fi/dir for users/groups. useful for secure net fi sharing. Has indexing, compress., encrypt. on FS level |
| CDFS | FS for CD/DVD's |
| NFS | Network File System. mostly in servers where you can have fi access on net btw sys. |
| ext3, ext4 | used for Linux. 4 is updated -v that enables larger pars, fi & better perf |
| HFS | used for MacOS |
| Swap par | Linux par used when physical RAM is maxxed out. The Data flows to swap pars; reducing perf, in place of running more apps simultaneously. |
| quick vs. full format | quick changes FS records making dsk appear empty. Full rewrites prev fi, detects surface errors on dsk and makes restoring fi harder. |

### Misc OS info

1. 3rd party (unsigned drivers) should have source verified to ensure validity.
2. signed drivers: W install drivers are tested/approved by MS
3. workgroup: Can setup printer & fi sharing w/ small group/fam
   1. ex. a dept in a larger org. or a home user
4. Domain setup: Companies can use a domain controller instead for more secure, centralized login for large groups, which allows an easier path for managing large net
5. Time, Date, Region, Lang: config these settings during install (some OS require reinstall to change lang.)
6. Driver install, Software, Updates: Keep system updated for secuirty reasons. Install proper drivers for the type of system (32-bit => x86 sys && 64-bit on x64 sys). Use 'check for updates' utility in W10 to update OS and other MS software. Other software needs checked separatley.
7. Know differences in Hardware/Apps/OS compatability

___

## `Network`

- IEEE (Institute of Electrical & Electronics Engineers) handles wired and wireless networking
- ISO (International Organization for Standardization) handles other types of networks
- 2 types of communication protocols:
  - binary utilizes all values of a byte; intended for machine reading; more terse and faster
  - text-based/plain text - only uses values corresponding to human-readable characters in ASCII encoding
- `SDN`: software-defined networking sets up the network through the cloud and uses virutalization to replace functionality of the router in a network
- `Cable Modem`: device that connects to a cable line for connectivity
  - newer versions don't modulate/demodulate analog signals, but are still called modems.
- `ONT`: optical network terminal - modem that provides connectivity by using a fiber-optic line
- `DSL`: digital subscriber line - modem that uses telephone line to provide connectivity

### Rules governing the transmission specified by the protocol

1. Data and address formats for data exchange & address mapping
   1. exchange of digital message bitstrings
      1. `header`: fields w/ relevance to the operation of the protocol
      2. `payload`: where actual message is carried
   2. addresses are used to identify & send to intended receiver
      1. carried in header of bitstrings & identified using an address pair
   3. address mapping: map addresss of one scheme on addresss of another scheme
      1. ex. translate logical IP specified by app to an ethernet MAC address
2. Routing: systems that aren't directly connected, using intermediary systems along the route to intended receiver to forward data on behalf of sender, which are connected via routers
   1. Internetworking: interconnection of networks via routers
   2. Routing: sending data from source => destination network
      1. It's supported by host addressing & identification using hierarchical IP address system
3. detection of transmission erros: CRC of data area added to end of packets, allows rec to reject packets on CRC diff and arrange for retransmission
4. acknowledgement: recievers send acknowledgements of packets received correctly
   1. required for connection-oriented communication
   2. loss of info (timeouts and retries): packets can be lost on the network or delayed in transit
   3. Sender may expect an acknow. of correct reception from the rec w/in a certain amount of time
   4. sender may need to retransmit the info on timeouts
   5. retransmission has no effect when link is permanently broken, so the n of retransmissions is limited
      1. if the limit is exceeded it's an error
   6. `Information flow`, `Sequence` and `Flow control`
   7. `MAC`: media access control - sublayer within Data Link (0SI - layer 2) (Link layer 1 TCP/IP) that provides flow control & multiplexing for transmission medium, frame delimiting & recognition,
      1. Data Link/Link Layer also includes LLC sublayer - logical link control: provides flow control & multiplexing for logical link (ex. EtherType, 802.1Q VLAN tag)
   8. half-duplex links: transmission via one direction at a time
   9. shared medium: transmission via 1 sender at a time
   10. bitstrings are divided into pieces and sent on network individually
       1. Can get lost, delayed, or take different routes, resulting in pieces arriving out of sequence or retransmitted, which creates duplicate pieces
   11. The data is marked w/ sequence info at the sender, so receiver can figure out any issues to reassemble message or ask for retransmission
   12. flow control is needed when sender transmits faster than reciever so intermediate network equipment can process the transmission
   13. Queueing (buffers) - usually FIFO queues that are used to deal with messages in the order it was sent
       1. can use multiple queues with diff priorities

### Common Internet Protocols, Data and File Sharing

### `TCP/IP`

- IP is responsible for delivering packets to the right computer
- Transmission Control Protocol/Internet Protocol model: _standardized process_; data link protocol; Connection Oriented Communication
  - used to allow computers & devices connected to the internet to communicate w/ each other across networks
  - determines how PCs transfer data so that it's kept accurate.
  - assumes a connectionless net most suitable for LAN
  - data may be delivered out of order, since different network packets are routed independently and may be delivered over different paths
  - connection-oriented protocol and requires handshaking to set up end-to-end communications.
  - Once a connection is set up, user data may be sent bi-directionally over the connection
  - reliable; ordered; heavyweight; streaming
    - manages acknowledgement, retransmission, timeouts
    - attempts delivery of message multiple times and will resend if data is lost (either no missing data or dropped connection)
    - will buffer the out of order data to proper order
    - requires three packets to set up a socket connection before data can be sent
    - handles reliability and congestion control
    - data read as a byte stream, no indications transmitted to signal message (segment) boundaries

1. breaks down data into packets and reassembles packets into complete message on other end
   1. smaller packets makes it easier to maintain accuracy
   2. packets can travel via diff routes depending on congestion.
   3. Data divided into packets based on 4-layer procedure, going thru each layer in 1 order and reassembled on receiving end

### TCP/IP Abstraction Layers

- **Network/Link** (network access)
  - operates w/in scope of local network connection that a host is attached to.
  - Link includes all hosts accessible w/o traversing a router.
  - Link size is determined by the networking hardware design.
  - TCP/IP designed to be hardware independent and can be used on top of any link-layer tech
    - (ex. any hardware, virtual link layers(VPNS & tunnels))
  - includes protocols used for describing local net topology and interfaces needed to affect transmission of internet layer datagrams to other next-neighbor hosts.
  - moves packets between internet layer interfaces of 2 different hosts on same link.
  - The transmitting/reciving packets link processes are controlled in device driver for network card, firmware and/or chipsets.
    - `NIC`: network interface/adapter card: provides physical interface between a PC and the cabling used for connectivity
    - (performing functions like framing- which prepares the internet layer packets for transmissions, and then transmit the frames to the physical layer over a transmission medium).
  - TCP/IP has specifications for translating network address methods used in IP to link-layer addresses,(ex.MAC addresses).
  - Other aspects below that level, are assumed to exist and aren't  defined.
  - corresponds with functions in Layer 2 of OSI model
  - Ethernet, PPP, ADSL
- **Internet**
  - provides an unreliable datagram transmission facility between hosts located on different IP networks by forwarding datagrams to appropriate next-hop router for further relaying to destination.
  - Essentially establishes the internet and is responsible for sending packets across multiple networks. Makes internetworking (the interworking of diff IP networks) possible
  - IP carries data for many upper layer protocols (each w/ unique protocol #s).
  - IP is principal component of internet layer and defines 2 addressing systems to ID network hosts and locate them on the network.
  - protocols include: IP, ICMP, ARP, RARP, IGMP
  - Transmits data to network access layer when sending
  - Transmits data to transport layer when receiving
  - IPv4 uses 32-bit IP address and is capable
  - does logical addressing and data routing
  - IP, ICMP, ARP, DHCP
- **Transport**
  - allows host-host communication.
  - provides reliable, connection0oriented transport between two sockets on two PCS that communicate via IP.
  - defines status of connection and level of service during data transportation
  - transmits data to internet layer when sending
  - transmits data to Application layer when receiving
  - TCP, UDP protocols
- **Application**
  - UI for communication and how host programs interface with Transport Layer
  - defines TCP/IP application protocols
  - Transmits data to Transport Layer when sending and receiving
  - Protocols: DNS, HTTP, FTP, Telnet, RDP, POP3, SSH, SNMP, SMTP, NNTP(network news transport protocol)

### **Ports** and **Protocols**

1. `FTP`: 21 file-transfer oriented protocol that ensures data delivery; file transfer to/from server
   1. server that hosts files; allowing usrs to browse, transfer, upload files
2. `TFTP`: 69, trivial file transfer protocol - faster version of FTP that uses UDP
3. `ssh`: 22, remote administration protocol where user can control/modify their remote servers over the internet; replaced unsecure telnet protocol
   1. Secure Shell: cryptographic connection-oriented network protocol for operating network services securely over unsecured net
      1. ex. Access resources of a company branch in a diff area
   2. uses cryptographic techniques to ensure communication to and from  as well as enrypting data
   3. provides secure communication between 2 untrusted hosts over an unsecured network
4. `Telnet`: 23, unencrypted remote device access
5. **E-mail**
   1. `SMTP` 25, simple mail transfer protocol, sending email
   2. `POP3` 110, post office pro, receiving email
   3. `IMAP` 143, internet message access pro, receiving email
6. `RDP`: 27, reliable data protocol, provides facilities for remote loading, debugging and bulk transfer of images and data
   1. Remote Desktop Protocol: 3389, used for connecting remote PCs
7. **DNS**: 54, domain name system/service, translates domain names to IP addresses
8. **HTTP**: 400 hypertext transfer pro; standard for web communication; used for rendering pages in browser.
   1. **HTTPS**: 443 secured communication. on web
9. **DHCP**: 67/68, dynamic host configuration protocol; dynamically assigns IP addresses to network hosts through leases using UDP as its transport protocol
10. `NetBios`/`NetBT`: 137-139 network basic input output system and NetBIOS over TCP/IP: LAN communication. Works over OSI layer 4 and needs to work w/ a layer 5 protocol (ex. TCP/IP) to work properly.
11. `SMB`/`CIFS`:445 Server message block (primarily a Microsoft protocol) for shared file access
    1. Common internet file system: enhanced version of SMB; shared access on a network
12. `SLP`: 427 service location protocol; local service discovery
13. `AFP`: 548 Apple filling protocol; used for Apple file services
14. `LDAP`: 389 Lightweight directory access pro; access a directory on network objects
15. `SNMP`: 161/162, simple net mngmnt pro: send/rec net mngmnt messages
    1. used for monitoring/managing other nodes in a TCP/IP network
16. `Proxy Server`: features include access control, caching, URL filtering and privacy
17. `WINS`: Windows Internet name service

- _Network stack_: set of hardware/software that provides the infrastructure for a comp
- _Router_: Layer 3 (network layer) device that connects diff devices and determines best route for traffic between networks (uses a set of rules)
- _switches_: layer 2 (data link) device that endpoint devices connect to. It interconnects hosts on a LAN using MAC address of each host to make decisions about forwarding traffic
  - managed: configurable w/ features allowing a net admin to optimize/customize the switch. Have better monitoring options than unmanaged
  - unmanaged: plug-and-play; can't config. designed to allow hosts to auto connect when plugged into the switch, but coming at the expense of performance
  - routers and switches provide connectivity and control fraffic on the net.
- _Access Point_: any device to which a host can connect in order to access a net. Usually referring to a wireless access point that allows WiFi devices to connect to the net.
  - _Cloud-based network controller_: network appliance that acts as a mngmt console for multiple network access points. also allows connection of AP to the net w/o config of each individual one.
- _Firewall_: A security appliance that filters traffic, permitting/blocking traffic thru it based on a config set of rules and network traffic inspection
- _NIC_: network interface card, adapter card used to connect a host to the network
- _repeater_: used to extend a signal being sent to provide add'l coverage
- _hub_: older tech layer 1 (physical layer) device that connects hosts together.
  - Don't recognize MAC addresss; Only send traffic coming in on one port out on every other port
- _cable/DSL modem_: used to connect to an ISP
- _Bridge_: layer 2 (data link) device that connects 2 net segments and controls traffic moving between them
-_patch panel_: physical panel w/ multiple connection points used as a central location to interconnect devies and ports on a net. Allows for an organized cabling strucutrre to manage 10s-100s of interconnections
- _PoE_: Power over Ethernet: tech, usually incorporated into switches, that delivers power to devices over data lines rather than a separate power cord
  - ex. You can power a device thru an ethernet port on a switch
  - PoE injector is used to add power to a data cable going to a PoE device (IP phone/camera)
  - PoE Switch is a net switch that supplies power to its Ethernet ports to power PoE devices
- _EoP_: ethernet over power; uses standard electrical wiring to interconnect ethernet devices
- 1
- _DHCP_: Dynamic Host Configuration Protocol; is a network management protocol used on IP networks
  - employs connectionless service model, using UDP (UDP port 67 for server and 68 for client)
  - manages IP settings for devices on its local network, (ex. auto & dynamically assigns IP addresss to those devices)
  - auto assigns IP addresses and other communication param to devices connected to the net using a client–server architecture
  - two network components: a centrally installed network DHCP server and client instances of the protocol stack on each device that periodically requests a set of param. from server

- Physical connection info
   > Hubs vs Swtiches: Hubs are outdated and connect each pc that's plugged into the repeater, it takes the signal that pc A sends to PC B (a frame: made up of 1500 bits) and repeats it by sending it to every pc connected and then those PC's read their MAC address and the address of the signals MAC and either reads it if it's for them or deletes it if not. Hubs just repeat back on all the ports, whatever's coming out.
   >> Switches: when the box collects the MAC of every PC connected to it and when it receives a frame  it makes a direct, physical connection between the two PC's. A switch is still a repeater, but it's a smart repeater and only sends the data out to the proper destination based on the MAC address

### `UDP`: user datagram protocol - datagram oriented protocol

- used to send messages (transported as datagrams in packets) to other hosts on an Internet Protocol (IP) network
- doesn't require prior communication to set up communication channels or data paths
- uses a simple connectionless communication model. UDP provides checksums for data integrity, and port numbers for addressing different functions at the source and destination of the datagram
- simpler message-based connectionless protocol. Connectionless protocols do not set up a dedicated end-to-end connection. Communication is achieved by transmitting information in one direction from source to destination without verifying the readiness or state of the receive
- Pros:
- doesn't ensure protection against delivery, ordering or duplication; good for time-sensitive apps
- transaction oriented, provides datagrams, simple and stateless, suitable for large N of clients
- lack of retransmission delays makes it good for real-time apps like VoIP, online games, supports multicast
- unreliable; not ordered; lightweight; datagrams; no congestion control; broadcasts; multicast
  - No concept of acknowledgement, retransmission, timeout
  - no ordering of messages, no tracking connections
  - packets sent indy and checked for integrity on arrival, packets w/ defined boundaries that're honored upon receipt
  - doesn't avoid congestion; control measures have to be setup at app level or in net
  - UDP can broadcase - sent packets can be addressed to be rec by all devices on the subnet
  - multicast mode of op where a single datagram packet can auto route w/o dupe to a group of subs

> Although UDP provides integrity verification (via checksum) of the header and payload, it provides no guarantees to the upper layer protocol for message delivery and the UDP layer retains no state of UDP messages once sent. For this reason, UDP sometimes is referred to as Unreliable Datagram Protocol. If transmission reliability is desired, it must be implemented in the user's application.

### OSI model (Open systems interconnection)

- connection-oriented network
  - communication session or a semi-permanent connection is est. before any useful data can be transferred. The established connection ensures that data is delivered in the correct order to the upper communication layer.
- most suitable for WAN
- the layers comm. via an interface called service access point
  - protocol standards define how peer entities (corresponding layers at each sys.) comm
  - service standards define how one layer talks w/ the layer above it.
- communication between a computing system are split into 7 different abstraction layers:
  - Physical, Data Link, Network, Transport, Session, Presentation, Application

  - The _Application_ layer may provide the following services to the application processes:
    - identification of the intended communication partners, establishment of the necessary authority to communicate, determination of availability and authentication of the partners, agreement on privacy mechanisms for the communication, agreement on responsibility for error recovery and procedures for ensuring data integrity, synchronization between cooperating application processes, identification of any constraints on syntax (e.g. character sets and data structures), determination of cost and acceptable quality of service, selection of the dialogue discipline, including required logon and logoff procedures
      - app layer protocols: WWW, SMTP, FTP
  - The _presentation_ layer: provides services to the application layer:
    - responsible for presenting the data in standard formats, data compression/decompression & encryption/decryption
    - presentation layer stadards: JPEG, MPEG, MIDI, PICT, TIFF
    - a request for the establishment of a session, data transfer, negotiation of the syntax to be used between the application layers, any necessary syntax transformations, formatting and special purpose transformations (e.g. data compression and data encryption).
  - The _session_ layer may provide the following services to the presentation layer: establishment and release of session connections, normal and expedited data exchange, a quarantine service which allows the sending presentation entity to instruct the receiving session entity not to release data to its presentation entity without permission, interaction management so presentation entities can control whose turn it is to perform certain control functions, resynchronization of a session connection, reporting of unrecoverable exceptions to the presentation entity.
  - The _transport_ layer provides reliable and transparent data transfer in a cost-effective way as required by the selected quality of service. It may support the multiplexing of several transport connections on to one network connection or split one transport connection into several network connections.
  - The _network_ layer does the setup, maintenance and release of network paths between transport peer entities. When relays are needed, routing and relay functions are provided by this layer. The quality of service is negotiated between network and transport entities at the time the connection is set up. This layer is also responsible for network congestion control
  - The _data_ link layer does the setup, maintenance and release of data link connections. Errors occurring in the physical layer are detected and may be corrected. Errors are reported to the network layer. The exchange of data link units (including flow control) is defined by this layer.
  - The _physical_ layer describes details like the electrical characteristics of the physical connection, the transmission techniques used, and the setup, maintenance and clearing of physical connections

   >"Communication protocols enable an entity in one host to interact with a corresponding entity at the same layer in another host. Service definitions, like the OSI Model, abstractly describe the functionality provided to an (N)-layer by an (N-1) layer, where N is one of the seven layers of protocols operating in the local host.
   >>
      At each level N, two entities at the communicating devices (layer N peers) exchange protocol data units (PDUs) by means of a layer N protocol. Each PDU contains a payload, called the service data unit (SDU), along with protocol-related headers or footers. Data processing by two communicating OSI-compatible devices proceeds as follows:

   1. The data to be transmitted is composed at the topmost layer of the transmitting device (layer N) into a protocol data unit (PDU).
   2. The PDU is passed to layer N-1, where it is known as the service data unit (SDU).
   3. At layer N-1 the SDU is concatenated with a header, a footer, or both, producing a layer N-1 PDU. It is then passed to layer N-2.
   4. The process continues until reaching the lowermost level, from which the data is transmitted to the receiving device.
   5. At the receiving device the data is passed from the lowest to the highest layer as a series of SDUs while being successively stripped from each layer's header or footer until reaching the topmost layer, where the last of the data is consumed."

**LDAP**: Lightweight Directory Access Protocol

- Standards-based protocol that sits on top of TCP/IP allowing clients to do  directory server operations:
- storing and retrieving data, searching for data matching a given set of criteria, authenticating clients, etc.
- Uses TCP port 389 for unencrypted communication & 636 for LDAP over a TLS-encrypted channel

>>
    IEEE 802.11 is a set of protocols within the IEEE 802 WLAN standards that specifies wireless protocols

___

## `Hardware`

### Memory

- DRAM & SRAM are most widely used types of RAM

1. `SRAM`  Static random access memory - Uses transistors to store information. Expensive and used for cache memory
2. `DRAM` Dynamic random access memory - Need to be refreshed to retain data. Usually used for main memory
3. `SDRAM`: new tech, supported by PC's that support 100MHz memory buses.
4. `EDO`: extended data out memory: type of RAM chip that makes improvemnts on time to read from memory
5. `ECC`: error checking and correcting memory: data that's read/transmitted is checked for errors and corrected
6. `ROM` - Read only memory - Data in ROM can not be erased or changed
7. `PROM` Programmable ROM - Once programmed, data can't be erased or change
8. `EPROM` - Erasable PROM - Data can be removed from PC curcuit, erased by ultraviolet (UV) light and then reprogrammed
9. `EEPROM` Electronically erasable PROM - Data can be erased with electrical signals.
   1. Chip can then be reprogrammed. Transistor uses 5v.
   2. EEPROMs are frequently used to store BIOS. Used to program dynamically
10. `SIMM` (installed in pairs & come in 30 and 72 pin formats) & DIMM (can be installed 1 at a time and com in 168 pin config)
11. `Unbuffered`
12. `Buffered`

### Storage and Peripherals

1. Hard drives are usually 2.5" form factor (desktops use 3.5")
   1. 2.5: better performance due to larger cache and higher rotation speed
   2. more available/cheaper than 1.8" drives that weigh less, consume less power, but have slower rotation speed & access time
      1. usually found in 10 inch or ultraportable laptops
2. drive tech: serial and parallel ATA
3. don't have separate power connectors
4. Form factors: 2.5”, 1.8”, or M.2
5. Magnetic disk drives
6. SSD
7. SCSI (Small Computer System Interface)
8. Sectors usually contain 512 bytes.
9. L1 is generally found in the processor chip and it's the smallest & fastest for the CPU to read. It ranges from 8-64KB.
   1. L2 and L3 are larger than L1 but take longer to access.

#### RAID

1. `RAID` (Redundant Array of independent disk) Types: Hardware & Software RAID
    1. RAID 0: Striping w/o parity and no fault tolerance
       1. min. 2 disks needed and read/write performance increase
    2. RAID 1: Mirroring and dubplexing.
       1. mirroring requires 2 equal sized pars on diff drives.
       2. disk duplexing req. 2 disk and 2 controllers.
       3. provides fault tolerance, w/ slower disk access compared to striping
    3. RAID 2 - striping w/ error correction
    4. RAID 3 - striping w/ error correction code stored as parity
       1. takes a striped array, then adds prity HDD to the array. The parity info is vital if a drive fails because it can restore blocks broken from data corruption. Parity written to 1 drive
    5. RAID 4: striping w/ large blocks allocation
    6. RAID 5: striping w/ parity. Requires 3 pars on diff drives.
       1. fault tolerant & less expensive than disk mirroring.
       2. data can't be recovered if >= 1 disk fails, so tape backups need to be used.
       3. spreading the parity info across all drives allows all the drives to rebuild the array if another fails.
    7. Mirroring has more overhead due to the entire drive being copied to another drive.
    8. RAID 10: mirrored stripping. Mode 0 array + mode 1 array, striped.
       1. ex. You striped data into 2 drives, then each drive is mirrored
       2. requires a total of 4 drives
    9. Disk swapping: Hot-swapping (Host plugging): ability to add/remove devices to PC while it's running & OS will auto recognize changes.
       1. cold: device needs powered down prior to replacing parts
       2. warm: The server can remain powered on, but I/O functions corresponding to the part that needs replaced need stopped by the appropriate command
       3. hot: the faulty part can be replaced w/o interrupting the srver or exec any interruption commands in I/O procedures.
2. `USB`
       1. universal serial bus 1.1 cocmes in 1.5 MB/s and 12 Mbps; USB 2..0 runs at 480 Mbps
       2. form factors: micro, USB-C, mini
       3. USB 3.0 runs at 5 Gbps; USB 3.1 at 10 Gbps
       4. USB ver. often use coors to show v.
       5. USB connectors come in many types:
          1. Type-A, B, C, standard, mini, micro
       6. all USB devices connect to USB controllers built into the otherboard of the system; the USB controller is in charge of all connect USB devices
       7. this creates n upstream/downstream concept
       8. USB-A connectors connect downstream; B connectors connect upstream (with some exceptions)
       9. must have a device driver; OS's come w/ thousands of built-in device drivers; may need to manually download from internet
3. `Thunder and Lightning`
    1. general purpose I/O port that runs at 10 Gbs up to 40 Gbps
    2. uses a mini DisplayPort or USB C connector
    3. exclusive to Apple and uses proprietary lightning connector
4. `Keyboards/Mice`
    1. keyboards use ither USB or PS/2 connection; while mice almost exclusively USB; game controllers often have proprietary connection that requires a converter piece
    2. keyboard video mouse (KVM) switches give ability for a single keyboard, monitor, mouse to connect multiple PC's
5. `RAM`
    1. SODIMM:
        1. multiple configurations: 200, 204, 260, or 292-pin
        2. 32 | 64-bit configurations
6. `Sight/Sound`
7. `Readers/Scanners`
8. `Expansion Cards`

___

## `Software`

- `SDK` is a kit that offers tools, code samples, libraries, processes, and guides for creating software applications on specific platforms.
- `API` is an interface that allows the software to interact with each other

### Windows Admin Tools

- Data usage - DusmSvc: net data use; limit and metered network; disable background data
- DNScache - DnsClient
- netman - network connections: manages objects in network folder for viewing LAN & remote connections
- UAC virtualization
- Event viewer/scheduler
- Performance diagnostic logger
- Windows SDK component
- ICANN - domain registry
- gpedit.msc => component config => admin template

### Windows Management Framework

1. Manage different version of Window client and servers
2. DSC - desired state configuration
3. ISE - integrated script environment
4. WinRM - windoes remote management
5. SIL - software inventory logging
6. Windows Page Manager Service (can use WinGet via CLI)
7. My analytics Dashboard
8. System Center Config Manager (SCCM)
9. Component Services Admin of COM, Apps, distrubted apps that're deployed in a server PC using MMC (Microsoft Management Console)

### Windows naming

- Windows naming is designed for LANs and when installed you give the PC a Windows name
- all Windows systems will be members of a domain or workgroup
- `homegroups` are more secure and automated organization (still a type of workgroup)
  - `workgroup` is basic type of networking organiztion used as an organizational tool w/ no security or central admin
  - `domain` is an organizational group (type used today is Active Directory domain) that provides central admin and has ability to disperse security and network info to other PC's at one time

___

### Displays

 1. Types
    1. backlight systems
       1. _CCFL_: cold cathode flourescent light - older, uses daylight specter flourescent tube and inverter for power
       2. _LED_: light emitting diodes - doesn't use inverter and uses strips of LEDs
          1. LCD blocks areas of backlight to create images
          2. LEDs generate light themselves and consumes less power
          3. Plasma: made of small cells of ionized gas (good contrast ratio)
    2. _CRT_: cathode ray tube
    3. _LCD_: requires backlight sys; uses liquid crystal displays
       1. frequent in laptops
    4. _OLED_: organic light emitting diode - thinner/lighter; made of a layer of organic compound between 2 light-emitting electrods
       1. common in handheld devices

___

## Mobile Devices

## References

>>
    Quoted & paraphrased information from personal notes and online resources

> [Quickstart](https://www.quickstart.com/blog/comptia-prep-identifying-motherboard-components-understanding-their-functions/) |
> [Wikipedia](https://en.wikipedia.org/wiki/User_Datagram_Protocol) |
> [LinkedIn Learning](https://www.linkedin.com/learning/comptia-a-plus-220-1001-cert-prep-6-physical-networking/introduction-to-networking) |
> [Become/ UnionTestPrep](https://uniontestprep.com/comptia-a-core-series-exam/study-guide/220-1101-networking/pages/1) |
> [Meyes Comptia Exam Guide/ McGrawHill](https://www.mheducation.com/highered/product/comptia-certification-all-one-exam-guide-tenth-edition-exams-220-1001-220-1002-meyers/M9781260454031.html) |

# CompTIA A+ Docs

| Hima Balde | PPU | 06-10 of 2022 |
|---|---|---|

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

## Parts

1. `CPU`(The Central Processing Unit) is the part of the computer that asks, "what's next"
2. `Main Memory`: stores prog. & data that CPU uses quickly and isn't saved on power off
3. `Secondary Memory`: also stores info; but is slower; keeps info even if PC has no power
   1. (ex. disk drives, flash memory - USBs)
4. `I/O devices`: input and output devices used to interact w/ the computer
5. `network connection`: get info over network; store/retrieve data (similar to secondary mem.)

### Motherboard

- `Power connectors` – Any component cannot operate without power and the same goes for a motherboard. The power connector is a 20/24-pin connector that sits near to the processor socket on some hardware while is present beside the right edge in others. It’s the area where the main connector attaches and thus, supplies power to all components.
- `Processor socket` – It is a central unit present on the motherboard located on the center and the main function of it is to hold the entire processor. In layman’s terms, it is called “the brain of a computer”.
- `Video card slot` – It does not require much explanation as it remains one of the most common components. Just as the name suggests, a video card slot attaches a card. It is a PCI-Express slot. High-end gaming PCs have motherboards that comprise of multiple video card slots.
- `Memory slots` – These slots are usually situated on the upper right area of the motherboard and carry a computer’s memory modules. Slots can differ in number and it usually depends on the motherboard. It starts at 2 and goes up to 8 slots. The latter number is usually present on gaming PCs’ motherboards. Users generally pay close attention to the memory of the motherboard when buying it. Modern motherboards have the DDR3 memory that is now industry standard. Basically, the number of slots determines the capacity of memory on a motherboard.
- `IDE & SATA ports` – These ports are used to allow connectivity for optical drives and storage devices. IDE is rather outdated, so it is not much common anymore to be found on motherboards. IDE was replaced by SATA interface because it is smaller and faster. In fact, it can allow speeds up to 600 MB/s.
- `Expansion slots` – Their primary function is to allow a user to attach additional hardware to optimize their PC’s performance. A user can install a high-performance sound card or a TV tuner.
- `Northbridge & Southbridge` – Looking at the motherboard, anyone can easily spot a square and metallic component on the bottom right area. This area is for the evacuation of heat building up in the system. It provides thermal protection for the Northbridge that is an important component of the motherboard. Northbridge coordinates the flow of data between video card, memory, and the processor. The Southbridge has the same function, only that it coordinates data flow between soundcards and the processor.
- `BIOS Chip & Battery` – The BIOS chip is a component which consists of a basic code required to carry out the boot process on a computer. The process goes on to the point where the operating system or OS takes over. BIOS is present on a memory chip, and this chip needs a constant supply of power in order to perform its function. However, the power supply can be cut if unplugged from the grid, which is why there is a battery that supplies adequate power to keep it running.
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

## OS Install, Upgrade, Boot

### _Boot methods_: user selects how to boot pc & w/ what media

1. optical disc (CD-ROM, DVD, Blu-ray): pc will prob have built-in drive to read them; very common way to install OS on a pc
2. external/flash drive (interfaces: USB, eSATA): ext optical/hard/flash drives, USB is common
3. Network boot (PXE): preboot eXecution Env.; boot from network resources; net & remote server hosting the bootable image need config.
   1. common in corp. env. where net & server resources are availalbe; allows setting up multiple pc's w/ similar images
4. internal fixed disk (HDD/SSD) & internal Hard Drive (Partition)
   1. disk can have OS install image or OS already installed. Most common way to boot PC after OS install completed
   2. simple configs have one bootable par on a disk, but a disk can have > 1 par to multiboot diff OS. One logical par can span multiple physical hard disks

| Install Types | |
| :---: | --- |
| _Type_ | _Description_ |
| 💻 | 📕 |
| unattended | pre-config., need special server w/ install image/script & good for many PC's w/ same config |
| in-place upgrade | installs newer OS over older one; may preserve settings, fi, apps |
| clean  | disregards previous data; used for PC w/o an OS or to intentionally delete old data |
| repair  | boot w/ same -v OS & select repair; rewrites SF & settings, retains user fi; can repair OS that's unbootable or w/ issues unfixable by other methods  |
| multiboot | uses boot mngr that maintains boot config; user sel OS to boot; recommend install OS's to diff HDD or separate logical pars |
| remote net | PXE net boot using remote server; may require choosing install options or be unattended |
| image deployment | used for PC's w/ == hardware that need == OS/settings/apps. Diff software tools can do this. Steps involve sel one PC => clean install, config, app install => create image from that PC & make available on network or portable media => copy image to other PC's |
| recovery par | create rec par during install that is a bootable par for later or repair install; contains diagnostic/repair tools |
| refresh/restore | pre-config. to restore OS to restore point; recom. before large config changes or software installs; settings can revert back to it |
| |
| **Partitioning**
|   |
| _Type_ | _Description_ |
| --- | --- |
| _Info_ |creates >= 1 logical drives; can be formatted separately & have separate FS. W10 allows each par to have diff drive letter
| Dynamic | more complex config & less limits than basic dsk. Can create pars spanning many physical HDD's (software RAID) |
| Basic | most common; separated into logical pars |
| Primary  | can have only one logical drive; W10 only boots from primary par |
| Extended  | enables >= 1 logical drive |
| logical | rep by a drive letter in W10; recomm. distinguishing btw dsk, par & logical drive; can be assigned 1:1 but aren't limited to 1 |
| GPT | GUID Par Table: has info on how dsk is partitioned. supports larger drives & more pars/drive than MBR |
|   |
| **File System Types/Formatting** |
| _Type_ | _Description_ |
| Info | Fs enables storing/managing/accessing fi on a par. OS's support diff FS & pars are formatted w/ specific FS before use
| ExFAT | designed for small flash & SSD drives, good for perf & media fi storage |
| FAT32 | supported by many OS & provides basic features. pars can be >= 2 TB |
| NTFS  | more advanced & supported by modern W --v. user can set/manage permissions for fi/dir for users/groups. useful for secure net fi sharing. Has indexing, compress., encrypt. on FS level  |
| CDFS  | FS for CD/DVD's |
| NFS | Network File System. mostly in servers where you can have fi access on net btw sys. |
| ext3, ext4 | used for Linux. 4 is updated -v that enables larger pars, fi & better perf |
| HFS | used for MacOS |
| Swap par | Linux par used when physical RAM is maxxed out. The Data flows to swap pars; reducing perf, in place of running more apps simultaneously. |
| quick vs. full format | quick changes FS records making dsk appear empty. Full rewrites prev fi, detects surface errors on dsk and makes restoring fi harder. |
| --- | --- |

### Misc

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

- IEEE (Institute of Electrical and Electronics Engineers) handles wired and wireless networking
- International Organization for Standardization (ISO) handles other types.
- 2 types of comms protocols:
  - binary utilizes all values of a byte; intended for machine reading; more terse and faster
  - text-based/plain text - only uses values corresponding to human-readable characters in ASCII encoding

### Rules governing the transmission specified by the protocol

1. Data and address formats for data exchange (and address mapping)
   1. exchange of digital message bitstrings (dividied in fields; header: fields w/ relevance to the op of the protocol and payload: where actual message is carried)
   2. addresses used to ID send and intedned receiver/s; carried in header of bitstrings; ID'd using an addy pair
   3. addy mapping: map addys of one scheme on addys of another scheme (ex. translate logical IP specified by app to an ethernet MAC addy)
2. routing: systems that aren't directly connected, using intermediary systems along the route to intended rec to forward data on behalf of sender, connected via routers
   1. internetworking: interconnection of networks via routers.
   2. Routing: sending data from source net to destination net. It's supported by host addressing and identification using hierarchical IP addy system.
3. detection of transmission erros: CRC of data area added to end of packets, allows rec to reject packets on CRC diff and arrange for retransmission
4. acknowledgement: recievers send acknowledgements of packets received correctly

   1. required for connection-oriented comms
   2. loss of info (timeouts and retries): packets can be lost on the net or delayed in transit
   3. the sender may expect an acknow. of correct reception from the rec w/in a certain amount of time.
   4. on timeouts: the sender may need to retransmit the information.
   5. retransmission has no effect when link is permanently broken, so the n of retransmissions is limited and if the limit is exceeded it's an error
   6. direction of info flow
   7. _media access control_
   8. half-duplex links: transmission via one direction at a t
   9. shared medium: transmission via 1 sender at a t
   10. sequence and flow control
   11. bitstrings are divided into pieces and sent on net indy; they can get lost, delayed, take diff routes and can result in pieces arriving out of seq. or retransm. creating duplicate pieces
   12. The data is marked w/ seq. info at the sender, so rec can figure out any issues to reassemble message or ask for retrans.
   13. flow control is needed when sender transmits faster than reciever & intermediate net equip can process the trans.
   14. queueing (buffers): ususally FIFO queues
   15. used to deal w/ message in order it was sent; can use multiple queues w/ diff priorities

### Common Internet Protocols, Data and File Sharing

### `TCP/IP`

- IP is responsible for delivering packets to the right comp.
- Transmission Control Protocol/Internet Protocol model: _standardized process_; data link protocol;Connection Oriented Communication
  - used to allow computers & devices connected to the internet to communicate w/ each other across networks
  - determines how PCs transfer data so that it's kept accurate.
  - assumes a connectionless net most suitable for LAN
  - data may be delivered out of order, since different network packets are routed independently and may be delivered over different paths
  - connection-oriented protocol and requires handshaking to set up end-to-end communications.
  - Once a connection is set up, user data may be sent bi-directionally over the connection
  - reliable; ordered; heavyweight; streaming
    - manages acknow, retransm., timeouts
    - attempts delivery of message multiple times and wil resend if data is lost (either no missing data or dropped conn)
    - will buffer the out of order data to proper order
    - requires three packets to set up a socket conn before data can be sent
    - handles reliability and congestion control
    - data read as a byte stream, no indications transmitted to signal message (segment) boundaries

1. breaks down data into packets and reassembles packeets into complete message on other end
   1. smaller packets makes it easier to maintain accuracy
   2. packets can travel via diff routes depending on congestion.
   3. Data divided into packets based on 4-layer procedure, going thru each layer in 1 order and reassembled on receiving end

### Abstraction Layers

- **`Link`** (network access)
  - operates w/in scope of local net conn. that a host is attached to. link includes all hosts accessible w/o traversing a router. link size is determined by the networking hardware design. TCP/IP designed to be hw indy and can be used on top any link-layer tech (ee.x. any hardware, virtual link layers like VPNS & tunnels)
  - includes protocols used for describing local net topology and interfaces needed to affect transmission of internet layer datagrams to other next-neighbor hosts.
  - moves packets btw internet layer interfaces of 2 diff hosts on same link. the transmitting/reciving packets link processes are controlled in device driver for network card, firmware and/or chipsets. (performing functions like framing- which prepares the internet layer packets for transmissions, and then transmit the frames to the physical layer over a transmission medium). TCP/IP has specs for translating net addy methods used in IP to link-layer addys, like MAC addys. Other aspects below that level, are implicitly assumed to exist and aren't explicitly defined.
  - corresponds w/ functions in Layer 2 of OSI model
- **`Internet`**
  - provides an unreliable datagram transmission facility between hosts located on diff IP nets by forwarding datagrams to appropriate next-hop router for further relaying to destination.
  - Essentially establishes the internet and is responsible for sending packets across multiple networks. Makes internetworking (the interworking of diff IP networks) possible
  - IP carries data for many upper layer protocols (each w/ unique protocol #s).
  - IP is principal component of internet layer and defines 2 addressing systems to ID network hosts and locate them on the network.
  - IPv4 uses 32-bit IP address and is capable
- **`Transport`**
- **`Application`**

### **Ports** and **Protocols**

1. `FTP`: 21 file-transfer oriented protocol that ensures data delivery; file transfer to/from server
   1. server that hosts files; allowing usrs to browse, transfer, upload files
2. `ssh`: 22 remote administration protocol where user can control/modify their remote servers over the internet; replaced unsecure telnet protocol
   1. uses cryptographic techniques to ensure communication to and from  as well as enrypting data
   2. provides secure communication between 2 untrusted hosts over an unsecured network
   3. Secure Shell: cryptographic net pro for operating network services securely over unsecured net
      1. ex. Access resources of a company branch in a different state
3. `Telnet`: 23, unencrypted remote device access
4. E-mail
   1. `SMTP` 25, simple mail transfer pro., sending email
   2. `POP3` 110, post office pro, receiving email
   3. `IMAP` 143, internet message access pro, receiving email
5. `RDP`: 27, reliable data protocol, provides facilities for remote loading, debugging and bulk transfer of images and data
   1. Remote Desktop Pro: 3389, used for connecting remote PCs
6. **DNS**: 54 domain name system, translates domain names to IP addresses
7. **HTTP**:hypertext transfer pro; standard for web comms; used for rendering pages in browser.
   1. **HTTPS**: secured comms. on web
8. `NetBios`/NetBT: 137-139 network basic input output system: LAN comms
9. `SMB`/CIFS:445 Server message block/Common internet file system; shared access on a network
10. `SLP`: 427 service location pro.; local service discovery
11. `AFP`: 548 Apple filling pro.; used for Apple file services
12. `DHCP`: 67/68, dynamic host config pro.; assigns IP addys to network hosts
13. `LDAP`: 389 Lightweight directory access pro; access a directory on network objects
14. `SNMP`: simple net mngmnt pro: send/rec net mngmnt messages
15. `Proxy Server`: features include access control, caching, URL filtering and privacy

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
  - Don't recognize MAC addys; Only send traffic coming in on one port out on every other port
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
  - manages IP settings for devices on its local network, (ex. auto & dynamically assigns IP addys to those devices)
  - auto assigns IP addresses and other comms param to devices connected to the net using a client–server architecture
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
  - No concept of acknow., retransm, timeout
  - no ordering of messages, no tracking conn
  - packets sent indy and checked for integrity on arrival, packets w/ defined boundaries that're honored upon receipt
  - doesn't avoid congestion; control measures have to be setup at app level or in net
  - UDP can broadcase - sent packets can be addressed to be rec by all devices on the subnet
  - multicast mode of op where a single datagram packet can auto route w/o dupe to a group of subs

> Although UDP provides integrity verification (via checksum) of the header and payload,[2] it provides no guarantees to the upper layer protocol for message delivery and the UDP layer retains no state of UDP messages once sent. For this reason, UDP sometimes is referred to as Unreliable Datagram Protocol.[3] If transmission reliability is desired, it must be implemented in the user's application.

### OSI model (Open systems interconnection)

- connection-oriented network
  - comms session or a semi-permanent connection is est. before any useful data can be transferred. The established connection ensures that data is delivered in the correct order to the upper communication layer.
- most suitable for WAN
- the layers comm. via an interface called service access point
  - protocol standards define how peer entities (corresponding layers at each sys.) comm
  - service standards define how one layer talks w/ the layer above it.
- comms between a computing system are split into 7 different abstraction layers:
  - Physical, Data Link, Network, Transport, Session, Presentation, Application

  - The _Application_ layer may provide the following services to the application processes: identification of the intended communication partners, establishment of the necessary authority to communicate, determination of availability and authentication of the partners, agreement on privacy mechanisms for the communication, agreement on responsibility for error recovery and procedures for ensuring data integrity, synchronization between cooperating application processes, identification of any constraints on syntax (e.g. character sets and data structures), determination of cost and acceptable quality of service, selection of the dialogue discipline, including required logon and logoff procedures.
  - The _presentation_ layer may provide the following services to the application layer: a request for the establishment of a session, data transfer, negotiation of the syntax to be used between the application layers, any necessary syntax transformations, formatting and special purpose transformations (e.g. data compression and data encryption).
  - The _session_ layer may provide the following services to the presentation layer: establishment and release of session connections, normal and expedited data exchange, a quarantine service which allows the sending presentation entity to instruct the receiving session entity not to release data to its presentation entity without permission, interaction management so presentation entities can control whose turn it is to perform certain control functions, resynchronization of a session connection, reporting of unrecoverable exceptions to the presentation entity.
  - The _transport_ layer provides reliable and transparent data transfer in a cost-effective way as required by the selected quality of service. It may support the multiplexing of several transport connections on to one network connection or split one transport connection into several network connections.
  - The _network_ layer does the setup, maintenance and release of network paths between transport peer entities. When relays are needed, routing and relay functions are provided by this layer. The quality of service is negotiated between network and transport entities at the time the connection is set up. This layer is also responsible for network congestion control
  - The _data_ link layer does the setup, maintenance and release of data link connections. Errors occurring in the physical layer are detected and may be corrected. Errors are reported to the network layer. The exchange of data link units (including flow control) is defined by this layer.
  - The _physical_ layer describes details like the electrical characteristics of the physical connection, the transmission techniques used, and the setup, maintenance and clearing of physical connections

   >
    "Communication protocols enable an entity in one host to interact with a corresponding entity at the same layer in another host. Service definitions, like the OSI Model, abstractly describe the functionality provided to an (N)-layer by an (N-1) layer, where N is one of the seven layers of protocols operating in the local host.
   >>
      At each level N, two entities at the communicating devices (layer N peers) exchange protocol data units (PDUs) by means of a layer N protocol. Each PDU contains a payload, called the service data unit (SDU), along with protocol-related headers or footers. Data processing by two communicating OSI-compatible devices proceeds as follows:

   1. The data to be transmitted is composed at the topmost layer of the transmitting device (layer N) into a protocol data unit (PDU).
   2. The PDU is passed to layer N-1, where it is known as the service data unit (SDU).
   3. At layer N-1 the SDU is concatenated with a header, a footer, or both, producing a layer N-1 PDU. It is then passed to layer N-2.
   4. The process continues until reaching the lowermost level, from which the data is transmitted to the receiving device.
   5. At the receiving device the data is passed from the lowest to the highest layer as a series of SDUs while being successively stripped from each layer's header or footer until reaching the topmost layer, where the last of the data is consumed."

___

### `Hardware`

### Storage and Peripherals

1. Magnetic disk drives
2. SSD
3. SCSI (Small Computer System Interface)
4. Boot order

5. L1 is generally found in the processor chip and it's the smallest & fastest for the CPU to read. It ranges from 8-64KB.
   1. L2 and L3 are larger than L1 but take longer to access.
6. f

7. RAID (Redundant Array of independent disk)
   1. hardware RAID
   2. troubleshooting

8. `Optical media`
9. `USB`
   1. universal serial bus 1.1 cocmes in 1.5 MB/s and 12 Mbps; USB 2..0 runs at 480 Mbps
   2. USB 3.0 runs at 5 Gbps; USB 3.1 at 10 Gbps
   3. USB ver. often use coors to show v.
   4. USB connectors come in many types:
      1. Type-A, B, C, standard, mini, micro
   5. all USB devices connect to USB controllers built into the otherboard of the system; the USB controller is in charge of all connect USB devices
   6. this creates n upstream/downstream concept
   7. USB-A connectors connect downstream; B connectors connect upstream (with some exceptions)
   8. must have a device driver; OS's come w/ thousands of built-in device drivers; may need to manually download from internet
10. `Thunder and Lightning`
    1. general purpose I/O port that runs at 10 Gbs up to 40 Gbps
    2. uses a mini DisplayPort or USB C connector
    3. exclusive to Apple and uses proprietary lightning connector
11. `Keyboards/Mice`
    1. keyboards use ither USB or PS/2 connection; while mice almost exclusively USB; game controllers often have proprietary connection that requires a converter piece
    2. keyboard video mouse (KVM) switches give ability for a single keyboard, monitor, mouse to connect multiple PC's
12. `Sight/Sound`
13. `Readers/Scanners`
14. `Expansion Cards`

___

### `Software`

- SDK is a kit that offers tools, code samples, libraries, processes, and guides for creating software applications on specific platforms.
- API is an interface that allows the software to interact with each other

### Windows Admin Tools

- Data usage - DusmSvc: net data use; limit and metered network; disable background data
- DNScache - DnsClient
- netman - network connections: manages objects in network foder for viewing LAN & remote connections
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
9. Component Services Admin of COM, Apps, distrubted apps thatre deployed in a server PC using MMC (Microsoft Management Console)

### Windows naming

- W10 naming is designed for LANs and when installed you give the PC a Windows name
- all W10 systems will be members of a domain or workgroup
- homegroups are more secure and automated organization (still a type of workgroup)
  - workgroup is basic type of networking organiztion used as an organizational tool w/ no security or central admin
  - domain is org group (type used today is Active Directory domain) that provides central admin and has ability to disperse security and net info to other PC's at one time
- g
- d
- d

### Mobile Devices

1. hard drives are usually 2.5" form factor (desktops use 3.5")
   1. 2.5: better perf due to larger cache and higher rotation speed
   2. more available/cheaper than 1.8" drives that weigh less, consume less power, but slower rotation speed & access time (usually in 10 inch or ultraportable laptops)
2. dirve tech: serial and parallel ATA
3. don't have separate power connectors

#### Displays

   1. Types
      1. backlight systems
         1. _CCFL_: cold cathode flourescent light - older, uses daylight specter flourescent tube and inverter for power
         2. _LED_: light emitting diodes - doesn't use inverter and uses strips of LEDs
            1. LCD blocks areas of backlight to create images
            2. LEDs generate light themselves and consumes less power
            3. Plasma: made of small cells of ionized gas (good contrast ratio)
      2. _LCD_: requires backlight sys; uses liquid crystal displays
         1. frequent in laptops
      3. _OLED_: organic light emitting diode - thinner/lighter; made of a layer of organic compound between 2 light-emitting electrods
         1. common in handheld devices
      4. _CRT_: cathode ray tube

### Referenced info and quoted material from personal notes and online resources

> [Quickstart](https://www.quickstart.com/blog/comptia-prep-identifying-motherboard-components-understanding-their-functions/) |
> [Wikipedia](https://en.wikipedia.org/wiki/User_Datagram_Protocol) |
> [LinkedInLearning](https://www.linkedin.com/learning/comptia-a-plus-220-1001-cert-prep-6-physical-networking/introduction-to-networking?autoplay=true&contextUrn=urn%3Ali%3AlearningCollection%3A6949411704820695040&resume=false&u=41913436)


# A+ sample questions

- [A+ sample questions](#a-sample-questions)
  - [Sections 220-1101](#sections-220-1101)
  - [Sections 220-1102](#sections-220-1102)
    - [Safety and Professionalism](#safety-and-professionalism)
    - [Hardware: Main overview](#hardware-main-overview)
    - [Wireless Networks](#wireless-networks)
      - [DNS database records](#dns-database-records)
      - [Network =\> IP Address, Types](#network--ip-address-types)
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
- threates & vulnerabilities
- SOHO security settings
- workstation security

- **Data & Remote Info**
- data destruction and disposal
- backup and recovery methods
- script files
- remote access tech

----------

### Safety and Professionalism

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
- toolkit should have atleast a Phillips-head screwdrive.
- create temporary passwords when working w/ clients, if you need to access their account, then change it afterwards.
- Follow up with clients after completing ticket
- antistatic straps keeps you at same electrical potential as the PC
- Backup data before working on client PC's and document findings

### Hardware: Main overview

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

### Wireless Networks

#### DNS database records

1. `A` record returns a 32-bit IP address.
2. `AAAA` record creates a pointer that maps a hostname to an IPv6 address.
3. `MX` record maps a domain name to a list of mail servers for that specific domain.
4. `TXT` records don't direct any traffic, but provides more info about a domain to outside services
   1. `TXT` records used for spam management:
      1. `SPF` - open standard that defines a method to prevent email sender address forgery. It allows the domain owner to list the servers that are allowed to send mail from the domain.
      2. `DKIM` - allows an email receiver to verify that an email claiming to come from a specific domain was actually authorized by the domain owner. It's an authentication method that allows using digital signature to sign outbound emails
      3. `DMARC` - has instructions for email recipient on how to handle emails that don't meet the sender's mail policies

#### Network => IP Address, Types

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

----------

## References and Resources

<!-- !['./prac.py'](https://)
![alt](https://) -->
[ExamCompass][exam_compass]

[exam_compass]: https://www.examcompass.com/comptia-a-plus-220-1101-exam-acronyms-quiz

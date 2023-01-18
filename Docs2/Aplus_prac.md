
# A+ sample questions

## 220-1101

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

#### Network -> IP Address, Types

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

## Sections 220-1101

### Cloud

- Cloud computing
- virtualization
- troubleshooting methodology

### Devices

- Laptop
- Display devices
- mobile devices
- printers

### Network

- protocols
- TCP & UDP Ports
- IP Addressing
- internet connection types
- services
- wireless
- hardware
- types
- tools

### Hardware

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

### OS

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

### Security

- physical
- logical
- wireless
- malware
- malware removal
- social engineering
- threates & vulnerabilities
- SOHO security settings
- workstation security

### Data & Remote Info

- data destruction and disposal
- backup and recovery methods
- script files
- remote access tech

## References and Resources

<!-- !['./prac.py'](https://)
![alt](https://) -->
[ExamCompass][exam_compass]

[exam_compass]: https://www.examcompass.com/comptia-a-plus-220-1101-exam-acronyms-quiz
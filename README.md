# Boris Mats — IT and Security Operations Portfolio

I'm moving into IT and security operations. Before this I spent nine years as a veterinary surgeon, and since 2024 I've worked as a government veterinary officer and lead epidemiological investigator at the Israeli Ministry of Agriculture, where the job is investigation: gather evidence from noisy sources, work out what actually happened, and write it up so it holds under scrutiny.

Everything in this repository I built and ran myself.

**Looking for a first role in Help Desk, NOC, or Tier 1 SOC.** Based in Holon, available for shift work.

CompTIA Security+ (SY0-701) · Google Cybersecurity Professional Certificate · TryHackMe Pre Security

---
---

## Projects

### 1. Windows Domain Controller and Group Policy Lab
**[→ ad-domain-gpo-lab](./ad-domain-gpo-lab)**

A Windows Server 2025 domain controller in VirtualBox, promoted to Active Directory Domain Services, with a Windows Pro client joined to the domain. Domain users and security groups created and managed. Group Policy Objects that standardise the desktop for one target group: enforced wallpaper, a deployed shortcut, and live machine and account details shown on the desktop background. Policy delivery verified on the client with `gpupdate` and `gpresult`.

This is the closest thing here to day-to-day first-line support: accounts, groups, permissions, and working out why a policy did or did not reach a machine.
---

### 2. Linux VPS Hardening and Cowrie Honeypot
**[→ vps-hardening](./vps-hardening)**

An internet-facing Ubuntu VPS on DigitalOcean, hardened and then deliberately given something to attack.

Hardening: Tailscale mesh VPN with UFW blocking public access to management ports, SSH restricted to the internal interface, password and root login disabled, key-based authentication only, non-default SSH port. Client side uses a passphrase-protected key pair and a `~/.ssh/config` for aliased access.

Honeypot: a Cowrie SSH honeypot on an isolated network layout, logging brute-force campaigns. Bash scripts handle log rotation and aggregation. Analysis covers attacker source addresses and geolocation, the credential lists being sprayed, and the payloads pulled down after access.

Artifacts: [VPS hardening documentation](./vps-hardening/ssh_config_guide/README.md) · [honeypot log analysis](/vps-hardening/honeypot/README.md)
---

### 3. Google Cybersecurity Labs
**[→ security-task-automation](./security-task-automation) · [→ reporting](./reporting)**

- **[Security task automation](./security-task-automation/File-Updates-in-Python/README.md)** — a Python script that maintains an IP allow-list: parsing the file, applying conditional logic, writing it back.
- **[Incident documentation](./reporting/security-incident-journal/README.md)** — incident state forms for a ransomware simulation, written against the NIST and SANS incident response lifecycle. Scoping, impact assessment, containment, eradication, recovery.
- **[DDoS analysis](./reporting/Incident-Report-Analysis/README.md)** — an ICMP flood traced from the outage back to the cause, with the response mapped to the NIST Cybersecurity Framework: rate limiting, spoofing defence, IPS and IDS placement.

---
---

## Skills

Grouped by what job postings actually ask for.

**Windows and end-user support.** Windows 10 and 11, Windows Server 2025, Active Directory Domain Services, Group Policy, user and security group administration, Event Viewer, printers and peripherals, Microsoft Office. Microsoft 365 administration is coursework so far, not yet hands-on — I would rather say that than pad the list.

**Networking.** TCP/IP, DNS, DHCP, HTTP/S, VPN, Wi-Fi. Packet capture and analysis in Wireshark and tcpdump, including port mirroring on a managed switch to see real traffic rather than lab traffic.

**Linux and scripting.** Ubuntu and Kali administration, UFW, SSH hardening, systemd, cron. Python for log parsing and data extraction, Bash for automation.

**Security monitoring.** Log analysis and alert triage, honeypot deployment and attacker behaviour analysis, incident documentation against NIST.

---
---

## Contact

Email: 5921189@gmail.com
LinkedIn: [boris-mats](https://www.linkedin.com/in/boris-mats-4b7102254/)

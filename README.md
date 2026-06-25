# cybersecurity-portfolio

# SOC Analyst Portfolio | Boris Mats

Hello! I am an aspiring Cybersecurity Analyst specializing in security monitoring, network traffic analysis, and incident management (Blue Team operations). I have a solid foundation in Linux administration, network protocols, and threat detection methodologies.

## Tech Stack & Skills
* **SIEM and Monitoring:** Log analysis, alert triage, creating detection rules.
* **Network Security:** Wireshark, Nmap, TCP/IP paradigm, VPN configuration.
* **Threat Intelligence & Analysis:** Honeypots (Cowrie), OSINT, PEStudio, malware behavior analysis.
* **OS and Scripting:** Linux System Administration (Bash), Automation (Python), Data Querying (SQL).
* **Certifications:** Google Cybersecurity Professional Certificate, CompTIA Security+ .

---

## Cybersecurity Projects

### Project 1: Linux VPS Hardening & Cowrie Honeypot Deployment
**Description:** A hands-on project focused on securing an internet-facing Linux cloud infrastructure and deploying a controlled decoy environment (honeypot) to capture and analyze real-world malicious cyber activity.

* **Infrastructure Hardening & Network Security:**
  * **Environment:** Provisioned and configured an Ubuntu VPS on DigitalOcean.
  * **Zero-Trust Network Access:** Integrated **Tailscale Mesh VPN** and configured **UFW (Uncomplicated Firewall)** to completely block public access to management ports, restricting SSH access strictly to the internal Tailscale network interface.
  * **SSH Daemon Hardening:** Disabled password authentication (`PasswordAuthentication no`) and root login (`PermitRootLogin no`), enforcing key-based authentication for standard users only. Changed the default SSH port to mitigate automated volumetric scanning.
  * **Client-Side Security:** Generated passphrase-protected SSH key pairs and optimized the local client workflow using a custom `~/.ssh/config` file for secure, aliased access.
* **Honeypot Deployment & Analysis:**
  * Deployed a **Cowrie SSH/Telnet Honeypot** on an isolated network layout to log brute-force campaigns.
  * Developed Bash scripts for automated log rotation and aggregation of Cowrie logs.
  * Analyzed automated attacker infrastructure, extracting malicious IP addresses (IP Geolocation), targeted credentials, and malware payloads.
* **Artifacts & Documentation:**
  * [Detailed VPS Hardening Documentation](./projects/vps-hardening/README.md)
  * [Honeypot Log Analysis Report](./projects/cowrie-analysis/README.md)

---

### Project 2: Google Cybersecurity Professional Labs (Threat Analysis & Incident Response)
**Description:** A compilation of practical labs and analytical reports completed during the Google Cybersecurity program, demonstrating proficiency with industry-standard SOC tools.

#### 1. Security Task Automation (Python & SQL)
* **Objective:** Developed a Python script to automate the updates of an IP address allow-list and used SQL queries to audit database access logs.
* **Skills Demonstrated:** Parsing text files in Python, conditional logic for security automation, and crafting optimized SQL queries for user privilege auditing.
* **Artifact:** [Python File Automation Script](./security-task-automation/File-Updates-in-Python/File-Updates-in-Python.md)

#### 2. Incident Documentation and Response Playbooks (NIST Framework)
* **Objective:** Documented security incidents (Incident State Forms) following the NIST/SANS Incident Response lifecycle based on a ransomware attack simulation.
* **Skills Demonstrated:** Incident scoping, impact assessment, and defining actionable containment, eradication, and recovery strategies.
* **Artifact:** [Security Incident Journal](./reporting/security-incident-journal.md)

#### 3. DDoS Attack Mitigation & Analysis (NIST CSF)
* **Objective:** Analyzed a sudden network outage caused by an ICMP flood attack and mapped the technical response strategy to the NIST Cybersecurity Framework.
* **Skills Demonstrated:** Incident lifecycle management, firewall rate-limiting configuration, IP spoofing defense, and IPS/IDS deployment planning.
* **Artifact:** [Incident Report Analysis](./reporting/Incident-Report-Analysis.md)

---

## Contact Me
* **Email:** 5921189@gmail.com
* **LinkedIn:** [Boris Mats](https://www.linkedin.com/in/boris-mats-4b7102254/)

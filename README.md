# cybersecurity-portfolio

# SOC Analyst (Tier 1) Portfolio | Boris Mats

Hello! I am an aspiring Cybersecurity Analyst specializing in security monitoring, network traffic analysis, and incident management (Blue Team operations). I have a solid foundation in Linux administration, network protocols, and threat detection methodologies.

## Tech Stack & Skills
* **SIEM and Monitoring:** Log analysis, alert triage, creating detection rules.
* **Network Security:** Wireshark, Nmap, TCP/IP paradigm, VPN configuration.
* **Threat Intelligence & Analysis:** Honeypots (Cowrie), OSINT, PEStudio, malware behavior analysis.
* **OS and Scripting:** Linux System Administration (Bash), Automation (Python), Data Querying (SQL).
* **Certifications:** Google Cybersecurity Professional Certificate, CompTIA Security+ .

---

## Cybersecurity Projects

### Project 1: VPS Hardening & Cowrie SSH/Telnet Honeypot Deployment
**Description:** A hands-on project focused on setting up a controlled environment (decoy) to capture, log, and analyze real-world malicious activity and brute-force attacks.

* **Architecture & Deployment:**
  * Provisioned a cloud VPS running Linux.
  * Configured a secure VPN tunnel for isolated administrative access.
  * Changed the default SSH port and deployed the **Cowrie Honeypot** .
* **Key Tasks Performed:**
  * Implemented firewall policies (UFW)
  * Developed Bash scripts for automated log rotation and aggregation of Cowrie JSON logs.
  * Analyzed automated brute-force campaigns: extracted attacker IP addresses (IP Geolocation), compiled lists of targeted credentials, and tracked downloaded malware payloads.
* **Artifacts & Documentation:**
  * [Honeypot Log Analysis Report](./projects/cowrie-analysis/README.md) 
  * [Sanitized Scripts](./projects/cowrie-analysis/configs/)

---

### Project 2: Google Cybersecurity Professional Labs (Threat Analysis & Incident Response)
**Description:** A compilation of practical labs and analytical reports completed during the Google Cybersecurity program, demonstrating proficiency with industry-standard SOC tools.

#### 1. Network Traffic Analysis & Scanning Detection (Wireshark & Nmap)
* **Objective:** Investigated PCAP files to identify unauthorized network scanning and potential vulnerability exploitation attempts.
* **Skills Demonstrated:** Identifying Nmap scan signatures (SYN, FIN, and Xmas scans), analyzing TCP streams, and detecting host compromise via anomalous traffic patterns.
* **Artifact:** [Network Incident Investigation Report](./google-labs/network-analysis-report.md)

#### 2. Security Task Automation (Python & SQL)
* **Objective:** Developed a Python script to automate the updates of an IP address allow-list and used SQL queries to audit database access logs.
* **Skills Demonstrated:** Parsing text files in Python, conditional logic for security automation, and crafting optimized SQL queries for user privilege auditing.
* **Artifact:** [Python File Automation Script](./security-task-automation/File-Updates-in-Python/File-Updates-in-Python.md)

#### 3. Incident Documentation & Response Playbooks (NIST Framework)
* **Objective:** Documented security incidents (Incident State Forms) following the NIST/SANS Incident Response lifecycle based on a ransomware attack simulation.
* **Skills Demonstrated:** Incident scoping, impact assessment, and defining actionable containment, eradication, and recovery strategies.
* **Artifact:** [Security Incident Journal](./reporting/security-incident-journal.md)

---

## Contact Me
* **Email:** 5921189@gmail.com
* **LinkedIn:** [Boris Mats](https://www.linkedin.com/in/boris-mats-4b7102254/)

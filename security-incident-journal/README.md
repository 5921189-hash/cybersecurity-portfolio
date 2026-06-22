#  Security Incident Detection and Response Journal

This repository contains my hands-on **Incident Analysis Journal** completed as part of the Google Cybersecurity Professional Certificate program. It documents my practical experience in analyzing threat vectors, utilizing OSINT/SIEM tools, and understanding the core mechanics of the Tier 1 SOC Analyst workflow.

---

## Security Toolbelt & Methodologies
* **OSINT and Malware Triage:** VirusTotal (Hash verification, URL analysis, IP reputation checking).
* **SIEM Operations:** Splunk (Log ingestion, event normalization, and search query execution).
* **Frameworks & Playbooks:** NIST SP 800-61 r2 Incident Response Lifecycle, Phishing Triage Playbooks.
* **Analytical Framework:** The 5 W's (Who, What, When, Where, Why) approach to incident scoping.

---

## Incident Log Entries

### 🔹 Entry 1: Ransomware Attack on Healthcare Provider
* **Date:** November 9, 2025
* **Context:** A ransomware attack targeted a small primary care medical organization.
* **The 5 W's Analysis:**
  * **Who:** An organized group of unethical hackers specializing in attacks on healthcare and transportation companies
  * **What:** Infecting computers with malware through phishing emails gave hackers access to the computers in order to encrypt data and then demand a large sum of money in exchange for a key to decrypt the data. This resulted in serious disruption to business operations as access to important patient data was lost.
  * **When:** Thursday at 09:00 AM.
  * **Where:** Local workstations and network endpoints via unauthorized remote access.
  * **Why:** Initial access was gained when an employee executed a malicious phishing attachment. Contributing factors include lack of email security gateway filtering, weak attachment inspection policies, and insufficient employee security awareness.
* **Takeaway & Remediation:** Immediate coordination with law enforcement is required. Critical need to evaluate data decryption options and implement an immutable, offline backup policy to ensure business continuity.

---

### 🔹 Entry 2: Workstation Malware Triage
* **Date:** November 17, 2025
* **Tools Used:** VirusTotal
* **The 5 W's Analysis:**
  * **Who:** Internal employee (unintentional insider threat via social engineering).
  * **What:** Execution of a malicious email attachment (executable file), resulting in the unauthorized creation of multiple malicious processes/files on the host.
  * **When:** 01:11 PM.
  * **Where:** Local employee workstation.
  * **Why:** Ingestion and execution of an untrusted file from a suspicious inbound email.
* **Takeaway & Remediation:** Deployed VirusTotal to analyze file hashes, relationships, and sandbox behavior. 
* **Defensive Recommendations:** Enforce execution restrictions (e.g., AppLocker/SRP) to block untrusted attachments from running directly from mail clients, and implement continuous security awareness training.

---

### 🔹 Entry 3: Phishing Alert Triage and Playbook Execution
* **Date:** November 18, 2025
* **Tools Used:** VirusTotal, Phishing Response Playbook
* **Context:** Response to alert ticket due to phishing playbook
* **The 5 W's Analysis:**
  * **Who:** External malicious actor. Email headers revealed a malformed sender address (missing '@' symbol) and an unaligned display name.
  * **What:** Phishing attempt leading to a potential malicious attachment execution/link click.
  * **When:** July 20, 2022, 09:30:14 AM 
  * **Where:** Employee endpoint (IP: `176.157.125.93`).
  * **Why:** Inadequate inbound email filtering allowed a malformed, malicious message into the inbox.
* **Takeaway & Remediation:** The alert was triaged as a True Positive. Cross-referencing the sender's IP on VirusTotal flagged it as a malicious infrastructure node originating from China. The attachment hash matched known malware signatures, and the email body contained distinct grammatical errors indicative of phishing.

---

### 🔹 Entry 4: Incident Final Report Review (Web Security)
* **Date:** November 22, 2025
* **Context:** Post-incident review of a data breach.
* **The 5 W's Analysis:**
  * **Who:** External malicious actor.
  * **What:** Data exfiltration achieved via Forced Browsing tactics.
  * **When:** December 28, 2022, at 07:20 PM.
  * **Where:** Corporate public-facing web application.
  * **Why:** Insecure URL access controls allowed unauthenticated users to guess and directly access restricted directory paths.
* **Takeaway & Remediation:** A critical observation from this report was a 6-day visibility gap between initial malicious activity and formal incident logging. 
* **Defensive Recommendations:** Enforce strict broken object-level authorization defenses on the web server, and optimize SIEM alerting thresholds to minimize time to detection.

---

### 🔹 Entry 5: Log Analysis and Security Event Auditing
* **Date:** November 28, 2025
* **Tools Used:** Splunk (SIEM)
* **Context:** Analyzing security events for "Buttercup Games."
* **Core Concepts Applied:** Structured log analysis using SIEM. Splunk was utilized to ingest, normalize, and filter massive log pools. Executed advanced search queries to isolate specific event fields, correlate time windows, and narrow down anomalies for deeper analysis.

---

## Personal Reflections & Professional Growth

#### Technical Obstacles Overcome
During the program, the official Splunk modules were modified/removed from the standard curriculum. Recognizing the criticality of SIEM proficiency for a Tier 1 SOC role, I took the initiative to source external, third-party Splunk labs and environments independently. This allowed me to master SIEM search syntax, query logic, and event correlation under realistic conditions.

#### Evolution of Security Mindset
This curriculum shifted my perspective from theoretical cybersecurity to structured, practical defense. I am now confident in executing specialized incident response playbooks, configuring intrusion detection system (IDS) rulesets like **Suricata**, leveraging **VirusTotal** for threat intelligence, and systematically breaking down logs to map out an adversary's footprint.

#### Favorite Tool Deep-Dive: VirusTotal & Cryptographic Hashes
My favorite concept explored was the application of cryptographic hashing for file integrity verification. Tools like VirusTotal provide an incredible macro-level view of threat intelligence through sandbox behavioral reports and community feedback. I have integrated this into my daily digital hygiene, verifying software hashes prior to installation.

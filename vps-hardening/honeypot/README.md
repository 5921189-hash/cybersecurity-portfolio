# Cowrie Honeypot: Log Management & Threat Intelligence

A lightweight, zero-dependency automation toolset designed to analyze, rotate, and extract actionable threat intelligence from Cowrie SSH/Telnet honeypot logs.

## Project Overview

This project focuses on operationalizing honeypot data. Instead of letting logs accumulate and consume disk space, this toolset provides:
1. **Log Rotation**: Automated log maintenance script to prevent disk exhaustion on low-resource VPS environments.
2. **Log Analysis**: Fast, memory-efficient Python script to identify top attacking IPs, target countries, and brute-forced credentials. 

---

## Scripts

* [log_rotator.sh](/security-task-automation/log_rotator.sh) - Shell script for managing log archives.
* [log_analyzer.py](/security-task-automation/log-analyzer.py) - Built-in Python script for parsing and geo-locating login attempts.
  

---

## Features And Mechanics

### 1. Log Rotation (`log_rotator.sh`)
* **Compression Tier (15+ Days):** Targets raw files older than 15 days and compresses them using gzip to dramatically reduce disk space consumption while preserving historical data.
* **Purge Tier (30+ Days):** Automatically discovers and permanently deletes files older than 30 days to avoid disk exhaustion vulnerabilities on the host system.
* **Safe Operations:** Explicitly filters out repository assets (e.g., matching .git* configurations) from destructive pipelines using native find exclusions.

### 2. Log Analyzer (`log_analyzer.py`)
* **Zero Dependencies**: Uses only native Python libraries (`json`, `urllib`, `collections`). Safe to run on production environments without installing third-party packages.
* **Memory Efficient**: Reads logs line-by-line using standard I/O streams, ensuring stable execution even on 1GB RAM virtual servers.
* **Threat Intelligence**: Aggregates data to surface the top 5 threat actors (with country detection via IP API), top targeted usernames, and top attempted passwords.


---

## Usage And Automation

### Prerequisites
* Python 3.x
* A Linux environment hosting an active Cowrie Honeypot deployment.

### Automated Scheduling with Cron For The Shell Script
The retention script is fully productionized to execute completely hands-free. It runs on a weekly schedule using the system's `crontab`, tracking performance indicators and error boundaries across independent log files.

To view or append this automation, access your task scheduler:
```bash
crontab -e
```
Add the following production configuration:
```text
0 0 * * 0 /home/cowrie/cowrie/scripts/log_rotator.sh >> /home/cowrie/cowrie/rotation.log 2>> /home/cowrie/cowrie/rotation.err
```

Cron Syntax Breakdown:

* `0 0 * * 0`: The script triggers automatically every Sunday at midnight (00:00).
* `>> /home/.../rotation.log`: Redirects normal standard output (stdout) to a centralized verification file to monitor which files were processed.
* `2>> /home/.../rotation.err`: Redirects runtime error outputs (stderr) to a dedicated file for rapid debugging and troubleshooting.
**Note:** You do not need to manually create `rotation.log` and `rotation.err` beforehand. Linux shell redirection (`>>` and `2>>`) will automatically generate these files upon the script's first execution if they do not exist.


### Running Analytics
To analyze your honeypot logs interactively, execute:
```bash
python3 scripts/log_analyzer.py
```

#### Interactive Prompts:

* Choose `y` to analyze the active `cowrie.json` file.
* Choose `n` to target a specific log file by date (`yyyy-mm-dd`).

#### Sample Output

```text
Processing log file /home/cowrie/cowrie/var/log/cowrie/cowrie.json.2026-06-20...

=== TOP 5 ATTACKING IPS AND COUNTRIES ===
IP: 103.13.206.18 [Singapore] -> 116 attacks
IP: 122.177.242.181 [India] -> 115 attacks
IP: 14.225.253.26 [Vietnam] -> 60 attacks
IP: 51.77.158.34 [France] -> 60 attacks
IP: 45.134.9.27 [Mexico] -> 58 attacks

=== TOP 5 USERNAMES ===
Username: root -> used 801 times
Username: 345gs5662d34 -> used 372 times
Username: ubuntu -> used 35 times
Username: admin -> used 31 times
Username: postgres -> used 11 times

=== TOP 5 PASSWORDS ===
Password: 3245gs5662d34 -> used 373 times
Password: 345gs5662d34 -> used 372 times
Password: 123456 -> used 94 times
Password: 123 -> used 42 times
Password: 1234 -> used 31 times
```


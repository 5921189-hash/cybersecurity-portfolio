# Cowrie Honeypot: Log Management & Threat Intelligence

A lightweight, zero-dependency automation toolset designed to analyze, rotate, and extract actionable threat intelligence from Cowrie SSH/Telnet honeypot logs.

## Project Overview

This project focuses on operationalizing honeypot data. Instead of letting logs accumulate and consume disk space, this toolset provides:
1. **Log Analysis**: Fast, memory-efficient Python script to identify top attacking IPs, target countries, and brute-forced credentials.
2. **Log Rotation**: Automated log maintenance script to prevent disk exhaustion on low-resource VPS environments.

---

## Scripts

* [log_analyzer.py](/cybersecurity-portfolio/blob/main/security-task-automation/log-analyzer.py) - Built-in Python script for parsing and geo-locating login attempts.
* [log_rotator.sh]() - Shell script for managing log archives.

---

## Features And Mechanics

### 1. Log Analyzer (`log_analyzer.py`)
* **Zero Dependencies**: Uses only native Python libraries (`json`, `urllib`, `collections`). Safe to run on production environments without installing third-party packages.
* **Memory Efficient**: Reads logs line-by-line using standard I/O streams, ensuring stable execution even on 1GB RAM virtual servers.
* **Threat Intelligence**: Aggregates data to surface the top 5 threat actors (with country detection via IP API), top targeted usernames, and top attempted passwords.

### 2. Log Rotation (`log_rotator.sh`)
* Automatically manages log sizes.
* Archives historical data to optimize disk space.

---

## Usage

### Log Analyzer

#### Prerequisites
* Python 3.x
* Active Cowrie Honeypot installation with JSON logging enabled.

#### Running Analytics
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
nan

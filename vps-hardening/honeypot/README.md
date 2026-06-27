# Cowrie Honeypot: Log Management & Threat Intelligence

A lightweight, zero-dependency automation toolset designed to analyze, rotate, and extract actionable threat intelligence from Cowrie SSH/Telnet honeypot logs.

## 🚀 Project Overview

This project focuses on operationalizing honeypot data. Instead of letting logs accumulate and consume disk space, this toolset provides:
1. **Log Analysis**: Fast, memory-efficient Python script to identify top attacking IPs, target countries, and brute-forced credentials.
2. **Log Rotation**: Automated log maintenance script to prevent disk exhaustion on low-resource VPS environments.

---

## 📁 Repository Structure

* `scripts/log_analyzer.py` - Built-in Python script for parsing and geo-locating login attempts.
* `scripts/log_rotator.sh` - Shell script for managing log archives.

---

## 📊 Features & Mechanics

### 1. Log Analyzer (`log_analyzer.py`)
* **Zero Dependencies**: Uses only native Python libraries (`json`, `urllib`, `collections`). Safe to run on production environments without installing third-party packages.
* **Memory Efficient**: Reads logs line-by-line using standard I/O streams, ensuring stable execution even on 1GB RAM virtual servers.
* **Threat Intelligence**: Aggregates data to surface the top 5 threat actors (with country detection via IP API), top targeted usernames, and top attempted passwords.

### 2. Log Rotation (`log_rotator.sh`)
* Automatically manages log sizes.
* Archives historical data to optimize disk space.

---

## 🛠️ Usage

### Prerequisites
* Python 3.x
* Active Cowrie Honeypot installation with JSON logging enabled.

### Running Analytics
To analyze your honeypot logs interactively, execute:
```bash
python3 scripts/log_analyzer.py

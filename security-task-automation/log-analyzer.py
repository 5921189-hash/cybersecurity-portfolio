import json
import urllib.request
from collections import Counter

last_log_file = None
LOG_FILE = None
log_date = ""

while last_log_file != "n" and last_log_file != "y":
    last_log_file = input("Do you want to choose the latest log file for analysis? (y/n) ").strip().lower()
    if last_log_file == "y":
        LOG_FILE = "/home/cowrie/cowrie/var/log/cowrie/cowrie.json"
    elif last_log_file == "n":
        log_date = input("Date for analysis (yyyy-mm-dd): ").strip()
        LOG_FILE = "/home/cowrie/cowrie/var/log/cowrie/cowrie.json." + log_date
    else:
        print("Invalid input. You can use only y or n")

if not LOG_FILE:
    print("Error: Log file path is not defined.")
    exit()


# Initializing counters
ips = Counter()
passwords = Counter()
usernames = Counter()

print(f"Processing log file /home/cowrie/cowrie/var/log/cowrie/cowrie.json.{log_date}...")
with open(LOG_FILE, "r", encoding="utf-8") as f:
    for line in f:
        try:
            event = json.loads(line)
            if "cowrie.login" in event.get("eventid", ""):
                ips[event.get("src_ip")] += 1
                passwords[event.get("password")] += 1
                usernames[event.get("username")] += 1
        except:
            continue

print("\n=== TOP 5 ATTACKING IPS AND COUNTRIES ===")
# Fetching country data for top 5 IPs via free API
for ip, count in ips.most_common(5):
    country = "Unknown"
    if ip:
        try:
            # Generating a link for a request to a free API
            url = f"http://ip-api.com/json/{ip}?fields=country"
            
            # Open the link and read the response (as in a regular browser)
            with urllib.request.urlopen(url, timeout=3) as response:
                geo_data = json.loads(response.read().decode())
                country = geo_data.get("country", "Unknown")
        except:
            country = "Network Error"

    print(f"IP: {ip} [{country}] -> {count} attacks")

print("\n=== TOP 5 USERNAMES ===")
for user, count in usernames.most_common(5):
    print(f"Username: {user} -> used {count} times")

print("\n=== TOP 5 PASSWORDS ===")
for pwd, count in passwords.most_common(5):
    print(f"Password: {pwd} -> used {count} times")
